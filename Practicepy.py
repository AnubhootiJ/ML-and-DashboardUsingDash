from flask import Flask, render_template, request
from sklearn.externals import joblib
import numpy as np
import pandas as pd
import json

import datetime
import time

df_dim = pd.read_csv('data/Dimension.csv', encoding='latin-1')

model = joblib.load("RF_model.pkl")
Lat = df_dim.loc[df_dim['State'] == 'DEL', 'Latitude'].values[0]
Long = df_dim.loc[df_dim['State'] == 'DEL', 'Longitude'].values[0]
date='2019-05-23'
tim = '09:05:36'
ts = datetime.datetime.strptime(date+' '+tim, '%Y-%m-%d %H:%M:%S')
ts = int(time.mktime(ts.timetuple()))

d = {'c1': [ts], 'c2': [Lat], 'c3': [Long]}
x = pd.DataFrame(data=d)
# model = joblib.load("model.pkl")
answer = model.predict(x)[0]
print("The earthquake of magnitude {} and depth {} km".format(answer[0], answer[1]))
