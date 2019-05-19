from dash.dependencies import Input, Output
import plotly.graph_objs as go
import joblib
from flask import Flask, render_template, request

from plotly import tools
import datetime
import time
from app import app
import pandas as pd
import json

df_dim = pd.read_csv('data/Dimension.csv', encoding='latin-1')
model = joblib.load("RF_model.pkl")

@app.callback(Output('output', component_property='children'),
              [Input('date1', 'date'),
               Input('Time', component_property='value'),
               Input('predict-dropdown', component_property='value'),
               Input('button', 'n_clicks')])
def update_data(date, tim, state, n_clicks):
    # date = date.strftime('%Y/%m/%d')
    if n_clicks is not None:
        Lat = df_dim.loc[df_dim['State'] == state, 'Latitude'].values[0]
        Long = df_dim.loc[df_dim['State'] == state, 'Longitude'].values[0]
        ts = datetime.datetime.strptime(date+' '+tim, '%Y-%m-%d %H:%M:%S')
        ts = int(time.mktime(ts.timetuple()))
        d = {'c1': [ts], 'c2': [Lat], 'c3': [Long]}
        x = pd.DataFrame(data=d)

        # model = joblib.load("model.pkl")
        answer = 0 # model.predict(x)[0]
        return "As per the calculations of our model, there is a probability of an earthquake occurring of magnitude {} and depth {} km".format(answer[0], answer[1])

# ############################### -------  EARTHQUAKE CALLBACKS  ------- ######################################## #

df_EQ = pd.read_csv('data/Consolidated_EQ.csv', encoding='latin-1')
df_EQ['Date'] = pd.to_datetime(df_EQ['Date'], errors='coerce')

# callback for Earthquake data table changing as per data picker
@app.callback(Output('datatable-Earthquake', 'data'),
              [Input('date-picker-earthquake', 'start_date'),
               Input('date-picker-earthquake', 'end_date')])
def update_data_1(start_date, end_date):
    df2 = df_EQ[(df_EQ['Date'] > start_date) & (df_EQ['Date'] < end_date)]
    df2 = df2.to_dict("rows")
    return df2

# callback for Earthquake Graph as per data table
@app.callback(Output('EarthquakeGraph', 'figure'),
              [Input('date-picker-earthquake', 'start_date'),
               Input('date-picker-earthquake', 'end_date')])

def update_graph_1(start_date, end_date):
    df2 = df_EQ[(df_EQ['Date'] > start_date) & (df_EQ['Date'] < end_date)]
    return {
        'data': [go.Scatter(
            x=df2['Date'],
            y=df2['Magnitude'],
            mode='markers'
        )],
        'layout': {
            'height': 225,
            'margin': {'l': 20, 'b': 30, 'r': 30, 't': 10},
            'xaxis':{
                'title': 'Date'
                },
            'yaxis': {
                'title': 'Magnitude',
                'side': 'right'
            }
        }
    }


# ############################### -------  HEALTH STATISTICS CALLBACKS  ------- ######################################## #

df_health = pd.read_csv('data/Delhi Health WP data 2017.csv', encoding='latin-1')

df_health['Reported Date'] = pd.to_datetime(df_health['Reported Date'], errors='coerce')

# callback for Health data table changing as per data picker
@app.callback(Output('datatable-Health', 'data'),
              [Input('date-picker-health', 'start_date'),
               Input('date-picker-health', 'end_date')])
def update_data_2(start_date, end_date):
    df3 = df_health[(df_health['Reported Date'] > start_date) & (df_health['Reported Date'] < end_date)]
    df3 = df3.to_dict("rows")
    return df3


# callback for Health Graph as per data table
@app.callback(Output('HealthGraph', 'figure'),
              [Input('date-picker-health', 'start_date'),
               Input('date-picker-health', 'end_date')])

def update_graph_2(start_date, end_date):
    df4 = df_health[(df_health['Reported Date'] > start_date) & (df_health['Reported Date'] < end_date)]
    grp = df4.groupby('Month')['Occurrence'].sum().sort_values()
    return {
        'data': [go.Bar(
                    x=grp.index,
                    y=grp,
                    marker=dict(
                        color=['#35af8a', '#00846e', '#4d6e81', '#00d2da', '#008695', '#35af8a', '#00846e', '#4d6e81', '#00d2da', '#008695', '#35af8a', '#00846e', '#4d6e81'
                        ]),
                    )
                ],
        'layout': {
            'height': 225,
            'margin': {'l': 20, 'b': 30, 'r': 50, 't': 10},
            'xaxis':{
                'title': 'Month'
                },
            'yaxis': {
                'side': 'right'
            }
        }
    }

# callback for Health Graph as per data table
@app.callback(Output('HealthScatter', 'figure'),
              [Input('date-picker-health', 'start_date'),
               Input('date-picker-health', 'end_date')])

def update_graph_3(start_date, end_date):
    df5 = df_health[(df_health['Reported Date'] > start_date) & (df_health['Reported Date'] < end_date)]
    grp = df5.groupby('Disease')['Occurrence'].sum().sort_values()
    return {
        'data': [go.Bar(
                    y=grp.index,
                    x=grp,
                    orientation='h',
                    )
                ],
        'layout': {
            'height': 1500,
            'margin': {'l': 120, 'b': 30, 'r': 10, 't': 10},
            'xaxis':{
                'title': 'Reported Disease Count'
                }
            }
        }

# callback for Health Graph grouped by Month
@app.callback(Output('MonthGraph', 'figure'),
              [Input('health-dropdown', 'value')])

def update_graph_4(value):
    grp = df_health.groupby('Month')
    grp1 = grp.get_group(value)
    grp2 = grp1.groupby('Disease')['Occurrence'].sum().nlargest(5)
    grp2 = grp2.sort_values()
    return {
        'data': [go.Bar(
                    y=grp2.index,
                    x=grp2,
                    orientation='h',
                    marker=dict(
                        color=['#35af8a', '#00846e', '#4d6e81', '#00d2da', '#008695']),
                    )
                ],
        'layout': {
            'height': 300,
            'margin': {'l': 20, 'b': 30, 'r': 280, 't': 10},
            'xaxis': {
                'title': 'Reported Disease Count',
                },
            'yaxis': {
                # 'tickangle':315,
                'side': 'right'
            }
            }
        }

# callback for Health Graph grouped by Region
@app.callback(Output('RegionGraph', 'figure'),
              [Input('region-dropdown', 'value')])

def update_graph_5(value):
    grp = df_health.groupby('Final Zone')
    grp1 = grp.get_group(value)
    grp2 = grp1.groupby('Disease')['Occurrence'].sum().nlargest(5)
    grp2 = grp2.sort_values()
    return {
        'data': [go.Bar(
                    y=grp2.index,
                    x=grp2,
                    orientation='h',
                    marker=dict(
                        color=['#35af8a', '#4d6e81', '#008695', '#00846e', '#00d2da']),
                    )
                ],
        'layout': {
            'height': 300,
            'margin': {'l': 20, 'b': 30, 'r': 280, 't': 10},
            'xaxis': {
                'title': 'Reported Disease Count',
                },
            'yaxis': {
                # 'tickangle':315,
                'side': 'right'
            }
            }
        }

