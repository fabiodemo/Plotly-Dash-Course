#!/usr/bin/env python
# coding: utf-8

# # Dashboard Components

# ## HTML Components

# Dash componentes are provided by two libraries:
# - dash_html_components;
#     - Describe the layout of the page.
# - dash_core_components.
#     - Describe the individual graphs themselves.

# - Dash uses dictionaries to pass in CSS style calls;
# 

# In[1]:


import dash
import dash_html_components as html


# In[3]:


app = dash.Dash()

app.layout = html.Div(['This is the outermost div!'],
    style = {
        'color': 'green',
        'border': '2px green solid'
    }
)

if __name__ == '__main__':
    app.run_server()


# In[10]:


app = dash.Dash()

app.layout = html.Div([
        'This is the outermost div!',
        html.Div('This is a inner div!',
            style= {
                'color': 'red',
                'border': '2px red solid'
            },
        ),
        html.Div([
            'Another inner div!'
            ],
            style= {
                'color': 'blue', 
                'border': '2px blue solid'}
        )
    ],
    style = {
        'color': 'green',
        'border': '2px green solid'
    }
)

if __name__ == '__main__':
    app.run_server()


# ## Dash Core Components

# - Dash Core Components are more abstract (higher level) calls that allow to quickly insert common components into the dashboard;
# - Documentation available on:
#     - https://dash.plotly.com/dash-core-components
# -

# In[13]:


import dash
import dash_core_components as dcc
import dash_html_components as html


# In[23]:


app = dash.Dash()

app.layout = html.Div(
    [
        html.Label('Dropdown'),
        dcc.Dropdown(
            options = [
                {
                    'label': 'New Yor City', 
                    'value': 'NYC'
                },
                {
                    'label': 'San Francisco', 
                    'value': 'SF'
                }
            ],
            value = 'SF'
        ),
        html.Label('Slider'),
        dcc.Slider(
            min = - 10,
            max = 10,
            step = 0.5,
            value = 0,
            marks = {
                i: i for i in range(-10, 11)
            }
        ),
        # Paragraph for a 'quick/lazy fix'
        html.P(html.Label('Some Radio Items')),
        dcc.RadioItems(
            options = [
                {
                    'label': 'New Yor City', 
                    'value': 'NYC'
                },
                {
                    'label': 'San Francisco', 
                    'value': 'SF'
                }
            ],
            value = 'SF'
        )
    ]
)

if __name__ == '__main__':
    app.run_server()


# ## Markdown in Dash

# - Can also display markdown text, which allow links, italics, bold text, bullet lists, and more;
#     - http://commonmark.org/help.

# In[24]:


app = dash.Dash()

markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/) specification of Markdown.

Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!

Markdown includes syntax for things like **bold text** and *italics*,
[links](http://commonmark.org/help), inline `code` snippets, lists,
quotes, and more.
'''

app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
])

if __name__ == '__main__':
    app.run_server()


# ## Help with Dash

# Three main methods to get help:
# - The documentation;
# - Calling the Python function help();
# - Calling the pydoc at the terminal;

# In[25]:


import dash_html_components as html
print(help(html.Div))


# Generate an html containg all the documents for that library/component

# In[26]:


get_ipython().system('pydoc -w dash_html_components.Div')

