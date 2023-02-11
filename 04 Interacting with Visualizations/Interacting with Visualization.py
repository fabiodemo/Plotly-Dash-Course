#!/usr/bin/env python
# coding: utf-8

# # Interacting with Visualizations

# - The information can be served internally using json and then parsed for a specific information;
# - Every graph has a hoverData component property that can be accessed.

# ## Hover Over Data

# In[3]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json
import base64
import numpy as np


# In[3]:


df = pd.read_csv('../Data/wheels.csv')


# In[6]:


app = dash.Dash()

app.layout = html.Div(
    [
        html.Div(
            dcc.Graph(
                id = 'wheels-plot',
                figure = {
                    'data': [
                        go.Scatter(
                            x = df.color,
                            y = df.wheels,
                            dy = 1,
                            mode = 'markers',
                            marker = {
                                'size': 15
                            }
                        )
                    ], 
                    'layout': go.Layout(
                        title = 'Test',
                        hovermode = 'closest'
                    )
                }
            )
        ),
        html.Div(
            html.Pre(
                id = 'hover-data',
                style = {'paddingTop': 35}
            ),
            style = {
                'width': '30%'
            }
        )
    ]
)

@app.callback(
    Output(
        'hover-data',
        'children'
    ),
    [
        Input(
            'wheels-plot',
            'hoverData'
        )
    ]
)
def callback_image(hoverData):
    return json.dumps(hoverData, indent = 2)

if __name__ == '__main__':
    app.run_server()


# In[7]:


app = dash.Dash()

app.layout = html.Div(
    [
        html.Div(
            dcc.Graph(
                id = 'wheels-plot',
                figure = {
                    'data': [
                        go.Scatter(
                            x = df.color,
                            y = df.wheels,
                            dy = 1,
                            mode = 'markers',
                            marker = {
                                'size': 15
                            }
                        )
                    ], 
                    'layout': go.Layout(
                        title = 'Test',
                        hovermode = 'closest'
                    )
                }
            ),
            style = {
                'width': '30%',
                'float': 'left'
            }
        ),
        html.Div(
            html.Pre(
                id = 'hover-data',
                style = {'paddingTop': 35}
            ),
            style = {
                'width': '30%'
            }
        )
    ]
)

@app.callback(
    Output(
        'hover-data',
        'children'
    ),
    [
        Input(
            'wheels-plot',
            'hoverData'
        )
    ]
)
def callback_image(hoverData):
    return json.dumps(hoverData, indent = 2)

if __name__ == '__main__':
    app.run_server()


# In[22]:


app = dash.Dash()

df = pd.read_csv('../Data/wheels.csv')

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app.layout = html.Div([
    html.Div([
    dcc.Graph(
        id='wheels-plot',
        figure={
            'data': [
                go.Scatter(
                    x = df['color'],
                    y = df['wheels'],
                    dy = 1,
                    mode = 'markers',
                    marker = {
                        'size': 12,
                        'color': 'rgb(51,204,153)',
                        'line': {'width': 2}
                        }
                )
            ],
            'layout': go.Layout(
                title = 'Wheels & Colors Scatterplot',
                xaxis = {'title': 'Color'},
                yaxis = {'title': '# of Wheels','nticks':3},
                hovermode='closest'
            )
        }
    )], style={'width':'30%', 'float':'left'}),

    html.Div([
    html.Img(id='hover-image', src='children', height=300)
    ], style={'paddingTop':35})
])

@app.callback(
    Output('hover-image', 'src'),
    [Input('wheels-plot', 'hoverData')])
def callback_image(hoverData):
    wheel=hoverData['points'][0]['y']
    color=hoverData['points'][0]['x']
    path = '../Data/Images/'
    return encode_image(path+df[(df['wheels']==wheel) &     (df['color']==color)]['image'].values[0])

if __name__ == '__main__':
    app.run_server()


# ## Click Data

# In[21]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import base64

app = dash.Dash()

df = pd.read_csv('../Data/wheels.csv')

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app.layout = html.Div([
    html.Div([
    dcc.Graph(
        id='wheels-plot',
        figure={
            'data': [
                go.Scatter(
                    x = df['color'],
                    y = df['wheels'],
                    dy = 1,
                    mode = 'markers',
                    marker = {
                        'size': 12,
                        'color': 'rgb(51,204,153)',
                        'line': {'width': 2}
                        }
                )
            ],
            'layout': go.Layout(
                title = 'Wheels & Colors Scatterplot',
                xaxis = {'title': 'Color'},
                yaxis = {'title': '# of Wheels','nticks':3},
                hovermode='closest'
            )
        }
    )], style={'width':'30%', 'float':'left'}),

    html.Div([
    html.Img(id='click-image', src='children', height=300)
    ], style={'paddingTop':35})
])

@app.callback(
    Output('click-image', 'src'),
    [Input('wheels-plot', 'clickData')])
def callback_image(clickData):
    wheel=clickData['points'][0]['y']
    color=clickData['points'][0]['x']
    path = '../Data/Images/'
    return encode_image(path+df[(df['wheels']==wheel) &     (df['color']==color)]['image'].values[0])

if __name__ == '__main__':
    app.run_server()


# ## Selection Data

# In[16]:


app = dash.Dash()

np.random.seed(10)
x1 = np.linspace(0.1, 5, 50)
x2 = np.linspace(5.1, 10, 50)
y = np.random.randint(0, 50, 50)

df1 = pd.DataFrame({'x': x1, 'y': y})
df2 = pd.DataFrame({'x': x1, 'y': y})
df3 = pd.DataFrame({'x': x2, 'y': y})

df = pd.concat([df, df2, df3])

app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Graph(
                    id = 'plot',
                    figure = {
                        'data': [
                            go.Scatter(
                                x = df['x'],
                                y = df['y'],
                                mode = 'markers'
                            )
                        ],
                        'layout': go.Layout(
                            title = 'Scatterplot',
                            hovermode = 'closest'
                        )
                    }
                )
            ],
            style = {
                'width': '30%',
                'display': 'inline-block'
            }
        ),
        html.Div(
            [
                html.H1(
                id = 'density',
                style = {
                    'paddingTop': 25
                }
                )
            ],
            style = {
                'width': '30%',
                'display': 'inline-block',
                'verticalAlign': 'top'
            }
        )
    ]
)

@app.callback(
    Output(
        'density', 'children'
    ),
    [
        Input(
            'plot', 'selectedData'
        )
    ]
)
def find_density(selectedData):
    # Calculate the density
    pts = len(selectedData['points'])
    rng_or_lp = list(selectedData.keys())
    rng_or_lp.remove('points')
    max_x = max(selectedData[rng_or_lp[0]]['x'])
    min_x = min(selectedData[rng_or_lp[0]]['x'])
    max_y = max(selectedData[rng_or_lp[0]]['y'])
    min_y = min(selectedData[rng_or_lp[0]]['y'])
    area = (max_x - min_x) * (max_y - min_y)
    d = pts/area
    return 'Density = {:.2f}'.format(d)

if __name__ == '__main__':
    app.run_server()


# ## Updating Graphs on Interactions

# - The user interaction can be the parameter that adjust a plot on a dashboard.

# ### Part I

# In[22]:


from numpy import random

app = dash.Dash()

df = pd.read_csv('../Data/mpg.csv')
# Adding Noise, adding jitter
df['year'] = random.randint(-4, 5, len(df)) * 0.1 + df['model_year']

app.layout = html.Div(
    [
        dcc.Graph(
            id = 'mpg-scatter',
            figure = {
                'data': [
                    go.Scatter(
                        x = df['year']+1900,
                        y = df['mpg'],
                        text = df['name'],
                        hoverinfo = 'text' + 'y' + 'x',
                        mode = 'markers'
                    )
                ],
                'layout': go.Layout(
                    title = 'MPG Data',
                    xaxis = {'title' : 'MODEL Year'},
                    yaxis = {'title': 'MPG'},
                    hovermode = 'closest'
                )
            }
        )
    ]
)

if __name__ == '__main__':
    app.run_server()


# ## Updating Graph on Interactions - Part II

# In[19]:


from numpy import random

app = dash.Dash()

df = pd.read_csv('../Data/mpg.csv')
# Adding Noise, adding jitter
df['year'] = random.randint(-4, 5, len(df)) * 0.1 + df['model_year']

app.layout = html.Div([
    html.Div([   # this Div contains our scatter plot
    dcc.Graph(
        id='mpg-scatter',
        figure={
            'data': [go.Scatter(
                x = df['year']+1900,  # our "jittered" data
                y = df['mpg'],
                text = df['name'],
                hoverinfo = 'text',
                mode = 'markers'
            )],
            'layout': go.Layout(
                title = 'mpg.csv dataset',
                xaxis = {'title': 'model year'},
                yaxis = {'title': 'miles per gallon'},
                hovermode='closest'
            )
        }
    )], style={'width':'50%','display':'inline-block'}),
    html.Div([  # this Div contains our output graph
    dcc.Graph(
        id='mpg_line',
        figure={
            'data': [go.Scatter(
                x = [0,1],
                y = [0,1],
                mode = 'lines'
            )],
            'layout': go.Layout(
                title = 'acceleration',
                margin = {'l':0}
            )
        }
    )
    ], style={'width':'20%', 'height':'50%','display':'inline-block'})
])


@app.callback(
    Output('mpg_line', 'figure'),
    [Input('mpg-scatter', 'hoverData')]
)
def callback_graph(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    figure = {
        'data': [
            go.Scatter(
                x = [0, 1],
                y = [0, 60/df.iloc[v_index]['acceleration']],
                mode = 'lines'
            )
        ],
        'layout': go.Layout(
            title = df.iloc[v_index]['name'],
            xaxis = {'visible': False},
            yaxis = {
                'visible': False,
                'range': [0, 60/df['acceleration'].min()]
            },
            margin = {'l': 0},
            height = 300
        )
    }
    return figure

if __name__ == '__main__':
    app.run_server()


# ## Updating Graph on Interactions - Part III

# In[22]:


from numpy import random

app = dash.Dash()

df = pd.read_csv('../Data/mpg.csv')
# Adding Noise, adding jitter
df['year'] = random.randint(-4, 5, len(df)) * 0.1 + df['model_year']

app.layout = html.Div([
    html.Div([   # this Div contains our scatter plot
    dcc.Graph(
        id='mpg-scatter',
        figure={
            'data': [go.Scatter(
                x = df['year']+1900,  # our "jittered" data
                y = df['mpg'],
                text = df['name'],
                hoverinfo = 'text',
                mode = 'markers'
            )],
            'layout': go.Layout(
                title = 'mpg.csv dataset',
                xaxis = {'title': 'model year'},
                yaxis = {'title': 'miles per gallon'},
                hovermode='closest'
            )
        }
    )], style={'width':'50%','display':'inline-block'}),
    html.Div([  # this Div contains our output graph
    dcc.Graph(
        id='mpg_line',
        figure={
            'data': [go.Scatter(
                x = [0,1],
                y = [0,1],
                mode = 'lines'
            )],
            'layout': go.Layout(
                title = 'acceleration',
                margin = {'l':0}
            )
        }
    )
    ], style={'width':'20%', 'height':'50%','display':'inline-block'}),
    html.Div([
        dcc.Markdown(
            id = 'mpg_stats'
        )
    ], style = {'width':'20%', 'height':'50%','display':'inline-block'})
])


@app.callback(
    Output('mpg_line', 'figure'),
    [Input('mpg-scatter', 'hoverData')]
)
def callback_graph(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    figure = {
        'data': [
            go.Scatter(
                x = [0, 1],
                y = [0, 60/df.iloc[v_index]['acceleration']],
                mode = 'lines',
                line = {
                    'width' : 3*df.iloc[v_index]['cylinders']
                }
            )
        ],
        'layout': go.Layout(
            title = df.iloc[v_index]['name'],
            xaxis = {'visible': False},
            yaxis = {
                'visible': False,
                'range': [0, 60/df['acceleration'].min()]
            },
            margin = {'l': 0},
            height = 300
        )
    }
    return figure

@app.callback(
    Output('mpg_stats', 'children'),
    [Input('mpg-scatter', 'hoverData')]
)
def callback_stats(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    stats = """
            {} cylinders
            {}cc displacement
            0 to 60mph in {} seconds
    """.format(
        df.iloc[v_index]['cylinders'],
        df.iloc[v_index]['displacement'],
        df.iloc[v_index]['acceleration']
    )
    return stats

if __name__ == '__main__':
    app.run_server()

