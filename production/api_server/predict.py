import lightgbm as lgb
import pandas as pd

MODEL_DIR = './models/'
MODEL_THRESHOLD = 0.3

user_model = lgb.Booster(model_file=MODEL_DIR + 'user_model')
main_model = lgb.Booster(model_file=MODEL_DIR + 'main_model')


def predict(x, model_type):
    if model_type == 'user':
        return int(user_model.predict(pd.DataFrame([x]))[0] > MODEL_THRESHOLD)
    else:
        return int(main_model.predict(pd.DataFrame([x]))[0] > MODEL_THRESHOLD)
