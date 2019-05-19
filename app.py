import dash

external_stylesheets = ['//fonts.googleapis.com/css?family=Raleway:400,300,600']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.config.suppress_callback_exceptions = True
