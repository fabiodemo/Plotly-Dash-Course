import dash
import dash_html_components as html

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