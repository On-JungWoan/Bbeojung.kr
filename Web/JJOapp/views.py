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

#
import joblib
#
import datetime # 날짜시간 모듈
from datetime import date, datetime, timedelta
from .models import mean_sum, congestion, distance, population, Label, BusInfo

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
def info(request, dist, station, route):

    bs = BusInfo.objects.filter(dist=dist, name=station)
    id_ = str( BusInfo.objects.filter( name=station )[0].i )
    dong_ = BusInfo.objects.filter(name=station)[0].dong_name

    #distance
    dist_model = distance.objects.filter(i = id_)[0]
    dist_list = [
        dist_model.dis_5159, dist_model.dis_5745, dist_model.dis_5445,
        dist_model.dis_4475, dist_model.dis_4406, dist_model.dis_2002,
        dist_model.dis_2232, dist_model.dis_6130, dist_model.dis_3236
    ]

    #population
    pop_list = [population.objects.filter(dong_name=dong_)[0].population]

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
    r_model = mean_sum.objects.filter( r = r )[0]
    i_model = mean_sum.objects.filter( i = i )[0]
    w_model = mean_sum.objects.filter( w = w )[0]
    rw_model = mean_sum.objects.filter( rw = rw )[0]
    ri_model  = mean_sum.objects.filter( ri = ri )[0]
    iw_model  = mean_sum.objects.filter( iw = iw )[0]
    riw_model  = mean_sum.objects.filter( riw = riw )[0]

    mean_sum_list = [r_model.r_s, r_model.r_m, i_model.i_s, i_model.i_m, w_model.w_s, w_model.w_m, rw_model.rw_s,
                     rw_model.rw_m, ri_model.ri_s, ri_model.ri_m, iw_model.iw_s, iw_model.iw_m, riw_model.riw_s, riw_model.riw_m
                     ]


    #congestion
    con_list = [
        congestion.objects.filter(r=r)[0].r_con, congestion.objects.filter(i=i)[0].i_con, congestion.objects.filter(w=w)[0].w_con
            ]

    #whether
    whether_list = [36.5, 0, 0.7, 51]

    # encode
    encode_list = [
        Label.objects.filter(r=r)[0].r_encode,
        Label.objects.filter(i=i)[0].i_encode,
        Label.objects.filter(riw=riw)[0].riw_encode,
        Label.objects.filter(ri=ri)[0].ri_encode,
    ]


    #model
    path = 'D:/python_projects/BusStopCongestionProject/Model/7_model_LightGBM.pkl'
    loaded_model = joblib.load(path)

    feature = pd.DataFrame( np.array( dist_list + pop_list + mean_sum_list + con_list + [weekend] +
        whether_list + weekday + encode_list).reshape(1,-1) )
    feature.columns = ['dis_5159', 'dis_5745', 'dis_5445',
       'dis_4475', 'dis_4406', 'dis_2002', 'dis_2232', 'dis_1130', 'dis_3236',
       'population', '18~19_ride_ri_mean',
       '18~19_ride_ri_sum', '18~19_ride_r_mean', '18~19_ride_r_sum',
       '18~19_ride_i_mean', '18~19_ride_i_sum', '18~19_ride_w_mean',
       '18~19_ride_w_sum', '18~19_ride_rw_mean', '18~19_ride_rw_sum',
       '18~19_ride_iw_mean', '18~19_ride_iw_sum', '18~19_ride_riw_mean',
       '18~19_ride_riw_sum', 'route_congestion', 'id_congestion',
       'weekday_congestion', 'weekend', '기온', '강수량', '풍속', '습도',
       'weekday_0', 'weekday_1', 'weekday_2', 'weekday_3', 'weekday_4',
       'weekday_5', 'weekday_6', 'route_encode', 'id_encode',
       'route_id_weekday_encode', 'route_id_encode']

    prediction = loaded_model.predict(feature)
    print(prediction)

    context = {
        'dist' : dist,
        'station' : station,
        'route' : route,
        'bus' : bs,
        'predict' : prediction
    }

    return render(request, 'detail/index.html', context)

#
def detail(request):
    if request.method == 'POST':
        dist = request.POST.get('location')
        station = request.POST.get('category')
        route = request.POST.get('keyword')

    bs = BusInfo.objects.filter(dist=dist, name=station)
    id_ = str( BusInfo.objects.filter( name=station )[0].i )
    dong_ = BusInfo.objects.filter(name=station)[0].dong_name

    #distance
    dist_model = distance.objects.filter(i = id_)[0]
    dist_list = [
        dist_model.dis_5159, dist_model.dis_5745, dist_model.dis_5445,
        dist_model.dis_4475, dist_model.dis_4406, dist_model.dis_2002,
        dist_model.dis_2232, dist_model.dis_6130, dist_model.dis_3236
    ]

    #population
    pop_list = [population.objects.filter(dong_name=dong_)[0].population]

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
    r_model = mean_sum.objects.filter( r = r )[0]
    i_model = mean_sum.objects.filter( i = i )[0]
    w_model = mean_sum.objects.filter( w = w )[0]
    rw_model = mean_sum.objects.filter( rw = rw )[0]
    ri_model  = mean_sum.objects.filter( ri = ri )[0]
    iw_model  = mean_sum.objects.filter( iw = iw )[0]
    riw_model  = mean_sum.objects.filter( riw = riw )[0]

    mean_sum_list = [r_model.r_s, r_model.r_m, i_model.i_s, i_model.i_m, w_model.w_s, w_model.w_m, rw_model.rw_s,
                     rw_model.rw_m, ri_model.ri_s, ri_model.ri_m, iw_model.iw_s, iw_model.iw_m, riw_model.riw_s, riw_model.riw_m
                     ]


    #congestion
    con_list = [
        congestion.objects.filter(r=r)[0].r_con, congestion.objects.filter(i=i)[0].i_con, congestion.objects.filter(w=w)[0].w_con
            ]

    #whether
    whether_list = [36.5, 0, 0.7, 51]

    # encode
    encode_list = [
        Label.objects.filter(r=r)[0].r_encode,
        Label.objects.filter(i=i)[0].i_encode,
        Label.objects.filter(riw=riw)[0].riw_encode,
        Label.objects.filter(ri=ri)[0].ri_encode,
    ]


    #model
    path = 'D:/python_projects/BusStopCongestionProject/Model/7_model_LightGBM.pkl'
    loaded_model = joblib.load(path)

    feature = pd.DataFrame( np.array( dist_list + pop_list + mean_sum_list + con_list + [weekend] +
        whether_list + weekday + encode_list).reshape(1,-1) )
    feature.columns = ['dis_5159', 'dis_5745', 'dis_5445',
       'dis_4475', 'dis_4406', 'dis_2002', 'dis_2232', 'dis_1130', 'dis_3236',
       'population', '18~19_ride_ri_mean',
       '18~19_ride_ri_sum', '18~19_ride_r_mean', '18~19_ride_r_sum',
       '18~19_ride_i_mean', '18~19_ride_i_sum', '18~19_ride_w_mean',
       '18~19_ride_w_sum', '18~19_ride_rw_mean', '18~19_ride_rw_sum',
       '18~19_ride_iw_mean', '18~19_ride_iw_sum', '18~19_ride_riw_mean',
       '18~19_ride_riw_sum', 'route_congestion', 'id_congestion',
       'weekday_congestion', 'weekend', '기온', '강수량', '풍속', '습도',
       'weekday_0', 'weekday_1', 'weekday_2', 'weekday_3', 'weekday_4',
       'weekday_5', 'weekday_6', 'route_encode', 'id_encode',
       'route_id_weekday_encode', 'route_id_encode']

    prediction = loaded_model.predict(feature)
    print(prediction)

    context = {
        'dist' : dist,
        'station' : station,
        'route' : route,
        'bus' : bs,
        'predict' : prediction
    }

    return render(request, 'detail/index.html', context)