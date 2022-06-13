import scipy
import plotly.offline as pyo
from plotly.tools import FigureFactory as ff ## More complex figures
import numpy as np
import pandas as pd

x1 = np.random.randn(1000)+2


hist_data = [x1]
group_labels = ['X1']

fig = ff.create_distplot(hist_data, group_labels);
pyo.plot(fig, filename= 'Distplot_01');

x1 = np.random.randn(1000)+2
x2 = np.random.randn(1000)
x3 = np.random.randn(1000)-2
x4 = np.random.randn(1000)+4


hist_data = [x1, x2, x3, x4]
group_labels = ['X1', 'X2', 'X3', 'X4']

fig = ff.create_distplot(hist_data, group_labels);
pyo.plot(fig, filename= 'Distplot_02');