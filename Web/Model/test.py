import os
from pycaret.regression import load_model, predict_model

MODEL_PATH = 'C:/Users/user/Desktop/bj/Bbeojung.kr/Web/Model'
MODEL_NAME = 'lgbm_first'


model = load_model(os.path.join(MODEL_PATH, MODEL_NAME))
model