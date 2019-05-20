import dash_core_components as dcc
import dash_html_components as html
import dash_table
from header import Header
from app import app
from datetime import datetime as dt
import pandas as pd


# ############################### -------  INTRODUCTION LAYOUT  ------- ######################################## #

layout_Intro = html.Div([

    html.Div([
        Header(),   # the common header to all pages

        html.Div([

            html.Br(),
            html.P("Staying healthy is a basic requirement for any living being. We take several precautions to "
                   "maintain a healthy lifestyle. This can be endangered while travelling to a new place for school, "
                   "work, or just for some fun holiday trip; especially if there is no reliable information "
                   "available to take the necessary precautions. The motivation for this particular project comes "
                   "from our personal experience of having to search thousands of websites to get a decent idea"
                   "of how safe a region is to visit in medical terms. If we know that dengue is a common disease in "
                   "the rainy season in Delhi, anyone travelling to the region can take relevant precautions by"
                   "getting properly vaccinated. "),
        ], className="Intro1"),

        html.Div([          # Giving a title
          html.H4(["About the Project"], className="Title", style={'marginTop': 15,
                                                                   'background': '#35af8a'})
          ]),

        html.Div([

            html.Br(),
            html.P("The project is a multi-page dashboard application with interactive graphs and elements for great"
                   "user-friendly experience. The project is based on two main tools - "),
            dcc.Markdown('''
                1. Dash by plotly - to create the dashboard, frontend development
                2. Python - for the backend development and models
                
                The project is divided into four tabs - 
                1. Overview - basic introduction for the project
                2. Predict - predicting earthquake at a given time, date, and place
                3. Earthquake - statistics related to earthquake in India
                4. Health - statistics related to Health in Delhi
                
                #### PREDICT TAB
                The predictive model is not yet deployed. Though, the tab basically gives the prediction of the 
                magnitude and depth by which an earthquake can occur given a date, time and region inputted by the user.
                
            '''
            )
        ], className="Intro1"),

        html.Div([          # Giving a title
            html.H4(["Different statistical elements in the Earthquake tab"], className="Title",
                    style={'marginTop': 15, 'background': '#008695'})
            ]),

        html.Div([

            html.Br(),
            dcc.Markdown('''
                #### FIRST ELEMENT - DATE PICKER AND TABLE
                
                Our first element in the Earthquake tab is the data table and date picker associated to it. As per the
                date picker, you can select the date range for which to view the data. 
                
                #### SECOND ELEMENT - GRAPH BASED ON YEAR
                
                The second element is a statistical graph giving a scatter of data points by magnitude each year. It 
                will change with the date picker. You can also click on a specific portion to focus on a particular 
                year, month, or date.  
                
                #### THIRD ELEMENT - WORLD MAP
                
                The third element is our data set plotted on a world map. You can see that most of our data is
                based on earthquake that occurred in India and neighboring countries. 
                
                #### FOURTH ELEMENT - CHOROPLETH AND BUBBLE GRAPHS FOR INDIA
                
                The fourth element consists of two graphs - one a choropleth graph and other the bubble graph both
                depicting the impact of earthquake in different regions of India. 

            '''
                         )
        ], className="Intro2"),

        html.Div([          # Giving a title
            html.H4(["Different statistical elements in the Health tab"], className="Title",
                    style={'marginTop': 15, 'background': '#00d2da'})
            ]),

        html.Div([

            html.Br(),
            dcc.Markdown('''
                #### FIRST ELEMENT - DATE PICKER AND TABLE

                Our first element in the Health tab is the data table and date picker associated to it. As per the
                date picker, you can select the date range for which to view the data. 

                #### SECOND ELEMENT - GRAPH BY OCCURRENCE

                The second element is a statistical graph giving a bar plot by occurrence every month in the year of 
                2016. To view a particular month or months, you can focus by clicking on that specific region.   

                #### THIRD ELEMENT - GRAPH BY DISEASE

                The third element is a statistical graph giving a bar plot by disease in the year of 2016. To view a 
                particular disease or diseases, you can focus by clicking on that specific region. 

                #### FOURTH ELEMENT - TOP 5 DISEASES BY MONTH

                The fourth element is a bar graph showing top 5 diseases every month. You can pick the month you want
                to view the top 5 diseases of from the dropdown just above the graph. 
                
                #### FIFTH ELEMENT - TOP 5 DISEASES BY REGION

                The fourth element is a bar graph showing top 5 diseases in every region. You can pick the region you 
                want to view the top 5 diseases of from the dropdown just above the graph. 

            '''
                         )
        ], className="Intro3"),

        html.Div([          # Giving a title
            html.H4(["About the Team"], className="Title", style={'marginTop': 15,
                                                                  'background': '#4d6e81'})
            ]),

        html.Div([

            html.Br(),

            dcc.Markdown('''
                The project was developed as a major project by team of 3 B.tech CSE students in 2019 -
                
                ANUBHOOTI JAIN 
                
                PRAKHARI JAIN
                
                SAHIL DHAWAN

            '''
                         )
        ], className="Intro4"),

        html.Div(className="Title", style={'marginTop': 15, 'background': '#00846e'}),

    ], className='subpage', style={'border': '5px #00846e solid'})

], className='page')


# ################################# -------  MODEL LAYOUT  ------- ######################################## #

layout_predict = html.Div([

    html.Div([

        Header(),

        html.Div([

            html.Div([
                html.H4(["Traveling? Predict possibility of tremors in the area!"], className="Title", style={'marginTop': 15, 'background': '#00846e'}),
            ]),

            html.Div([

                html.Div([
                    html.Label(["Pick Date:"]),
                    dcc.DatePickerSingle(id='date1',
                                         min_date_allowed=dt(2010, 8, 5),
                                         max_date_allowed=dt(2030, 9, 19),
                                         initial_visible_month=dt(2017, 8, 5),
                                         date=dt(2017, 8, 5),
                                         ),
                    ]),

                html.Div([
                    html.Label(["Give Time:  "]),
                    dcc.Input(id='Time', placeholder='HH:MM:SS',)
                ]),

                html.Div([
                    html.Label(["Choose State:"]),
                    dcc.Dropdown(
                        id='predict-dropdown',
                        options=[
                            {'label': 'Tripura', 'value': 'TRI'},
                            {'label': 'Uttar Pradesh', 'value': 'UP'},
                            {'label': 'Gujarat', 'value': 'GUJ'},
                            {'label': 'Punjab', 'value': 'PUN'},
                            {'label': 'Karnataka', 'value': 'KAR'},
                            {'label': 'Chandigarh', 'value': 'CHAN'},
                            {'label': 'Tamil Nadu', 'value': 'TN'},
                            {'label': 'Assam', 'value': 'ASS'},
                            {'label': 'Sikkim', 'value': 'SIK'},
                            {'label': 'Andhra Pradesh', 'value': 'AP'},
                            {'label': 'Rajasthan', 'value': 'RAJ'},
                            {'label': 'Kerala', 'value': 'KER'},
                            {'label': 'West Bengal', 'value': 'WB'},
                            {'label': 'Maharashtra', 'value': 'MAH'},
                            {'label': 'Delhi', 'value': 'DEL'},
                            {'label': 'Bihar', 'value': 'BIH'},
                            {'label': 'Andaman and Nicobar Islands', 'value': 'AND'},
                            {'label': 'Meghalaya', 'value': 'MEG'},
                            {'label': 'Himachal Pradesh', 'value': 'HP'},
                            {'label': 'Jammu and Kashmir', 'value': 'JK'},
                        ],
                        placeholder='Choose State',
                        style={
                            'width': '50%'}
                    ),
                ]),

                html.Div([
                    html.Button('PREDICT', id='button', style={}),
                ]),

                html.Div(id='output'),

            ], className='box', style={'width': '70%'}),

        ], className='up-box'),

        html.Div(className="Title", style={'marginTop': 15, 'background': '#00846e'}),

    ], className='subpage', style={'border': '5px #4d6e81 solid'})

], className='page')

# ############################### -------  EARTHQUAKE LAYOUT  ------- ######################################## #

# Read in Earthquake file
df_EQ = pd.read_csv('data/Consolidated_EQ.csv', encoding='latin-1')

# Converting date column from series to datetime, coerce sets error values to NaN
df_EQ['Date'] = pd.to_datetime(df_EQ['Date'], errors='coerce')

# Creating layout -> will be imported to index.py as one of the pages
layout_Earthquake = html.Div([

    html.Div([
        Header(),   # the common header to all pages

        html.Div([

            html.Br(),
            html.P("Natural disasters can be a dangerous ordeal, which is why it is always smart to be prepared fully. Here are some statistics for you to be prepared for your next trip!"),
            html.P("Just pick a date range, it will show the data for that particular period of time only for easy navigation."),
            html.Label("Select Date range:"),

            dcc.DatePickerRange(            # Creating a Date Picker
              id='date-picker-earthquake',
              min_date_allowed=df_EQ['Date'].min(),
              max_date_allowed=df_EQ['Date'].max(),
              start_date=df_EQ['Date'].min(),
              end_date=df_EQ['Date'].max(),
            )
        ], className="date-picker"),

        html.Div([          # Giving a title
          html.H4(["Earthquake Statistics in India"], className="Title", style={'marginTop': 15, 'background': '#00846e'})
          ]),

        html.Div([
        dash_table.DataTable(           # Creating the data table for Earthquake
            id='datatable-Earthquake',
            columns=[{"name": i, "id": i} for i in df_EQ.columns],
            n_fixed_rows=1,
            data=df_EQ.to_dict("rows"),
            filtering=True,
            sorting=True,
            sorting_type="multi",
            style_table={'overflowX': 'scroll',
                         'maxHeight': '300',
                         'overflowY': 'scroll'
                         },
            style_cell={'textAlign': 'left'},
            style_cell_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)'
                }
            ]
        )
    ], className="main-table"),

        html.Div([          # Giving a title for Graph 1
          html.H4(["Statistics Graph by Magnitude and Date"], className="Title", style={'marginTop': 15, 'background': '#4d6e81'})
          ], className="GraphTitle"),

        html.Div([          # Div for Earthquake Graph - Magnitude as per date picker
        dcc.Graph(id='EarthquakeGraph')
        ], className='row'),

        html.Div([          # Giving a title for Graph 2
          html.H4(["Affected Areas by Longitude and Latitude"], className="Title", style={'marginTop': 15, 'background': '#00d2da'})
          ], className="GraphTitle"),

        html.Div([          # Div for Earthquake Graph - Scatter as per date picker
            html.Img(src=app.get_asset_url('Map_EQ_1.png'), id='Map-LL-EQ')
        ], className='row'),

        html.Div([          # Giving a title for Graph 1
          html.H4(["Map Depicting Earthquake Impact (Choropleth Graph)"], className="Title", style={'marginTop': 15, 'background': '#008695'})
          ], className="MapTitle"),

        html.Div([  # Choropleth Map by Region Count
            html.Img(src=app.get_asset_url('India_EQ.png'), id='Map1EQ')
        ], className='row'),

        html.Div([          # Giving a title for Graph 1
          html.H4(["Map Depicting Earthquake Impact (Bubble Graph)"], className="Title", style={'marginTop': 15, 'background': '#35af8a'})
          ], className="MapTitle"),

        html.Div([  # Bubble Map by Region Count
            html.Img(src=app.get_asset_url('India_EQ_2.png'), id='Map2EQ')
        ], className='row'),

        html.Div(className="Title", style={'marginTop': 15, 'background': '#00846e'}),

    ], className='subpage', style={'border': '5px #00846e solid'})

], className='page')

# ############################### -------  HEALTH STATISTICS LAYOUT  ------- ######################################## #

# Read in Health data
df_health = pd.read_csv('data/Delhi Health WP data 2017.csv', encoding='latin-1')

# Converting date column from series to datetime, coerce sets error values to NaN
df_health['Reported Date'] = pd.to_datetime(df_health['Reported Date'], errors='coerce')

# Creating the second layout -> will be imported to index.py as second page

layout_Health = html.Div([

    html.Div([
        Header(),   # the common header to all pages

        html.Div([

            html.Br(),
            html.P("Health is a major issue especially when travelling to a new place. Here are some statistics that will give you an insight into the NCR region, the capital of India"),
            html.P("Just pick a date range, it will show the data for that particular period of time only for easy navigation."),
            html.Label("Select Date range:"),

            dcc.DatePickerRange(            # Creating a Date Picker
              id='date-picker-health',
              min_date_allowed=df_health['Reported Date'].min(),
              max_date_allowed=df_health['Reported Date'].max(),
              start_date=df_health['Reported Date'].min(),
              end_date=df_health['Reported Date'].max()
            )
        ], className="date-picker"),

        html.Div([          # Giving a title
          html.H4(["Health Statistics in Delhi"], className="Title", style={'marginTop': 15, 'background': '#00846e'})
          ]),

        html.Div([
        dash_table.DataTable(           # Creating the data table for Health
            id='datatable-Health',
            columns=[{"name": i, "id": i} for i in df_health.columns],
            n_fixed_rows=1,
            data=df_health.to_dict("rows"),
            filtering=True,
            sorting=True,
            sorting_type="multi",
            style_table={'overflowX': 'scroll',
                         'maxHeight': '300',
                         'overflowY': 'scroll'
                         },
            style_cell={'textAlign': 'left'},
            style_cell_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)'
                }
            ]
        )
    ], className="main-table"),

        html.Div([          # Giving a title for Graph 1
          html.H4(["Bar Graph by Occurrence"], className="Title", style={'marginTop': 15, 'background': '#4d6e81'})
          ], className="GraphTitle"),

        html.Div([          # Div for Health Graph
        dcc.Graph(id='HealthGraph')
        ], className='row'),

        html.Div([          # Giving a title for Graph 2
          html.H4(["Bar Graph for Reported Diseases in a Year "], className="Title", style={'marginTop': 15, 'background': '#00d2da'})
          ], className="GraphTitle"),

        html.Div([          # Div for Health Graph
        dcc.Graph(id='HealthScatter')
        ], className='row'),

        html.Div([          # Giving title for dropdown graph
          html.H4(["Diseases Prevalent by month"], className="Title", style={'marginTop': 15, 'background': '#008695'})
          ], className="GraphTitle"),

        html.Div([          # Giving title for dropdown graph
            dcc.Dropdown(
                id='health-dropdown',
                options=[
                    {'label': 'January', 'value': 'January'},
                    {'label': 'February', 'value': 'February'},
                    {'label': 'March', 'value': 'March'},
                    {'label': 'April', 'value': 'April'},
                    {'label': 'May', 'value': 'May'},
                    {'label': 'June', 'value': 'June'},
                    {'label': 'July', 'value': 'July'},
                    {'label': 'August', 'value': 'August'},
                    {'label': 'September', 'value': 'September'},
                    {'label': 'October', 'value': 'October'},
                    {'label': 'November', 'value': 'November'},
                    {'label': 'December', 'value': 'December'},
                ],
                value='January'
            ),

          ], className="row"),

        html.Div([          # Div for Health Graph by Particular Month
        dcc.Graph(id='MonthGraph')
        ], className='row'),

        html.Div([          # Giving title for dropdown graph
          html.H4(["Diseases Prevalent by Region"], className="Title", style={'marginTop': 15, 'background': '#35af8a'})
          ], className="GraphTitle"),

        html.Div([          # Giving title for dropdown graph by Region
            dcc.Dropdown(
                id='region-dropdown',
                options=[
                    {'label': 'Central', 'value': 'Central'},
                    {'label': 'City', 'value': 'City'},
                    {'label': 'Civil Line', 'value': 'Civil Line'},
                    {'label': 'Karol Bagh', 'value': 'Karol Bagh'},
                    {'label': 'Najafgarh', 'value': 'Najafgarh'},
                    {'label': 'Narela', 'value': 'Narela'},
                    {'label': 'New Delhi Municipal Council', 'value': 'New Delhi Municipal Council'},
                    {'label': 'Rohini', 'value': 'Rohini'},
                    {'label': 'Sadar Paharganj', 'value': 'Sadar Paharganj'},
                    {'label': 'Shahdara North', 'value': 'Shahdara North'},
                    {'label': 'Shahdara South', 'value': 'Shahdara South'},
                    {'label': 'South', 'value': 'South'},
                    {'label': 'West', 'value': 'West'},
                ],
                value='Central'
            ),

          ], className="row"),

        html.Div([          # Div for Health Graph by Particular Month
        dcc.Graph(id='RegionGraph')
        ], className='row'),

        html.Div(className="Title", style={'marginTop': 15, 'background': '#00846e'}),

    ], className='subpage', style={'border': '5px #00d2da solid'})

], className='page')

# ############################### -------  NO PAGE LAYOUT  ------- ######################################## #

noPage = html.Div([

    html.Div(className="Title", style={'marginTop': 15, 'background': '#00846e'}),

    html.H1("ERROR 404 PAGE NOT FOUND"),

    html.Div(className="Title", style={'marginTop': 15, 'background': '#00846e'}),
])
