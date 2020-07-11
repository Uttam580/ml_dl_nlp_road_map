import pandas as pd 
import numpy as np
import plotly.graph_objects as go 
import plotly.offline as pyo 

from dash import Dash
import dash_core_components as dcc 
import dash_html_components as html 

app= Dash()

np.random.seed(42)
random_x= np.random.randint(1,101,100)
random_y= np.random.randint(1,101,100)

app.layout= html.Div([dcc.Graph(
                id='scatterplot',
                figure= {'data':[
                    go.Scatter(
                        x= random_x,
                        y =random_y,
                        mode= 'markers',
                        marker={
                            'size': 12,
                            'color': 'rgb(51,204,159)',
                            'symbol':'pentagon',
                            'line': {'width':2}
                        }
                    )
                ],'layout': go.Layout(title='myscatterplot1',
                                        xaxis = {'title': 'X_axis'})}
),dcc.Graph(
                id='scatterplot2',
                figure= {'data':[
                    go.Scatter(
                        x= random_x,
                        y =random_y,
                        mode= 'markers',
                        marker={
                            'size': 12,
                            'color': 'rgb(200,53,159)',
                            'symbol':'pentagon',
                            'line': {'width':2}
                        }
                    )
                ],'layout': go.Layout(title='myscatterplot2',
                                        xaxis = {'title': 'X_axis'})}
)])


if __name__ == "__main__":
    app.run_server()

