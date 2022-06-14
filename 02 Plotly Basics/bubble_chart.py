#!/usr/bin/env python3
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Data/mpg.csv')

data = [go.Scatter(
                    x= df.horsepower,
                    y= df.mpg,
                    text= df.name,
                    mode= 'markers',
                    marker= dict(size= 2*df.cylinders)
                )]

layout = go.Layout(title= 'Bubble chart')
fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename= 'Bubble_Chart_01')

data = [go.Scatter(
                    x= df.horsepower,
                    y= df.mpg,
                    text= df.name,
                    mode= 'markers',
                    marker= dict(size= df.weight/200)
                )]

layout = go.Layout(title= 'Bubble chart')
fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename= 'Bubble_Chart_02')

data = [go.Scatter(
                    x= df.horsepower,
                    y= df.mpg,
                    text= df.name,
                    mode= 'markers',
                    marker= dict(size= df.weight/100, color= df.cylinders, showscale= True)
                )]

layout = go.Layout(title= 'Bubble chart')
fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename= 'Bubble_Chart_03')