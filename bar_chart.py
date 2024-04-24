import pandas as pd
import plotly_express as px
'''#Bar graph
#read the data
df=pd.read_csv('data/Caste.csv')
#take data related to Maharashtra
maharastra_data=df[df.state_name=='Maharashtra']
maharastra_stat=maharastra_data.groupby(['year','gender'])[['convicts','under_trial','detenues','others']].agg('sum').reset_index()
print (maharastra_stat.shape)
bar=px.bar(data_frame=maharastra_data,x='gender',y='convicts',\
           color='gender',\
           opacity=0.9,
           #facet_col='caste',
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
bar.show()
#Scatter plot
tips_data= px.data.tips()
print (tips_data.info())
scatterplot = px.scatter(
    data_frame=tips_data,
    x="total_bill",
    y="tip",
    opacity=0.8,                                              # set opacity of markers
    symbol="smoker",
    facet_row='sex',
    facet_col='time',
    facet_col_wrap=2,
)
scatterplot.show()'''
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
print (f"mean suicide rate of EU:{mean_sr}")
#get countries with suicide rate more than or equal to mean suicide rate
top_eu_stat=eu_stat_df[eu_stat_df['mean'] >= mean_sr]
#select the countries who has suicide rate more that the mean suicide rate
top_eu_data = eu_data[eu_data['country'].isin(top_eu_stat['country'].values.tolist())]
#plot the bar chart
suicide_bar=px.bar(data_frame=top_eu_data,y='country',x='suicide rate (deaths per 100,000)',\
           barmode='group',
           orientation='h',
		   title='suicide rate (deaths per 100,000) in Europe', # figure title
           width=1200,                   # figure width in pixels
           height=650,                   # figure height in pixels
           animation_frame='year',
		   range_x=[0,100],
           category_orders={'year': [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001,\
                                     2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,\
                                     2015, 2016, 2017]})
#controls animation speed
suicide_bar.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000
suicide_bar.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500
suicide_bar.show()