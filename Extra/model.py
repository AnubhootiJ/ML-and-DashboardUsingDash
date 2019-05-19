import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

import datetime
import time

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier

# Read in Earthquake file
df_EQ = pd.read_csv('data/Consolidated_EQ.csv', encoding='latin-1')

timestamp = []
for d, t in zip(df_EQ['Date'], df_EQ['Time(UTC)']):
    try:
        ts = datetime.datetime.strptime(d+' '+t, '%m/%d/%Y %H:%M:%S')
        timestamp.append(int(time.mktime(ts.timetuple())))
    except ValueError:
        timestamp.append('ValueError')

timeStamp = pd.Series(timestamp)
df_EQ['Timestamp'] = timeStamp.values

df_EQ = df_EQ.drop(['Date', 'Time(UTC)'], axis=1)
df_EQ = df_EQ[df_EQ.Timestamp != 'ValueError']

X = df_EQ[['Timestamp', 'Lat', 'Lang']]
y = df_EQ[['Magnitude', 'Depth(KM)']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
X_train_2, X_validation, y_train_2, y_validation = train_test_split(X_train, y_train, test_size=0.25, random_state=1)

def create_model(neurons, activation, optimizer, loss):
    model = Sequential()
    model.add(Dense(neurons, activation=activation, input_shape=(3,)))
    model.add(Dense(neurons, activation=activation))
    model.add(Dense(2, activation='softmax'))

    model.compile(optimizer=optimizer, loss=loss, metrics=['accuracy'])

    return model

model = KerasClassifier(build_fn=create_model, verbose=0)

neurons = [16]
batch_size = [10]
epochs = [10]
activation = ['sigmoid', 'relu']
optimizer = ['SGD', 'Adadelta']
loss = ['squared_hinge']

param_grid = dict(neurons=neurons, batch_size=batch_size, epochs=epochs, activation=activation, optimizer=optimizer, loss=loss)

grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1)
grid_result = grid.fit(X_train_2, y_train_2)


means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']

model = Sequential()
model.add(Dense(16, activation='relu', input_shape=(3,)))
model.add(Dense(16, activation='relu'))
model.add(Dense(2, activation='softmax'))

model.compile(optimizer='SGD', loss='squared_hinge', metrics=['accuracy'])

model.fit(X_train_2, y_train_2, batch_size=10, epochs=20, verbose=1, validation_data=(X_validation, y_validation))

[test_loss, test_acc] = model.evaluate(X_test, y_test)
# print("Evaluation result on Test Data : Loss = {}, accuracy = {}".format(test_loss, test_acc))


from sklearn.externals import joblib
joblib.dump(model, 'model.pkl')
