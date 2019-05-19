import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from layouts import layout_predict, layout_Earthquake, layout_Health, noPage
from app import app
from app import server
import joblib
import callbacks

import pandas as pd
import io
from flask import send_file

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/overview/':
        return layout_predict
    elif pathname == '/earthquake/':
        return layout_Earthquake
    elif pathname == '/health/' or '/':
        return layout_Health
    else:
        return noPage

if __name__ == '__main__':
    app.run_server(debug=True)
