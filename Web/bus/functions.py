import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

# from Private.secret import *
from lightgbm import LGBMRegressor
import joblib
import numpy as np

import requests
import json

# # url 입력
# BUS_ID = 2873
# url = f'http://api.gwangju.go.kr/xml/arriveInfo?serviceKey={BIS_ARRIVE_KEY}&BUSSTOP_ID={BUS_ID}'

# # url 불러오기
# response = requests.get(url)

# #데이터 값 출력해보기
# contents = response.text
# json_ob = json.loads(contents)


MODEL_PATH = './Model/lgbm_4th.pkl'
model = joblib.load(MODEL_PATH)

def make_infer():
    time_list = [0, 1, 2]
    pred_list = []

    for t in time_list:
        tmp_pred = int( model.predict(np.array([1,t]).reshape(1,-1))[0] )
        pred_list.append(tmp_pred)

        del tmp_pred
    return pred_list