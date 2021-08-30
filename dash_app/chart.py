import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

#app = dash.Dash(__name__)
def create_chart_app(flask_app):
    chart_app = dash.Dash(server = flask_app, name = "Chartboard", url_base_pathname='/chart/')
    chart_app.layout = html.Div([
        dcc.Graph(id='graph-with-slider'),
        dcc.Slider(
            id='year-slider',
            min=df['year'].min(),
            max=df['year'].max(),
            value=df['year'].min(),
            marks={str(year): str(year) for year in df['year'].unique()},
            step=None
        )
    ])
    init_callbacks(chart_app)
    return chart_app

def init_callbacks(chart_app):
    @chart_app.callback(
        Output('graph-with-slider', 'figure'),
        Input('year-slider', 'value'))
    def update_figure(selected_year):
        filtered_df = df[df.year == selected_year]

        fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                        size="pop", color="continent", hover_name="country",
                        log_x=True, size_max=55)

        fig.update_layout(transition_duration=500)

        return fig


#if __name__ == '__main__':
    #app.run_server(debug=True)