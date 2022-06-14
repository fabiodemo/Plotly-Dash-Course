#!/usr/bin/env python3
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(56)
x_values = np.linspace(0, 1, 100)
y_values = np.random.randn(100)

trace0 = go.Scatter(x= x_values, y= y_values+7, 
                    mode= 'markers', name= 'markers')
trace1 = go.Scatter(x= x_values, y= y_values, 
                    mode= 'lines', name= 'mylines')
trace2 = go.Scatter(x= x_values, y= y_values-7, 
                    mode= 'lines+markers', name= 'line+markers')

data = [trace0, trace1, trace2]

layout = go.Layout(title= 'Line Chart')
fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename= 'Line_Chart')