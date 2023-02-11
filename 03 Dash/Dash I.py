#!/usr/bin/env python
# coding: utf-8

# # Dash

# - Dash is used for creating Dashboards purely in Python;
# - These dashboards are served as web applications that can be deployed;
#     - Not just only static html files.
# - We can connect and interact with teh dashboards;
# - Can manipulate HTML or CSS inside Python;
# - **dash_core_components** library offers higher-level, interactive components that are generated with JavaScript, HTML and CSS through the React.js library;
# - Dash components are described entirely through keyword attributes;
#     - Dash is declarative.
# 

# In[27]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd


# ## Part One - Layouts

# In[7]:


app = dash.Dash()

app.layout = html.Div(children= [
    html.H1('Hello Dash!')
])

if __name__ == '__main__':
    app.run_server()


# In[6]:


app = dash.Dash()

app.layout = html.Div(children= [
    html.H1('Hello Dash!'),
    html.Div('Dash: Web Dashboard with Python'),
    dcc.Graph(
        id= 'Example',
        figure= {'data': [
            {'x': [1,2,3], 'y': [4,1,2], 'type': 'bar', 'name': 'SF'},
            {'x': [1,2,3], 'y': [2,5,3], 'type': 'bar', 'name': 'NYC'},
        ],
          'layout': {
              'title': 'BAR PLOTS!'
          }  
        }
    )
])

if __name__ == '__main__':
    app.run_server()


# In[ ]:


app = dash.Dash()

app.layout = html.Div(children= [
    html.H1('Hello Dash!'),
    html.Div('Dash: Web Dashboard with Python'),
    dcc.Graph(
        id= 'Example',
        figure= {'data': [
            {'x': [1,2,3], 'y': [4,1,2], 'type': 'bar', 'name': 'SF'},
            {'x': [1,2,3], 'y': [2,5,3], 'type': 'bar', 'name': 'NYC'},
        ],
          'layout': {
              'title': 'BAR PLOTS!'
          }  
        }
    )
])

if __name__ == '__main__':
    app.run_server()


# ## Part Two - Styling

# In[12]:


app = dash.Dash()

colors = {'background': '#111111', 'text': '#7FDBFF'}
#colors['text']

app.layout = html.Div(
    children= [
        html.H1(children= 'Hello Dash!', style={
            'textAlign': 'center',
            'color': colors['text']
        }),
        dcc.Graph(
            id= 'Example',
            figure= {'data': [
                {'x': [1,2,3], 'y': [4,1,2], 'type': 'bar', 'name': 'SF'},
                {'x': [1,2,3], 'y': [2,5,3], 'type': 'bar', 'name': 'NYC'},
            ],
            'layout': {
                'title': 'BAR PLOTS!',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {'color': colors['text']}
            }  
            }
        )
    ], 
    style={'backgroundColor': colors['background']}
)

if __name__ == '__main__':
    app.run_server()


# ## Part Three - Converting Simple PLotly Plot to Dashboard with Dash

# - Dash allows to easily insert plotly graphs into the Dashboard;

# In[15]:


np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)


# In[17]:


app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(
        id= 'scatterplot',
        figure= {
            'data': [
                go.Scatter(
                    x= random_x,
                    y= random_y,
                    mode= 'markers'
                )
            ],
            'layout': go.Layout(
                title= 'My Scatterplot'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()


# In[21]:


app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(
        id= 'scatterplot',
        figure= {
            'data': [
                go.Scatter(
                    x= random_x,
                    y= random_y,
                    mode= 'markers',
                    marker= {
                        'size': 12,
                        'color': 'rgb(51, 203, 153)',
                        'symbol': 'pentagon',
                        'line': {'width': 2}
                    }
                )
            ],
            'layout': go.Layout(
                title= 'My Scatterplot',
                xaxis= {'title': 'My X Axis Title'},
                yaxis= {'title': 'My Y Axis Title'}
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()


# In[23]:


app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(
        id= 'scatterplot',
        figure= {
            'data': [
                go.Scatter(
                    x= random_x,
                    y= random_y,
                    mode= 'markers',
                    marker= {
                        'size': 12,
                        'color': 'rgb(51, 203, 153)',
                        'symbol': 'pentagon',
                        'line': {'width': 2}
                    }
                )
            ],
            'layout': go.Layout(
                title= 'My Scatterplot',
                xaxis= {'title': 'My X Axis Title'},
                yaxis= {'title': 'My Y Axis Title'}
            )
        }
    ),
    dcc.Graph(
        id= 'scatterplot2',
        figure= {
            'data': [
                go.Scatter(
                    x= random_x,
                    y= random_y,
                    mode= 'markers',
                    marker= {
                        'size': 12,
                        'color': 'rgb(200, 203, 53)',
                        'symbol': 'pentagon',
                        'line': {'width': 2}
                    }
                )
            ],
            'layout': go.Layout(
                title= 'Second Plot',
                xaxis= {'title': 'My X Axis Title'},
                yaxis= {'title': 'My Y Axis Title'}
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()


# ## Exercise

# - Objective: build a dashboard that imports OldFaithful.csv
# - from the data directory, and displays a scatterplot.
# - The field names are:
# - 'D' = date of recordings in month (in August),
# - 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# - 'Y' = waiting time until the next eruption in minutes (to nearest minute).

# In[35]:


# Launch the application:
app = dash.Dash()

# Create a DataFrame from the .csv file:
df = pd.read_csv('../Data/OldFaithful.csv')
app.layout= html.Div(
    [
        dcc.Graph(
            id= 'scatterplot',
            figure= {
                'data': [
                    go.Scatter(
                        x= df.X,
                        y= df.Y,
                        mode= 'markers',
                        marker= {
                            'size': 7,
                            'color': 'rgb(51, 203, 153)',
                            'symbol': 'circle',
                            'line': {'width': 2}
                        }
                    )
                ],
                'layout': go.Layout(
                    title= 'Scatterplot Exercise About Vulcanic Eruptions',
                    xaxis= {'title': 'Duration of Eruption (in Minutes)'},
                    yaxis= {'title': 'Time to Nearest Eruption (in Minutes)'}
                )
            }
        )
    ]
)

# Create a Dash layout that contains a Graph component:

# Add the server clause:
if __name__ == '__main__':
    app.run_server()


# In[29]:


df

