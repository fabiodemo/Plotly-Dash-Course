import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Data/2018WinterOlympics.csv')

data = [go.Bar(
                x=df.NOC,
                y= df.Total)]

## Nested Bar Chart            
layout = go.Layout(title= 'Medals')
fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename= 'Bar_Medals_01')

trace_gold = go.Bar(x= df.NOC, 
                y= df.Gold, 
                name= 'Gold', 
                marker= {'color': '#FFD700'})

trace_silver = go.Bar(x= df.NOC, 
                y= df.Silver, 
                name= 'Silver', 
                marker= {'color': '#9EA0A1'})

trace_bronze = go.Bar(x= df.NOC, 
                y= df.Bronze, 
                name= 'Bronze', 
                marker= {'color': '#CD7F32'})

data = [trace_gold, trace_silver, trace_bronze]
layout = go.Layout(title= 'Medals')
fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename= 'Bar_Medals_02')


# Stacked bar Chart
trace_gold = go.Bar(x= df.NOC, 
                y= df.Gold, 
                name= 'Gold', 
                marker= {'color': '#FFD700'})

trace_silver = go.Bar(x= df.NOC, 
                y= df.Silver, 
                name= 'Silver', 
                marker= {'color': '#9EA0A1'})

trace_bronze = go.Bar(x= df.NOC, 
                y= df.Bronze, 
                name= 'Bronze', 
                marker= {'color': '#CD7F32'})

data = [trace_gold, trace_silver, trace_bronze]
layout = go.Layout(title= 'Medals', barmode= 'stack')
fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename= 'Bar_Medals_03')
