#!/usr/bin/env python
# coding: utf-8

# # Interactive Componentes

# ## Single Callbacks for Interactivity

# - Steps to create a callback from interactions:
#     - Create a function to return some desired output;
#     - Decorate that function with an @app.callback decorator;
#         - Set an **Output** to a component id;
#         - Set an **Input** to a component id.
#     - Connect the desired properties.

# In[1]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# In[6]:


app = dash.Dash()

app.layout = html.Div(
    [
        dcc.Input(
            id = 'my-id',
            value = 'Initial Text',
            type = 'text',
        ),
        html.Div(
            id = 'my-div',
            style = {
                'border': '2px blue solid'
            }
        )
    ]
)

@app.callback(
    Output(
        component_id = 'my-div', 
        component_property = 'children'
    ),
    [
        Input(
            component_id = 'my-id',
            component_property = 'value'
        )
    ]
)
def update_output_div(input_value):
    return "Your entered: {}".format(input_value)

if __name__ == '__main__':
    app.run_server()


# ## Dash Callbacks for Graphs

# In[1]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd


# In[2]:


df = pd.read_csv('../Data/gapminderDataFiveYear.csv')


# In[3]:


app = dash.Dash()


year_options = []
for year in df['year'].unique():
    year_options.append({'label': str(year), 'value':year})


app.layout = html.Div(
    [
        dcc.Graph(id = 'graph'),
        dcc.Dropdown(
            id = 'year-picker',
            options = year_options,
            value = df['year'].min()
        )
    ]
)

@app.callback(
    Output('graph', 'figure'),
    [Input(
        component_id = 'year-picker', 
        component_property = 'value'
    )]
)
def update_figure(selected_year):
    filtered_df = df[df['year'] == selected_year]

    traces = []

    for continent_name in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent'] == continent_name]
        traces.append(
            go.Scatter(
                x = df_by_continent['gdpPercap'],
                y = df_by_continent['lifeExp'],
                mode = 'markers',
                opacity = 0.7,
                marker = {'size': 15},
                name = continent_name
            )
        )
    return {'data': traces, 'layout': go.Layout(
        title = 'My Plot',
        xaxis = {'title': 'GDP Per Cap', 'type': 'log'},
        yaxis = {'title': 'Life Expectancy'}
    )}

if __name__ == '__main__':
    app.run_server()


# In[4]:


year_options


# ## Multiple Components

# ### Multiple inputs

# In[25]:


df = pd.read_csv('../Data/mpg.csv')


# In[16]:


app = dash.Dash()

features = df.columns

app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Dropdown(
                    id = 'xaxis',
                    options = [
                        {'label': i, 'value': i} for i in features
                    ],
                    value = 'displacement'
                ),
            ],
            style = {'width': '48%', 'display': 'inline-block'}
        ),
        html.Div(
            [
                dcc.Dropdown(
                    id = 'yaxis',
                    options = [
                        {'label': i, 'value': i} for i in features
                    ],
                    value = 'mpg'
                )
            ],
            style = {'width': '48%', 'display': 'inline-block'}
        ),
        dcc.Graph(id = 'feature-graphic')
    ],
    style = {'padding': 10}
)

@app.callback(
    Output('feature-graphic', 'figure'),
    [Input('xaxis', 'value'), 
    Input('yaxis', 'value')]
)
def update_graph(xaxis_name, yaxis_name):
    return {
        'data': [
            go.Scatter(
                x = df[xaxis_name],
                y = df[yaxis_name],
                text = df['name'],
                mode = 'markers',
                marker = {
                    'size': 15,
                    'opacity': 0.5,
                    'line': {
                        'width': 0.5,
                        'color': 'white'
                    }
                }
            )
        ], 
        'layout': go.Layout(
            title = 'My Dashboard for MPG',
            xaxis = {'title': xaxis_name},
            yaxis = {'title': yaxis_name},
            hovermode = 'closest'
        )
    }

if __name__ == '__main__':
    app.run_server()


# ### Multiple Outputs

# In[9]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import base64


# In[26]:


df = pd.read_csv('../Data/wheels.csv')


# In[27]:


df.head(3)


# In[28]:


app = dash.Dash()

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app.layout = html.Div(
    [
        dcc.RadioItems(
            id = 'wheels',
            options = [
                {'label': i, 'value': i} for i in df.wheels.unique()
            ],
            value = 1
        ),
        html.Div(
            id = 'wheels-output'
        ),
        html.Hr(),
        dcc.RadioItems(
            id = 'colors',
            options = [
                {'label': i, 'value': i} for i in df.color.unique()
            ],
            value = 1
        ),        
        html.Div(
            id = 'colors-output'
        ),
        html.Img(
            id = 'display-image',
            src = 'children',
            height = 300,
        )
    ],
    style = {
        'fontFamily': 'helvetica', 
        'fontsize': 18
    }
)

@app.callback(
    Output(
        'wheels-output', 'children'
    ),
    [
        Input(
            'wheels',
            'value'
        )
    ]
)
def callback_wheels(wheels_value):
    return "you chose {}".format(wheels_value)

@app.callback(
    Output(
        'colors-output', 'children'
    ),
    [
        Input(
            'colors',
            'value'
        )
    ]
)
def callback_colors(colors_value):
    return "you chose {}".format(colors_value)


@app.callback(
    Output('display-image', 'src'),
    [
        Input(
            'wheels', 'value'
        ),
        Input(
            'colors', 'value'
        )
    ]
)
def callback_image(wheel, color):
    path = '../Data/Images/'
    return encode_image(path+df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0])

if __name__ == '__main__':
    app.run_server()


# ### Exercise With Interactive Components

# - Objective: Create a dashboard that takes in two or more input values and returns their product as the output.
# 

# In[75]:


# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

# Launch the application:
app = dash.Dash()

range_min = -10
range_max = 10
step = 1

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:



app.layout = html.Div(
    [
        html.Div(
            dcc.RangeSlider(
            id = 'my-range-slider',
            min = range_min,
            max = range_max,
            step = step,
            value = [(range_max/2) - 2, (range_max/2) + 2],
            marks = {
                i: i for i in range(range_min,range_max+1)
            
            }),
            style = {
                'padding': 10,
                'width': '66%'
            } 
        ),
        html.Div(
            html.H1(
            id = 'output-range-slider'
        )
        )
        
    ],
    style = {'padding': 10}
)

# Create a Dash callback:
@app.callback(
    Output('output-range-slider', 'children'),
    [
        Input('my-range-slider', 'value')
    ]
)
def show_value(value):
    return '{}'.format(value[0] * value[1])

# Add the server clause:
if __name__ == '__main__':
    app.run_server()


# ## Controlling Callbacks with State

# - Normally, as soon as values are entered, the page updates to reflects any changes
# - But there are cases when its necessary to wait a series of changes for some time, before displaying the page;
# - dash.dependecies.States
#     - Offers the ability to store saved changes and send the mback on command.
#         - Kind like hitting a submit button on a form.
# - **State()** is added to the **@app.callback** along with an **Input()** and **Output()**
#     - The state is then connected to a component id and a property to report back.

# In[76]:


import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


# In the code below, the app will automatically update

# In[104]:


app = dash.Dash()

app.layout = html.Div(
    [
        dcc.Input(
            id = 'number-in',
            value = 1,
            style = {
                'fontSize': 24
            }
        ),
        html.H1(
            id = 'number-out'
        )
    ]
)

@app.callback(
    Output(
        'number-out', 
        'children'
    ),
    [Input(
        'number-in',
        'value'
    )]
)
def callback_state(number):
    return number

if __name__ == '__main__':
    app.run_server(port = 8080)


# In[103]:


app = dash.Dash()

app.layout = html.Div(
    [
        dcc.Input(
            id = 'number-in',
            value = 1,
            style = {
                'fontSize': 24
            }
        ),
        html.Button(
            id = 'submit-button',
            n_clicks = 0,
            children = 'Submit Here',
            style = {
                'fontSize': 24
            }
        ),
        html.H1(
            id = 'number-out'
        )
    ]
)

@app.callback(
    Output(
        'number-out', 
        'children'
    ),
    [Input(
        'submit-button',
        'n_clicks'
    )],
    [State(
        'number-in',
        'value'
    )]
)
def callback_state(number, n_clicks):
    return "{} was type in, and button was clicked {} times".format(n_clicks, number)

if __name__ == '__main__':
    app.run_server(port = 8080)

