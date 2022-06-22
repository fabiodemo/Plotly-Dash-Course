import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd

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