import dash_html_components as html
import dash_core_components as dcc

def Header():
    return html.Div([
        get_header(),
        get_menu()
    ])

def get_header():
    header = html.Div([
        html.Img(src='https://i.pinimg.com/564x/4a/bc/38/4abc38758eba60d6712bd86dd1542697.jpg', height='101', width='141'),
        html.H2('Your Guide To Safer Travel'),
    ], className="head")
    return header

def get_menu():
    menu = html.Div([

        dcc.Link('Overview |', href='/overview/', className="tab"),
        dcc.Link('Predict |', href='/predict/', className="tab"),
        dcc.Link('Earthquake (India) |', href='/earthquake/', className="tab"),
        dcc.Link('Health Statistics (Delhi) |', href='/health/', className="tab")
        
    ], className="menu")
    return menu
