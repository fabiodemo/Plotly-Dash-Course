#!/usr/bin/env python
# coding: utf-8

# # Milestone Project

# Using Pandas_datareader library
#     - A library updated for different API calls for stock information.

# ## Stock Price Dashboard Project

# ### Part I

# In[4]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd

app = dash.Dash()

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.H3('Enter a stock symbol: '),
    dcc.Input(
        id = 'my_ticket_symbol',
        value = 'TSLA'
    ),
    dcc.Graph(
        id = 'my_graph',
        figure = {
            'data': [{
                'x': [1,2], 'y': [3,1]
            }]
        }
    )
])

if __name__ == '__main__':
    app.run_server()


# ### Part II

# In[8]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd

app = dash.Dash()

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.H3('Enter a stock symbol: '),
    dcc.Input(
        id = 'my_ticket_symbol',
        value = 'TSLA'
    ),
    dcc.Graph(
        id = 'my_graph',
        figure = {
            'data': [{
                'x': [1,2], 'y': [3,1]
            }],
            'layout': {'title': 'Default Title'}
        }
    )
])

@app.callback(
    Output(
        'my_graph', 'figure'
    ),
    [Input('my_ticket_symbol', 'value')]
)
def update_graph(stock_ticker):
    fig = {
            'data': [{
                'x': [1,2], 'y': [3,1]
            }],
            'layout': {'title': stock_ticker}
    }
    return fig

if __name__ == '__main__':
    app.run_server()


# ### Part III
# Date Picker

# In[32]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd

app = dash.Dash()

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.H3('Enter a stock symbol: '),
    dcc.Input(
        id = 'my_ticket_symbol',
        value = 'TSLA'
    ),
    dcc.Graph(
        id = 'my_graph',
        figure = {
            'data': [{
                'x': [1,2], 'y': [3,1]
            }],
            'layout': {'title': 'Default Title'}
        }
    )
])

@app.callback(
    Output(
        'my_graph', 'figure'
    ),
    [Input('my_ticket_symbol', 'value')]
)
def update_graph(stock_ticker):
    start = datetime(2017, 1, 1)
    end = datetime(2017, 12, 31)
    df = web.DataReader(stock_ticker, 'quandl', start, end)
    print(df.head())
    fig = {
            'data': [{
                'x': df.index, 'y': df.Close
            }],
            'layout': {'title': stock_ticker}
    }
    return fig

if __name__ == '__main__':
    app.run_server()


# ### Part IV

# In[43]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd

app = dash.Dash()

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.Div([
        html.H3('Enter a stock symbol:',
        style = {'paddingRight': '30px'}
    ),

    dcc.Input(
        id = 'my_ticket_symbol',
        value = 'TSLA',
        style = {
            'fontSize': 24,
            'width': 75
        }
    )    
    ], style ={
        'paddingRight': '30px',
        'display': 'inline-block'
    }
    ),
    html.Div([
        html.H3('Select a start and end date:'),
        dcc.DatePickerRange(
            id = 'my_date_picker',
            min_date_allowed = datetime(2015,1,1),
            max_date_allowed = datetime.today(),
            start_date = datetime(2018, 1, 1),
            end_date = datetime.today()

        )
    ], style = {
        'display': 'inline-block'
    }
    ),
    dcc.Graph(
        id = 'my_graph',
        figure = {
            'data': [{
                'x': [1,2], 'y': [3,1]
            }],
        }
    )
])

@app.callback(
    Output(
        'my_graph', 'figure'
    ),
    [
        Input('my_ticket_symbol', 'value'),
        Input('my_date_picker', 'start_date'),
        Input('my_date_picker', 'end_date'),
    ]
)
def update_graph(stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')
    df = web.DataReader(stock_ticker, 'quandl', start, end)
    print(df.head())
    fig = {
            'data': [{
                'x': df.index, 'y': df.Close
            }],
            'layout': {'title': stock_ticker}
    }
    return fig

if __name__ == '__main__':
    app.run_server()


# ### Part V

# In[47]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd

app = dash.Dash()

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.Div([
        html.H3('Enter a stock symbol:',
        style = {'paddingRight': '30px'}
    ),

    dcc.Input(
        id = 'my_ticket_symbol',
        value = 'TSLA',
        style = {
            'fontSize': 24,
            'width': 75
        }
    )    
    ], style ={
        'paddingRight': '30px',
        'display': 'inline-block'
    }
    ),
    html.Div([
        html.H3('Select a start and end date:'),
        dcc.DatePickerRange(
            id = 'my_date_picker',
            min_date_allowed = datetime(2015,1,1),
            max_date_allowed = datetime.today(),
            start_date = datetime(2018, 1, 1),
            end_date = datetime.today()

        )
    ], style = {
        'display': 'inline-block'
    }
    ),
        html.Div([
        html.Button(
            id = 'submit-button',
            n_clicks = 0,
            children = 'Submit',
            style = {
                'fontSize': 24,
                'marginLeft': '30px'
            }
        )
    ], style = {
        'display': 'inline-block'
    }
    ),
    dcc.Graph(
        id = 'my_graph',
        figure = {
            'data': [{
                'x': [1,2], 'y': [3,1]
            }],
        }
    )
])

@app.callback(
    Output('my_graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [
        State('my_ticket_symbol', 'value'),
        State('my_date_picker', 'start_date'),
        State('my_date_picker', 'end_date'),
    ]
)
def update_graph(n_clicks, stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')
    df = web.DataReader(stock_ticker, 'quandl', start, end)
    print(df.head())
    fig = {
            'data': [{
                'x': df.index, 'y': df.Close
            }],
            'layout': {'title': stock_ticker}
    }
    return fig

if __name__ == '__main__':
    app.run_server()


# ### Part VI

# In[50]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd

app = dash.Dash()

nasdaq = pd.read_csv('../Data/NASDAQcompanylist.csv')
nasdaq.set_index('Symbol', inplace = True)
options = []

for tic in nasdaq.index:
    mydict = {}
    mydict['label'] = nasdaq.loc[tic]['Name'] + ' ' + tic # Apple Co. AAPL
    mydict['value'] = tic
    options.append(mydict)

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.Div([
        html.H3('Enter a stock symbol:',
        style = {'paddingRight': '30px'}
    ),

    dcc.Dropdown(
        id = 'my_ticket_symbol',
        options = options,
        value = ['TSLA'],
        multi = True
    )    
    ], style ={
        'display': 'inline-block',
        'verticalAlign': 'top',
        'width': '30%'
    }
    ),
    html.Div([
        html.H3('Select a start and end date:'),
        dcc.DatePickerRange(
            id = 'my_date_picker',
            min_date_allowed = datetime(2015,1,1),
            max_date_allowed = datetime.today(),
            start_date = datetime(2018, 1, 1),
            end_date = datetime.today()

        )
    ], style = {
        'display': 'inline-block'
    }
    ),
        html.Div([
        html.Button(
            id = 'submit-button',
            n_clicks = 0,
            children = 'Submit',
            style = {
                'fontSize': 24,
                'marginLeft': '30px'
            }
        )
    ], style = {
        'display': 'inline-block'
    }
    ),
    dcc.Graph(
        id = 'my_graph',
        figure = {
            'data': [{
                'x': [1,2], 'y': [3,1]
            }],
        }
    )
])

@app.callback(
    Output('my_graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [
        State('my_ticket_symbol', 'value'),
        State('my_date_picker', 'start_date'),
        State('my_date_picker', 'end_date'),
    ]
)
def update_graph(n_clicks, stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')
    
    traces = []
    for tic in stock_ticker:
        df = web.DataReader(tic, 'quandl', start, end)
        traces.append({'x': df.index, 'y': df.Close, 'name': tic})

    fig = {
            'data': traces,
            'layout': {'title': stock_ticker}
    }
    return fig

if __name__ == '__main__':
    app.run_server()

