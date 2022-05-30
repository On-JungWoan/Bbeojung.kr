# import os
# import django
# import requests, bs4
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# django.setup()
# from JJOapp.Map_grid import mapToGrid
# from JJOapp.models import Bus_stop, WeatherDB
# from urllib.parse import urlencode, quote_plus, unquote
# import datetime # 날짜시간 모듈
# from datetime import date, datetime, timedelta
# import requests
# import pandas as pd
# import json
# from urllib import request
#
#
# def check_weather(nx, ny):
#
#     url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"
#
#     serviceKey = "IkwYEWiPWior39UF5%2BeuNa8RFPbJwwib3HDmhR3FKgXKMDX%2F%2FEiXqpmWKPd4oW%2FN2EtbIxWTl2EvPWdI%2Fxgqfg%3D%3D"
#     serviceKeyDecoded = unquote(serviceKey, 'UTF-8')
#
#     now = datetime.now()
#     today = datetime.today().strftime("%Y%m%d")
#     y = date.today() - timedelta(days=1)
#     yesterday = y.strftime("%Y%m%d")
#
#     if now.minute < 45:  # base_time와 base_date 구하는 함수
#         if now.hour == 0:
#             base_time = "2330"
#             base_date = yesterday
#         else:
#             pre_hour = now.hour - 1
#             if pre_hour < 10:
#                 base_time = "0" + str(pre_hour) + "30"
#             else:
#                 base_time = str(pre_hour) + "30"
#             base_date = today
#     else:
#         if now.hour < 10:
#             base_time = "0" + str(now.hour) + "30"
#         else:
#             base_time = str(now.hour) + "30"
#         base_date = today
#     base_time = '0500'
#     queryParams = '?' + urlencode({quote_plus('serviceKey'): serviceKeyDecoded, quote_plus('base_date'): base_date,
#                                     quote_plus('base_time'): base_time, quote_plus('nx'): nx, quote_plus('ny'): ny
#                                     ,quote_plus('dataType'): 'json', quote_plus('numOfRows'): '60'})
#     response = request.urlopen(url+queryParams).read()
#     response = json.loads(response)
#
#     weather_data = dict()
#     items = response['response']['body']['items']['item']
#
#
#     for item in items:
#         weather_data['date']=item['fcstDate']
#         weather_data['Time']=item['fcstTime']
#         # 기온
#         if item['category'] == 'TMP':
#             weather_data['tmp'] = item['fcstValue']
#         # 습도
#         if item['category'] == 'REH':
#             weather_data['hum'] = item['fcstValue']
#         # 하늘상태: 맑음(1) 구름많은(3) 흐림(4)
#         if item['category'] == 'SKY':
#             weather_data['sky'] = item['fcstValue']
#         #강수형태
#         if item['category']=='PTY':
#             weather_data['rainType'] = item['fcstValue']
#         # 1시간 동안 강수량
#         if item['category'] == 'PCP':
#             weather_data['rain'] = item['fcstValue']
#         #풍속
#         if item['category']=='WSD':
#             weather_data['windspeed'] = item['fcstValue']
#
#
#     print("response: ", weather_data)
#     # print(weather_data['tmp'])
#     return weather_data
#
#
# bus= Bus_stop.objects.values('ARS_ID')
# records = WeatherDB.objects.all()
# records.delete()
# print(bus[0])
# for id in bus:
#     id = id['ARS_ID']
#     a=Bus_stop.objects.get(ARS_ID=id)
#     nx, ny = mapToGrid(a.lat, a.lon)
#     data = check_weather(nx, ny)
#     if data['rain']=='강수없음':
#         data['rain']=0
#     WeatherDB.objects.get_or_create(
#         ARS_ID=id,
#         lon=a.lon,
#         lat=a.lat,
#         Date=data['date'],
#         OneTime=data['Time'],
#         sky = data['sky'],
#         humidity = data['hum'],
#         rainType = data['rainType'],
#         temp = data['tmp'],
#         rain = data['rain'],
#         windspeed = data['windspeed'],
#     )
#
#     print("weatherDB saved")
#     print("************************")
