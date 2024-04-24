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
bar.show()'''
#Scatter plot
tips_data= px.data.tips()
print (tips_data.info())
scatterplot = px.scatter(
    data_frame=tips_data,
    x="total_bill",
    y="tip",
    opacity=0.8,                                              # set opacity of markers
    symbol="smoker",
    #marginal_x='rug',
    facet_row='sex',
    facet_col='time',
    #facet_col_wrap=2,
    #animation_frame='day', # assign marks to animation frames
	#range_x=[5,60],             # set range of x-axis
	#range_y=[0,13],             # set range of y-axis
	#category_orders={'day':['Thur','Fri','Sat','Sun']},    # set a specific ordering of values for animation data
)
#set the speed of the animation
#scatterplot.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000
#scatterplot.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500
scatterplot.show()