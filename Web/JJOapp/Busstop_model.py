# import requests, bs4
# import pandas as pd
# from lxml import html
# from urllib.request import Request, urlopen
# from urllib.parse import urlencode, quote_plus, unquote
# import os
# import django
# import pandas as pd
# import pyodbc
#
#
# # 1. URL 파라미터 분리하기.
# # Service URL
# xmlUrl = 'http://api.gwangju.go.kr/xml/stationInfo'
#
# My_API_Key = unquote('IkwYEWiPWior39UF5%2BeuNa8RFPbJwwib3HDmhR3FKgXKMDX%2F%2FEiXqpmWKPd4oW%2FN2EtbIxWTl2EvPWdI%2Fxgqfg%3D%3D')+xmlUrl     # 사용자 인증키
# queryParams = '?' + urlencode({quote_plus('ServiceKey') : My_API_Key})
#
# response = requests.get(xmlUrl + queryParams).text.encode('utf-8')
# xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')
# # xmlobj    # 디버깅용.
#
# rows = xmlobj.findAll("STATION")
# rows
# rowList = []
# nameList = []
# columnList = []
#
# rowsLen = len(rows)
# for i in range(0, rowsLen):
#     columns = rows[i].find_all()
#
#     columnsLen = len(columns)
#     for j in range(0, columnsLen):
#         # 첫 번째 행 데이터 값 수집 시에만 컬럼 값을 저장한다. (어차피 rows[0], rows[1], ... 모두 컬럼헤더는 동일한 값을 가지기 때문에 매번 반복할 필요가 없다.)
#         if i == 0:
#             nameList.append(columns[j].name)
#         # 컬럼값은 모든 행의 값을 저장해야한다.
#         eachColumn = columns[j].text
#         columnList.append(eachColumn)
#     rowList.append(columnList)
#     columnList = []  # 다음 row의 값을 넣기 위해 비워준다. (매우 중요!!)
#
# result = pd.DataFrame(rowList, columns=nameList)
# result