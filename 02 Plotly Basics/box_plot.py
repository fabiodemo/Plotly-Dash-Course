#!/usr/bin/env python3
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

data = [go.Box(y=y, boxpoints= 'all', jitter=0.3, pointpos= 0)]
pyo.plot(data, filename= "Box_Plot_01")

y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]


data = [go.Box(y=y, boxpoints= 'outliers')]
pyo.plot(data, filename= "Box_Plot_02")

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

data = [
        go.Box(y=snodgrass, name= 'Snoodgrass'),
        go.Box(y= twain, name= 'Twain')
        ]
pyo.plot(data, filename= "Box_Plot_03")