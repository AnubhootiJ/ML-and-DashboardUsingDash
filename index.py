import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from layouts import layout_Intro, layout_predict, layout_Earthquake, layout_Health, noPage
from app import app
from app import server
import callbacks

import pandas as pd
import io

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/earthquake/':
        return layout_Earthquake
    elif pathname == '/predict/':
        return layout_predict
    elif pathname == '/health/':
        return layout_Health
    elif pathname == '/overview/' or '/':
        return layout_Intro
    else:
        return noPage

if __name__ == '__main__':
    app.run_server(debug=True)
