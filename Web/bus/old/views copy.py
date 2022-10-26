# from apscheduler.schedulers.background import BackgroundScheduler
# import sklearn
# from urllib.parse import urlencode, quote_plus, unquote
# import requests
# from .Map_grid import mapToGrid
# import models
# import time
import numpy as np
import pandas as pd
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# from pycaret.regression import *

#
import joblib
#
import datetime # 날짜시간 모듈
from datetime import date, datetime, timedelta
from .models import *

from django.views.generic import View

class MyView(View):
    def get(self, request):
        return render(request, "main/index.html")

def about(request):
    a = [1,2,3,4]
    context = {
        'a' : a,
    }
    render(request, "main/about-us.html", context)

def index(request):
    bs = BusInfo.objects.all()
    context = {
        'bus' : bs
    }
    return render(request, "main/index.html", context)

#
def info(request, dist, id_, route):

    if ( (len(BusInfo.objects.filter( r=route ))==0) or (route=='') ):
        route =  BusInfo.objects.filter( i=id_ )[0].r
    station = BusInfo.objects.filter( i=id_ )[0].name
    dong_ = BusInfo.objects.filter(name=station)[0].dong_name

    #distance
    try:
        dist_model = distance.objects.filter(i = id_)[0]
        dist_list = [
            dist_model.dis_0, dist_model.dis_1, dist_model.dis_2,
            dist_model.dis_3, dist_model.dis_4, dist_model.dis_5,
            dist_model.dis_6, dist_model.dis_7, dist_model.dis_8
        ]
    except:
        dist_list = [
            9.623654997, 8.208407938, 8.944554846, 8.42822716, 7.733141688, 6.780249414, 6.90795094,
            8.019099519, 8.506656788
        ]


    # weekday one-hot encoding
    weekday = [0, 0, 0, 0, 0, 0, 0]
    wd = datetime.today().weekday()
    weekday[wd] = 1

    # weekend
    if datetime.today().weekday() >= 5:
        weekend = 1
    else:
        weekend = 0

    #mean_sum
    r = route
    i = id_
    w = str(wd)
    rw = route + '_' + str(wd)
    ri = route + '_' + id_
    iw = id_ + '_' + str(wd)
    riw = route + '_' + id_ + '_' + str(wd)
    length = len(BusInfo.objects.filter(i=i))

    mean_sum_list = []
    ms_model_list = [r_mean_sum, i_mean_sum, w_mean_sum, rw_mean_sum, ri_mean_sum, iw_mean_sum, riw_mean_sum]
    ms_param_list = [r, i, w, rw, ri, iw, riw]

    for i in range( len(ms_model_list) ):
        try:
            md = ms_model_list[i].objects.filter( target = ms_param_list[i] )[0]
            mean_sum_list.append(md.m)
            mean_sum_list.append(md.s)
        except:
            mean_sum_list.append(0)
            mean_sum_list.append(0)

    #congestion
    con_list = []
    con_model_list = [r_congestion, i_congestion, w_congestion]
    con_param_list = [r, i, w]

    for i in range( len(con_model_list) ):
        try:
            md = con_model_list[i].objects.filter( target = con_param_list[i] )[0]
            con_list.append(md.con)
        except:
            con_list.append(0)

    #population
    pop_list = [BusInfo.objects.filter(dong_name=dong_)[0].population]

    #whether
    whether_list = [36.5, 0, 0.7, 51]

    # # encode
    # encode_list = [
    #     Label.objects.filter(r=r)[0].r_encode,
    #     Label.objects.filter(i=i)[0].i_encode,
    #     Label.objects.filter(riw=riw)[0].riw_encode,
    #     Label.objects.filter(ri=ri)[0].ri_encode,
    # ]


    #model
    feature = pd.DataFrame( np.array( dist_list + pop_list + mean_sum_list + con_list + [weekend] +
        whether_list + weekday).reshape(1,-1) )

    feature.columns = ['dis_0', 'dis_1', 'dis_2',
       'dis_3', 'dis_4', 'dis_5', 'dis_6', 'dis_7', 'dis_8',
       'population', 'ri_mean',
       'ri_sum', 'r_mean', 'r_sum',
       'i_mean', 'i_sum', 'w_mean',
       'w_sum', 'rw_mean', 'rw_sum',
       'iw_mean', 'iw_sum', 'riw_mean',
       'riw_sum', 'route_congestion', 'id_congestion',
       'weekday_congestion', 'weekend', '기온', '강수량', '풍속', '습도',
       'weekday_0', 'weekday_1', 'weekday_2', 'weekday_3', 'weekday_4',
       'weekday_5', 'weekday_6']

    predict_list = []
    for i in range( 6, 23, 2 ):
        path = 'Model/' + str(i) + '_' + str(i + 1) + '_model_pycaret.pkl'
        predict_list.append( int(joblib.load(path).predict(feature)[0]) )

    context = {
        'dist' : dist,
        'station' : station,
        'route' : route,
        'id' : id_,
        'bus' : BusInfo.objects.all(),
        'predict' : predict_list,
        'sum_': sum(predict_list),
        'mean_sum' : mean_sum_list,
        'total' : mean_sum_list[2] * length,
    }

    return render(request, 'detail/index.html', context)

#
def detail(request):
    if request.method == 'POST':
        dist = request.POST.get('location')
        id_ = request.POST.get('category')
        route = request.POST.get('keyword')

    if ( (len(BusInfo.objects.filter( r=route ))==0) or (route=='') ):
        route =  BusInfo.objects.filter( i=id_ )[0].r
    station = BusInfo.objects.filter( i=id_ )[0].name
    dong_ = BusInfo.objects.filter(name=station)[0].dong_name

    #distance
    try:
        dist_model = distance.objects.filter(i = id_)[0]
        dist_list = [
            dist_model.dis_0, dist_model.dis_1, dist_model.dis_2,
            dist_model.dis_3, dist_model.dis_4, dist_model.dis_5,
            dist_model.dis_6, dist_model.dis_7, dist_model.dis_8
        ]
    except:
        dist_list = [
            9.623654997, 8.208407938, 8.944554846, 8.42822716, 7.733141688, 6.780249414, 6.90795094,
            8.019099519, 8.506656788
        ]


    # weekday one-hot encoding
    weekday = [0, 0, 0, 0, 0, 0, 0]
    wd = datetime.today().weekday()
    weekday[wd] = 1

    # weekend
    if datetime.today().weekday() >= 5:
        weekend = 1
    else:
        weekend = 0

    #mean_sum
    r = route
    i = id_
    w = str(wd)
    rw = route + '_' + str(wd)
    ri = route + '_' + id_
    iw = id_ + '_' + str(wd)
    riw = route + '_' + id_ + '_' + str(wd)
    length = len(BusInfo.objects.filter(i=i))

    mean_sum_list = []
    ms_model_list = [r_mean_sum, i_mean_sum, w_mean_sum, rw_mean_sum, ri_mean_sum, iw_mean_sum, riw_mean_sum]
    ms_param_list = [r, i, w, rw, ri, iw, riw]

    for i in range( len(ms_model_list) ):
        try:
            md = ms_model_list[i].objects.filter( target = ms_param_list[i] )[0]
            mean_sum_list.append(md.m)
            mean_sum_list.append(md.s)
        except:
            mean_sum_list.append(0)
            mean_sum_list.append(0)

    #congestion
    con_list = []
    con_model_list = [r_congestion, i_congestion, w_congestion]
    con_param_list = [r, i, w]

    for i in range( len(con_model_list) ):
        try:
            md = con_model_list[i].objects.filter( target = con_param_list[i] )[0]
            con_list.append(md.con)
        except:
            con_list.append(0)

    #population
    pop_list = [BusInfo.objects.filter(dong_name=dong_)[0].population]

    #whether
    whether_list = [36.5, 0, 0.7, 51]

    # # encode
    # encode_list = [
    #     Label.objects.filter(r=r)[0].r_encode,
    #     Label.objects.filter(i=i)[0].i_encode,
    #     Label.objects.filter(riw=riw)[0].riw_encode,
    #     Label.objects.filter(ri=ri)[0].ri_encode,
    # ]


    #model
    feature = pd.DataFrame( np.array( dist_list + pop_list + mean_sum_list + con_list + [weekend] +
        whether_list + weekday).reshape(1,-1) )

    feature.columns = ['dis_0', 'dis_1', 'dis_2',
       'dis_3', 'dis_4', 'dis_5', 'dis_6', 'dis_7', 'dis_8',
       'population', 'ri_mean',
       'ri_sum', 'r_mean', 'r_sum',
       'i_mean', 'i_sum', 'w_mean',
       'w_sum', 'rw_mean', 'rw_sum',
       'iw_mean', 'iw_sum', 'riw_mean',
       'riw_sum', 'route_congestion', 'id_congestion',
       'weekday_congestion', 'weekend', '기온', '강수량', '풍속', '습도',
       'weekday_0', 'weekday_1', 'weekday_2', 'weekday_3', 'weekday_4',
       'weekday_5', 'weekday_6']

    predict_list = []
    for i in range( 6, 23, 2 ):
        path = 'Model/' + str(i) + '_' + str(i + 1) + '_model_pycaret.pkl'
        predict_list.append( int(joblib.load(path).predict(feature)[0]) )

    context = {
        'dist' : dist,
        'station' : station,
        'route' : route,
        'id' : id_,
        'bus' : BusInfo.objects.all(),
        'predict' : predict_list,
        'sum_': sum(predict_list),
        'mean_sum' : mean_sum_list,
        'total' : mean_sum_list[2] * length,
    }

    return render(request, 'detail/index.html', context)

def search(request):
    if request.method == 'POST':
        station = request.POST.get('query')

    dist = BusInfo.objects.filter(name=station)[0].dist
    route = ''

    if ( (len(BusInfo.objects.filter( r=route ))==0) or (route=='') ):
        route =  BusInfo.objects.filter( name=station )[0].r
    id_ = str( BusInfo.objects.filter( name=station )[0].i )
    dong_ = BusInfo.objects.filter(name=station)[0].dong_name

    #distance
    try:
        dist_model = distance.objects.filter(i = id_)[0]
        dist_list = [
            dist_model.dis_0, dist_model.dis_1, dist_model.dis_2,
            dist_model.dis_3, dist_model.dis_4, dist_model.dis_5,
            dist_model.dis_6, dist_model.dis_7, dist_model.dis_8
        ]
    except:
        dist_list = [
            9.623654997, 8.208407938, 8.944554846, 8.42822716, 7.733141688, 6.780249414, 6.90795094,
            8.019099519, 8.506656788
        ]


    # weekday one-hot encoding
    weekday = [0, 0, 0, 0, 0, 0, 0]
    wd = datetime.today().weekday()
    weekday[wd] = 1

    # weekend
    if datetime.today().weekday() >= 5:
        weekend = 1
    else:
        weekend = 0

    #mean_sum
    r = route
    i = id_
    w = str(wd)
    rw = route + '_' + str(wd)
    ri = route + '_' + id_
    iw = id_ + '_' + str(wd)
    riw = route + '_' + id_ + '_' + str(wd)
    length = len(BusInfo.objects.filter(i=i))

    mean_sum_list = []
    ms_model_list = [r_mean_sum, i_mean_sum, w_mean_sum, rw_mean_sum, ri_mean_sum, iw_mean_sum, riw_mean_sum]
    ms_param_list = [r, i, w, rw, ri, iw, riw]

    for i in range( len(ms_model_list) ):
        try:
            md = ms_model_list[i].objects.filter( target = ms_param_list[i] )[0]
            mean_sum_list.append(md.m)
            mean_sum_list.append(md.s)
        except:
            mean_sum_list.append(0)
            mean_sum_list.append(0)

    #congestion
    con_list = []
    con_model_list = [r_congestion, i_congestion, w_congestion]
    con_param_list = [r, i, w]

    for i in range( len(con_model_list) ):
        try:
            md = con_model_list[i].objects.filter( target = con_param_list[i] )[0]
            con_list.append(md.con)
        except:
            con_list.append(0)

    #population
    pop_list = [BusInfo.objects.filter(dong_name=dong_)[0].population]

    #whether
    whether_list = [36.5, 0, 0.7, 51]

    # # encode
    # encode_list = [
    #     Label.objects.filter(r=r)[0].r_encode,
    #     Label.objects.filter(i=i)[0].i_encode,
    #     Label.objects.filter(riw=riw)[0].riw_encode,
    #     Label.objects.filter(ri=ri)[0].ri_encode,
    # ]


    #model
    feature = pd.DataFrame( np.array( dist_list + pop_list + mean_sum_list + con_list + [weekend] +
        whether_list + weekday).reshape(1,-1) )

    feature.columns = ['dis_0', 'dis_1', 'dis_2',
       'dis_3', 'dis_4', 'dis_5', 'dis_6', 'dis_7', 'dis_8',
       'population', 'ri_mean',
       'ri_sum', 'r_mean', 'r_sum',
       'i_mean', 'i_sum', 'w_mean',
       'w_sum', 'rw_mean', 'rw_sum',
       'iw_mean', 'iw_sum', 'riw_mean',
       'riw_sum', 'route_congestion', 'id_congestion',
       'weekday_congestion', 'weekend', '기온', '강수량', '풍속', '습도',
       'weekday_0', 'weekday_1', 'weekday_2', 'weekday_3', 'weekday_4',
       'weekday_5', 'weekday_6']

    predict_list = []
    for i in range( 6, 23, 2 ):
        path = 'Model/' + str(i) + '_' + str(i + 1) + '_model_pycaret.pkl'
        predict_list.append( int(joblib.load(path).predict(feature)[0]) )

    context = {
        'dist' : dist,
        'station' : station,
        'route' : route,
        'id' : id_,
        'bus' : BusInfo.objects.all(),
        'predict' : predict_list,
        'sum_': sum(predict_list),
        'mean_sum' : mean_sum_list,
        'total' : mean_sum_list[2] * length,
    }

    return render(request, 'detail/index.html', context)