import numpy as np
import pandas as pd
import datetime
import time

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor

df_EQ = pd.read_csv('data/EQ.csv', encoding='latin-1')

timestamp = []
for d, t in zip(df_EQ['Date'], df_EQ['Time']):
    try:
        ts = datetime.datetime.strptime(d+' '+t, '%m/%d/%Y %H:%M:%S')
        timestamp.append(int(time.mktime(ts.timetuple())))
    except OverflowError:
        timestamp.append('Off')

timeStamp = pd.Series(timestamp)
df_EQ['Timestamp'] = timeStamp.values


df_EQ = df_EQ.drop(['Date', 'Time'], axis=1)
df_EQ = df_EQ[df_EQ.Timestamp != 'Off']

X = df_EQ[['Timestamp', 'Latitude', 'Longitude']]
y = df_EQ[['Magnitude', 'Depth']]

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=0)

# ################## RANDOM FOREST REGRESSION ################# #

reg2 = RandomForestRegressor(random_state=0, n_estimators=500)
reg2.fit(train_X, train_y)
# y_forest = reg2.predict(test_X)
print(reg2.score(test_X, test_y))

from sklearn.externals import joblib
joblib.dump(reg2, 'RF_model.pkl', compress=9)


