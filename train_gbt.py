#!/usr/bin/env python

import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split

train = pd.read_csv('./data/train.csv')
train_x = train[['feature_1', 'feature_2', 'feature_3']]
train_y = train['target']
train_x, valid_x, train_y, valid_y = \
train_test_split(train_x, train_y, test_size=0.25, random_state=1234)
train_data = lgb.Dataset(train_x, label=train_y)
valid_data = lgb.Dataset(valid_x, label=valid_y, reference=train_data)

param = {
    'num_leaves': 63,
    'num_iterations': 1000,
    'learning_rate': 0.01,
    'lambda_l2': 0.0,
    'objective': 'regression',
    'metric': 'rmse',
    'verbosity': -1}

rt = lgb.train(param,
               train_data,
               valid_sets=[train_data, valid_data],
               early_stopping_rounds=200)

rt.save_model('./model/model.txt')
