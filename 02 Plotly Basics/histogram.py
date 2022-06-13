import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Data/mpg.csv')

data = [go.Histogram(x= df.mpg)]
layout = go.Layout(title= 'Histogram')
fig = go.Figure(data= data, layout= layout)

pyo.plot(fig, filename= 'Histogram_01')

df = pd.read_csv('../Data/mpg.csv')

data = [
        go.Histogram(x= df.mpg,
        xbins= dict(start= 0, end= 50, size= 10)
    )]
layout = go.Layout(title= 'Histogram Size 10')
fig = go.Figure(data= data, layout= layout)

pyo.plot(fig, filename= 'Histogram_01.html');

df = pd.read_csv('../Data/mpg.csv')

data = [
        go.Histogram(x= df.mpg,
        xbins= dict(start= 0, end= 50, size= 2)
    )]
layout = go.Layout(title= 'Histogram Size 2')
fig = go.Figure(data= data, layout= layout)

pyo.plot(fig, filename= 'Histogram_02.html');