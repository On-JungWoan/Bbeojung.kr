import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from secret import *
from lightgbm import LGBMRegressor
import joblib
import numpy as np

import requests
import re

def str_preprocessing(keyword, contents):
    text_data = ''.join(re.findall(r'<{}>.*</{}>'.format(keyword, keyword), contents))
    if text_data == '':
        return None
    return text_data.replace(f'{keyword}>', '').replace('<', '').split('/')[:-1]

def calc_remain(bus_id):
    url = f'http://api.gwangju.go.kr/xml/arriveInfo?serviceKey={BIS_ARRIVE_KEY}&BUSSTOP_ID={bus_id}'

    response = requests.get(url)
    contents = response.text

    LINE_NAME = str_preprocessing('LINE_NAME', contents)
    REMAIN_MIN = str_preprocessing('REMAIN_MIN', contents)
    REMAIN_STOP = str_preprocessing('REMAIN_STOP', contents)

    return LINE_NAME, REMAIN_MIN, REMAIN_STOP



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