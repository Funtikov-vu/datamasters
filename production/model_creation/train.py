import argparse
import json
import pandas as pd
from pandas import DataFrame
from lightgbm import LGBMClassifier


def read_json(fname):
    with open(fname) as f:
        res = json.load(f)
    return res


class HeartLGBM():
    df: DataFrame
    params: dict

    def __init__(self, df_name, model_type, params):
        self.df = pd.read_csv(df_name)
        self.params = read_json(params)
        self.columns = self.get_columns(model_type)
        self.fit_and_save()

    def get_columns(self, model_type):
        if model_type == 'user':
            return ['age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'smoke', 'alco', 'active', 'diff', 'bmi']
        else:
            return ['age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'smoke', 'alco', 'active', 'bmi',
                    'diff', 'cholesterol_1', 'cholesterol_2', 'cholesterol_3', 'gluc_1', 'gluc_2', 'gluc_3']

    def fit_and_save(self):
        x = self.df[self.columns]
        y = self.df["cardio"]
        lgb_model = LGBMClassifier(**self.params)
        lgb_model.fit(x, y)
        lgb_model.booster_.save_model('./models/' + model_type + '_model')

if __name__ == "__main__":

    fname = './dataset/clean_cardio_train.csv'
    model_type = 'user'
    params = './settings/params.json'

    parser = argparse.ArgumentParser()

    parser.add_argument("--model_type", help="Тип модели 'user', 'main'")
    parser.add_argument("--params", help="Путь до настроек модели")
    parser.add_argument("--dataset", help="Путь до датасета")

    args = parser.parse_args()

    if args.dataset:
        fname = args.dataset

    if args.params:
        params = args.params

    if args.model_type:
        model_type = args.model_type

    HeartLGBM(fname, model_type, params)
