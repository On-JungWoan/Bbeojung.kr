import os
import joblib

MODEL_PATH = 'C:/Users/user/Desktop/bj/Bbeojung.kr/Web/Model'
MODEL_NAME = 'lgbm_second.pkl'


model = joblib.load(os.path.join(MODEL_PATH, MODEL_NAME))
model