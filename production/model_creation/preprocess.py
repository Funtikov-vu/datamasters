import argparse

import pandas as pd
from sklearn import preprocessing


def normalising(df):
    columns = df.columns
    min_max_scaler = preprocessing.MinMaxScaler()
    df = min_max_scaler.fit_transform(df)
    df = pd.DataFrame(df, columns=columns)
    return df


def preprocess(fname):
    df = pd.read_csv(fname, sep=';')
    df.drop("id", axis=1, inplace=True)
    df.drop_duplicates(inplace=True)
    df["bmi"] = df["weight"] / (df["height"] / 100) ** 2
    df['diff'] = df['ap_hi'] - df['ap_lo']
    df['age'] = (df['age'] / 365).round().astype('int')
    df["gender"] = df["gender"] % 2
    out_filter = ((df["ap_hi"] > 250) | (df["ap_lo"] > 200) | (df["ap_hi"] <= 40) |
                  (df["ap_lo"] <= 40) | (df["diff"] <= 0) | (df['height'] < 120) |
                  (df['height'] >= 220) | (df["weight"] <= 30) | (df['bmi'] >= 50) |
                  (df['bmi'] <= 15))
    ord_cols = ['cholesterol', 'gluc']

    for col in ord_cols:
        dummies = pd.get_dummies(df[col])
        dummies.columns = ['{0}_{1}'.format(col, ind) for ind in dummies.columns]
        df = pd.concat([df, dummies], axis=1)
    df = df.drop(labels=['cholesterol', 'gluc'], axis=1)
    df = df[~out_filter]
    temp_name_arr = fname.split('/')
    temp_name_arr[-1] = 'clean_' + temp_name_arr[-1]
    new_name = "/".join(temp_name_arr)
    df.to_csv(new_name, index=False)


if __name__ == "__main__":
    fname = './dataset/cardio_train.csv'
    parser = argparse.ArgumentParser()

    parser.add_argument("--dataset", help="Путь до датасета")
    args = parser.parse_args()

    if args.dataset:
        fname = args.dataset
    preprocess(fname)




