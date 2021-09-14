import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

df = pd.read_csv('master.csv')

all_dims = ['Sensitivity', 'Score',
            'Date', 'Order', 'Index',
            'Score Relative to Average', 'Accuracy Relative to Average',
            'Score Relative to First Run', 'Accuracy Relative to First Run',]

chart_types = ['scatter', 'line', 'density_contour']

app = dash.Dash(__name__)

app.layout = html.Div([

    html.Div([

        dcc.Markdown('''
        `X Value`
        '''),

        dcc.Dropdown(
            id="dropdown-x",
            options=[{"label": x, "value": x} 
                    for x in all_dims],
            value='Accuracy Relative to Average',
            multi=False
        ),
    ], style={'width': '23%', 'display': 'inline-block', 'padding': '1%'}),

    html.Div([

        dcc.Markdown('''
        `Y Value`
        '''),

        dcc.Dropdown(
            id="dropdown-y",
            options=[{"label": x, "value": x} 
                    for x in all_dims],
            value='Score Relative to Average',
            multi=False
        ),
    ], style={'width': '22%', 'display': 'inline-block', 'padding': '1%'}),

    html.Div([

        dcc.Markdown('''
        `Chart Type`
        '''),

        dcc.Dropdown(
            id='chart_type',
            options=[{"label": x, "value": x} 
                    for x in chart_types],
            value='scatter',
            multi=False
        )
    ], style={'width': '22%', 'display': 'inline-block', 'padding': '1%'}),

    html.Div([
        
        dcc.Graph(id='scatter')

    ], style={'float': 'left', 'display': 'inline-block', 'padding-left': '5%'}),

], style={'zoom': '160%'})

@app.callback(
    Output("scatter", "figure"), 
    Input("dropdown-x", "value"),
    Input("dropdown-y", "value"),
    Input("chart_type", "value"))
def update_chart(dimx, dimy, chart_type='scatter'):
    if chart_type == 'scatter':
        fig = px.scatter(
            df, x=dimx, y=dimy, color="Scenario:")
        return fig
    if chart_type == 'line':
        fig = px.line(
            df, x=dimx, y=dimy, color="Scenario:")
        return fig
    if chart_type == 'density_contour':
        fig = px.density_contour(df, x=dimx, y=dimy, nbinsx=20, nbinsy=20)
        fig.update_traces(contours_coloring="fill", contours_showlabels = False, colorscale="Turbo", ncontours=20)
        return fig

app.run_server(debug=True)