#import packages
import dash
#for Dash HTML component
from dash import html
#for Dash core components
from dash import dcc
from dash import Input, Output
#for bootstrap
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

#to use bootstrap stylesheet
external_stylesheets =[dbc.themes.SUPERHERO]
#Bar graph
#read the data
df=pd.read_csv('data/Caste.csv')
#take data related to Maharashtra
maharastra_data=df[df.state_name=='Maharashtra']
maharastra_stat=maharastra_data.groupby(['year','gender'])[['convicts','under_trial','detenues','others']].agg('sum').reset_index()
#Create the bar plot
bar=px.bar(data_frame=maharastra_data,x='gender',y='convicts',\
           color='gender',\
           opacity=0.9,
           title='Maharastra Prison Statistics',
           orientation='v',              # 'v','h': orientation of the marks
           barmode='group',
           text='convicts',            # values appear in figure as text labels
           hover_name='under_trial',   # values appear in bold in the hover tooltip
           animation_frame='year',
           range_y=[0,9000]
           )
# controls the speed of x axis
bar.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000
# controls the speed of y axis
bar.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500

#Scatter plot
tips_data= px.data.tips()
#Draw scatterplot
scatterplot = px.scatter(
    data_frame=tips_data,
    x="total_bill",
    y="tip",
    opacity=0.8,                                              # set opacity of markers
    symbol="smoker",
    facet_row='sex',
    facet_col='time',
    facet_col_wrap=2,
    title='Tips Analysis'
)

#Draw racing bar
#load suicide data
suicide_data= pd.read_csv('data/suicide-rate-1990-2017.csv')

#print (suicide_data.describe())
#get the data for Europe
eu_data=suicide_data[suicide_data['region']=='Europe']
#find the avg(mean) suicide rates for each county
eu_stat_df=eu_data.groupby('country')['suicide rate (deaths per 100,000)'].agg(['mean']).sort_values('mean',ascending=False).reset_index()
#get the mean suicide rate of eu
mean_sr=eu_stat_df['mean'].mean()
#get countries with suicide rate more than or equal to mean suicide rate
top_eu_stat=eu_stat_df[eu_stat_df['mean'] >= mean_sr]
#select the countries who has suicide rate more that the mean suicide rate
top_eu_data = eu_data[eu_data['country'].isin(top_eu_stat['country'].values.tolist())]
#plot the bar chart
suicide_bar=px.bar(data_frame=top_eu_data,y='country',x='suicide rate (deaths per 100,000)',\
           barmode='group',
           orientation='h',
		   title='Suicide rate in Europe', # figure title
           width=1000,                   # figure width in pixels
           height=650,                   # figure height in pixels
           animation_frame='year',
		   range_x=[0,100],
           category_orders={'year': [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001,\
                                     2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,\
                                     2015, 2016, 2017]})
#controls animation speed
suicide_bar.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000
suicide_bar.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500
#Graph for bees
#load data
bees_data= pd.read_csv('data/bees.csv')
print(bees_data.info())

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])

# bootstrap
app.layout=dbc.Container([
            dbc.Row(
                dbc.Col(html.H4("Indian Prison Analysis",className='text-center mb-10'),
                xs=12, sm=12, md=12, lg=12, xl=12),align="center"
            ),#Row 1 ends
            dbc.Row(
                dbc.Col(dcc.Graph(id='maharastra_bar',figure=bar),className="col-md-6 offset-md-3")
                ,align="center"
            ),#row 2 ends
            dbc.Row(
                dbc.Col(html.H4("Tips Analysis",className='text-center mb-10'),
                xs=12, sm=12, md=12, lg=12, xl=12),align="center"
            ),#Row 3 ends
            dbc.Row(
                dbc.Col(dcc.Graph(id='tips_scatter',figure=scatterplot),className="col-md-8 offset-md-2")
                ,align="center"
            ),#row 4 ends
            dbc.Row(
                dbc.Col(html.H4("Suicide Rate Analysis In Europe",className='text-center mb-10'),
                xs=12, sm=12, md=12, lg=12, xl=12),align="center"
            ),#Row 5 ends
            dbc.Row(
                dbc.Col(dcc.Graph(id='EU_RB',figure=suicide_bar),className="col-md-8 offset-md-1"),align="center"
            ),#row 6 ends
            dbc.Row(
                dbc.Col(html.H4("Bees Analysis In USA",className='text-center mb-10'),
                xs=12, sm=12, md=12, lg=12, xl=12),align="center"
            ),#Row 7 ends
			dbc.Row([
                dbc.Col([
                    html.Label("Select Year:",style={'display':'flex','textAlign':'center'},className='text-center mb-12'),
                    #html.Header("Select Year:",style={'textAlign':'center'}),
                    #Drop down
                    dcc.Dropdown(id="year_selected",
                        options=[
                            {"label": "2015", "value": 2015},
                            {"label": "2016", "value": 2016},
                            {"label": "2017", "value": 2017},
                            {"label": "2018", "value": 2018}],
                        multi=False,
                        value=2015,
                        style={'width': "40%",
                               'justify-content': 'center'
                               }
                    ),
                    html.Br(),
                    html.Div(id='output_container', children=[]),
                    dcc.Graph(id='bees_graph')
                ],
                align="center",xs=12, sm=12, md=12, lg=12, xl=12)#column for row 8 ends

            ],align="center")#row 8 ends
], fluid=True)#app.layout ends
#
# App layout
# app.layout = html.Div([
#     #row 1 for Maharastra bar graph
#     html.Div([
#         html.Div([
#         ],className='col-md-2'),#row 1 col 1 ends
#         html.Div([
#             #card
#             html.Div([
#                 #card-body
# 			    html.Div([
#                     dcc.Graph(id='maharastra_bar',figure=bar)
# 				],className='card-body')#card-body ends
# 		    ],className='card')
#         ],className='col-md-8'),#row 1 col 2 ends
#         html.Div([
#         ],className='col-md-2')#row 1 col 3 ends
#     ],className='row'),#row 1 (Maharastra bar graph)ends
#     # row 2 for tips scatter plot
#     html.Div([
#         html.Div([
#             #card
#             html.Div([
#                 #card-body
# 		        html.Div([
#                     dcc.Graph(id='tips_scatter',figure=scatterplot)
# 			    ],className='card-body')#card-body ends
# 		    ],className='card')#card ends
#         ],className='col-md-12')
#     ], className='row'),# row 2 (tips scatter plot)ends
#     # row 3 for EU racing bar plot
#     html.Div([
#         html.Div([
#             #card
#             html.Div([
#                 #card-body
# 		        html.Div([
#                     dcc.Graph(id='EU_RB',figure=suicide_bar)
# 			    ],className='card-body')#card-body ends
# 		    ],className='card')#card ends
#         ],className='col-md-12')
#     ], className='row'),# row 3 (EU racing bar plot)ends
#     # row 4 for bees plot
#     html.Div([
#         html.Div([
#             html.Label(['Select Year:']),
#             #Drop down
#             dcc.Dropdown(id="year_selected",
#                  options=[
#                      {"label": "2015", "value": 2015},
#                      {"label": "2016", "value": 2016},
#                      {"label": "2017", "value": 2017},
#                      {"label": "2018", "value": 2018}],
#                  multi=False,
#                  value=2015,
#                  style={'width': "40%"}
#             ),
#             html.Br(),
#             html.Div(id='output_container', children=[]),
#             dcc.Graph(id='bees_graph')
#         ],className='col-md-12')
#     ], className='row'),# row 4 (bess graph)ends
# ],className='container')

# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
#call back functions
@app.callback([Output(component_id='output_container',component_property='children'),
                     Output(component_id='bees_graph',component_property='figure')],
	                Input(component_id='year_selected',component_property='value'))
def draw_bees(year):
    #make msg for the container
    container = "The year chosen by user is: {}".format(year)
    #make local copy of dataframe
    df=bees_data.copy()
    #filter tha data for selected year
    df=df[df['Year']== year]
    #filder data for only one virus
    df = df[df["Affected by"] == "Varroa_mites"]
    # draw plotly express figure
    fig = px.choropleth(
        data_frame=df,
        locationmode='USA-states',
        locations='state_code',
        scope="usa",
        color='Pct of Colonies Impacted',
        hover_data=['State', 'Pct of Colonies Impacted'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark'
    )
    return container,fig

if __name__ == '__main__':
    app.run_server(debug=True)