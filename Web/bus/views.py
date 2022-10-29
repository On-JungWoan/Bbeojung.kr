import numpy as np
import pandas as pd
from django.shortcuts import render, redirect
from .models import *
from .functions import make_infer
from secret import *

def test(request):
    context = {
        'key' : MAP_APP_KEY
    }
    return render(request, "main/test.html", context)


def about(request):
    a = [1,2,3,4]
    context = {
        'a' : a,
    }
    return render(request, "main/about-us.html", context)


def index(request):
    bs = BusInfo.objects.all()
    context = {
        'bus' : bs,
        'key' : MAP_APP_KEY
    }
    return render(request, "main/index.html", context)


#
def info(request, dist, id_, route):

    if ( (len(BusInfo.objects.filter( r=route ))==0) or (route=='') ):
        route =  BusInfo.objects.filter( i=id_ )[0].r
    station = BusInfo.objects.filter( i=id_ )[0].name
    dong_ = BusInfo.objects.filter(name=station)[0].dong_name

    predict_list = make_infer()

    context = {
        'dist' : dist,
        'station' : station,
        'route' : route,
        'id' : id_,
        'bus' : BusInfo.objects.all(),
        'predict' : predict_list,
        'sum_': sum(predict_list),
        'mean_sum' : [5]*15,
        'total' : 150,
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

    predict_list = make_infer()

    context = {
        'dist' : dist,
        'station' : station,
        'route' : route,
        'id' : id_,
        'bus' : BusInfo.objects.all(),
        'predict' : predict_list,
        'sum_': sum(predict_list),
        'mean_sum' : [5]*15,
        'total' : 150,
    }
    return render(request, 'detail/index.html', context)


#
def search(request):
    if request.method == 'POST':
        station = request.POST.get('query')

    dist = BusInfo.objects.filter(name=station)[0].dist
    route = ''

    if ( (len(BusInfo.objects.filter( r=route ))==0) or (route=='') ):
        route =  BusInfo.objects.filter( name=station )[0].r
    id_ = str( BusInfo.objects.filter( name=station )[0].i )
    dong_ = BusInfo.objects.filter(name=station)[0].dong_name

    predict_list = make_infer()

    context = {
        'dist' : dist,
        'station' : station,
        'route' : route,
        'id' : id_,
        'bus' : BusInfo.objects.all(),
        'predict' : predict_list,
        'sum_': sum(predict_list),
        'mean_sum' : [5]*15,
        'total' : 150,
    }

    return render(request, 'detail/index.html', context)