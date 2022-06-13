import scipy
import plotly.offline as pyo
from plotly.tools import FigureFactory as ff ## More complex figures
import numpy as np
import pandas as pd

df = pd.read_csv('../Data/2010SantaBarbaraCA.csv')

data = [go.Heatmap(
                    x=df.DAY, 
                    y= df.LST_TIME, 
                    z= df.T_HR_AVG.values.tolist())]
layout = go.Layout(title= 'SB CA Temps');
fig = go.Figure(data= data, layout= layout);

pyo.plot(fig, filename= 'Heatmap_01');

df = pd.read_csv('../Data/2010SantaBarbaraCA.csv')

data = [go.Heatmap(                    
                    x=df.DAY, 
                    y= df.LST_TIME, 
                    z= df.T_HR_AVG.values.tolist(),
                    colorscale= 'Jet')]
layout = go.Layout(title= 'YU MA Temps');
fig = go.Figure(data= data, layout= layout);

pyo.plot(fig, filename= 'Heatmap_02');