#!/usr/bin/env python3
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [go.Scatter(x= random_x, y= random_y, mode= 'markers')]
pyo.plot(data, filename='Scatter_Plot_01.html')

data = [go.Scatter(
                    x= random_x, 
                    y= random_y, 
                    mode= 'markers',
                    marker= dict(
                                size= 12,
                                color= 'rgb(51, 204, 153)',
                                symbol= 'star',
                                line= {'width': 2}
                    ))]

layout = go.Layout(
                    title= 'Correlation Between Two Variables',
                    xaxis= {'title': 'MY X AXIS'},
                    yaxis= dict(title='MY Y AXIS'),
                    hovermode= 'closest'
                )

fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename='Scatter_Plot_02.html')