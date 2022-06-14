import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash()

# crash_free = 0

# def refresh_layout():
#     global crash_free
#     crash_free += 1
#     return html.H1('Crash free for {} refreshes'.format(crash_free))

# app.layout = refresh_layout

app.layout = html.Div([
    html.H1(
        id = 'live-update-text'
    ),
    dcc.Interval(
        id = 'interval-component',
        interval = 2000,
        n_intervals = 0
    )
])


@app.callback(
    Output('live-update-text', 'children'),
    [Input('interval-component', 'n_intervals')]
)
def update_layout(n):
    return 'Crash free for {} refreshes'.format(n)

if __name__ == '__main__':
    app.run_server(port = 8051)