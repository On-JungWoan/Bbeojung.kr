from lightgbm import LGBMRegressor
import joblib
import numpy as np

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