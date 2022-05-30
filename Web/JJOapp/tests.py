# import os
# import django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# django.setup()
# from JJOapp.Map_grid import mapToGrid
# from JJOapp.models import Bus_stop, WeatherDB
# from urllib.parse import urlencode, quote_plus, unquote
# import datetime # 날짜시간 모듈
# from datetime import date, datetime, timedelta
# import requests
# import json
# def check_weather(nx, ny):
#
#     url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst"
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
#
#     queryParams = '?' + urlencode({quote_plus('serviceKey'): serviceKeyDecoded, quote_plus('base_date'): base_date,
#                                     quote_plus('base_time'): base_time, quote_plus('nx'): nx, quote_plus('ny'): ny,
#                                     quote_plus('dataType'): 'json'})
#
#     # 값 요청 (웹 브라우저 서버에서 요청 - url주소와 )
#     res = requests.get(url + queryParams, verify=False)
#     print(res)
#     rest = res.json().get('response')
#     rest2 = json.loads(rest)
#     data = dict()
#     data['date'] = base_date
#     print(rest2)
#     print(rest['items']['item'])
#     weather_data = dict()
#
#     for item in rest['items']['item']:
#         # 기온
#         if item['category'] == 'T1H':
#             weather_data['tmp'] = item['fcstValue']
#         # 습도
#         if item['category'] == 'REH':
#             weather_data['hum'] = item['fcstValue']
#         # 하늘상태: 맑음(1) 구름많은(3) 흐림(4)
#         if item['category'] == 'SKY':
#             weather_data['sky'] = item['fcstValue']
#         # 1시간 동안 강수량
#         if item['category'] == 'RN1':
#             weather_data['rain'] = item['fcstValue']
#
#     print("response: ", weather_data)
#     print(weather_data['tmp'])
#     return weather_data
# print(check_weather(60,127))
# bus=Bus_stop.objects.all()
# print(bus)
# a=Bus_stop.objects.get(id=3)
# print(a.lat)
#
# for id in range(0,len(bus)):
#     a=Bus_stop.objects.get(id=id)
#     nx, ny = mapToGrid(a.lat, a.lon)
#     data = check_weather(nx, ny)
#     WeatherDB.objects.update_or_create(bus_stop=a,
#                                        sky=data['sky'],
#                                        humidity=data['hum'],
#                                        rainType=data['rain'],
#                                        temp=data['tmp'],
#                                                  )
#
#     print("weatherDB saved")
#     print("************************")
import django
django.setup()
from JJOapp import models
a=models.Bus_stop.objects.get(ARS_ID=1002)
print(a.lat)