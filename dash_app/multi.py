import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')


#app = dash.Dash(__name__)
def create_multi_app(flask_app):
    multi_app = dash.Dash(server = flask_app, name = "Multiboard", url_base_pathname='/multi/')
    multi_app.layout = html.Div([html.Div(children=[
        dcc.Graph(id='graph-with-slider'),
        dcc.Slider(
            id='year-slider',
            min=df['year'].min(),
            max=df['year'].max(),
            value=df['year'].min(),
            marks={str(year): str(year) for year in df['year'].unique()},
            step=None
            ),
        ], style = {'display': 'inline-block', 'width': '60%', 'height': '30%'}),
        html.Div(children=[
            dcc.Input(
                id='num-multi',
                type='number',
                value=5
            ),
            html.Table([
                html.Tr([html.Td(['x', html.Sup(2)]), html.Td(id='square')]),
                html.Tr([html.Td(['x', html.Sup(3)]), html.Td(id='cube')]),
                html.Tr([html.Td([2, html.Sup('x')]), html.Td(id='twos')]),
                html.Tr([html.Td([3, html.Sup('x')]), html.Td(id='threes')]),
                html.Tr([html.Td(['x', html.Sup('x')]), html.Td(id='x^x')]),
            ])
        ], style = {'display': 'inline-block', 'width': '10%', 'height': '20%'})
    ])
    init_callbacks(multi_app)
    init_callbacks2(multi_app)
    return multi_app

def init_callbacks(multi_app):
    @multi_app.callback(
        Output('graph-with-slider', 'figure'),
        Input('year-slider', 'value'))
    def update_figure(selected_year):
        filtered_df = df[df.year == selected_year]

        fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                        size="pop", color="continent", hover_name="country",
                        log_x=True, size_max=55)

        fig.update_layout(transition_duration=500)

        return fig
def init_callbacks2(multi_app):
    @multi_app.callback(
        Output('square', 'children'),
        Output('cube', 'children'),
        Output('twos', 'children'),
        Output('threes', 'children'),
        Output('x^x', 'children'),
        Input('num-multi', 'value'))
    def callback_a(x):
        return x**2, x**3, 2**x, 3**x, x**x


#if __name__ == '__main__':
    #app.run_server(debug=True)