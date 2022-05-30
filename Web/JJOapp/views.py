# from apscheduler.schedulers.background import BackgroundScheduler
# import sklearn
# from urllib.parse import urlencode, quote_plus, unquote
# import requests
# from .Map_grid import mapToGrid
# import models
# import time
import pandas as pd
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
#
import joblib
#
import datetime # 날짜시간 모듈
from datetime import date, datetime, timedelta

def index(request):
    return render(request, "main/index.html")


#
def predict_output(request, ars_id, route):

    # weekday one-hot encoding
    weekday=[0,0,0,0,0,0,0]
    weekday[datetime.today().weekday()] = 1

    # weekend
    if datetime.today().weekday() >= 5:
        weekend = 1
    else :
        weekend = 0

    return render(request, 'detail/index.html')