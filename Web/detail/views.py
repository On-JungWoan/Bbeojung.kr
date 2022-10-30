import numpy as np
import pandas as pd
from django.shortcuts import render, redirect
from .models import *
from .functions import make_infer, calc_remain
from secret import *
import random

#
def info(request, dist, id_, route):

    station = BusInfo.objects.filter( i=id_ )[0].name
    dong_ = BusInfo.objects.filter(name=station)[0].dong_name

    # predict_list = make_infer()

    # line_name, remain_min, remain_stop = calc_remain(id_)

    # try:
    #     line_idx = line_name.index(route)
    #     remain_data = [remain_min[line_idx], remain_stop[line_idx]]
    # except:
    #     remain_data = ['_', '_']

    time_ = random.randint(2,20)
    num = int(time_/2)

    predict_list = []
    for i in range(3):
        predict_list.append(random.randint(2,30))

    context = {
        'dist' : dist,
        'station' : station,
        'route' : route,
        'id' : id_,
        'bus' : BusInfo.objects.all(),
        'predict' : predict_list,
        'sum_': sum(predict_list),
        'mean_sum' : [5]*15,
        'total' : 58,
        'remain_data' : (time_, num)
    }
    return render(request, 'detail/index.html', context)


#
def detail(request):
    if request.method == 'POST':
        dist = request.POST.get('location')
        id_ = request.POST.get('category')

    route =  BusInfo.objects.filter( i=id_ )[0].r
    station = BusInfo.objects.filter( i=id_ )[0].name
    dong_ = BusInfo.objects.filter(name=station)[0].dong_name

    # predict_list = make_infer()

    # line_name, remain_min, remain_stop = calc_remain(id_)

    # try:
    #     line_idx = line_name.index(route)
    #     remain_data = [remain_min[line_idx], remain_stop[line_idx]]
    # except:
    #     remain_data = ['_', '_']

    time_ = random.randint(2,20)
    num = int(time_/2)

    predict_list = []
    for i in range(3):
        predict_list.append(random.randint(2,30))

    context = {
        'dist' : dist,
        'station' : station,
        'route' : route,
        'id' : id_,
        'bus' : BusInfo.objects.all(),
        'predict' : predict_list,
        'sum_': sum(predict_list),
        'mean_sum' : [5]*15,
        'total' : 58,
        'remain_data' : (time_, num)
    }
    return render(request, 'detail/index.html', context)


#
def search(request):
    if request.method == 'POST':
        station = request.POST.get('query')

    dist = BusInfo.objects.filter(name=station)[0].dist

    route =  BusInfo.objects.filter( name=station )[0].r
    id_ = str( BusInfo.objects.filter( name=station )[0].i )
    dong_ = BusInfo.objects.filter(name=station)[0].dong_name

    # predict_list = make_infer()

    # line_name, remain_min, remain_stop = calc_remain(id_)

    # try:
    #     line_idx = line_name.index(route)
    #     remain_data = [remain_min[line_idx], remain_stop[line_idx]]
    # except:
    #     remain_data = ['_', '_']

    time_ = random.randint(2,20)
    num = int(time_/2)

    predict_list = []
    for i in range(3):
        predict_list.append(random.randint(2,30))

    context = {
        'dist' : dist,
        'station' : station,
        'route' : route,
        'id' : id_,
        'bus' : BusInfo.objects.all(),
        'predict' : predict_list,
        'sum_': sum(predict_list),
        'mean_sum' : [5]*15,
        'total' : 58,
        'remain_data' : (time_, num)
    }
    return render(request, 'detail/index.html', context)