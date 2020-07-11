import pandas as pd 
import numpy as np
import plotly.graph_objects as go 
import plotly.offline as pyo 

from dash import Dash
import dash_core_components as dcc 
import dash_html_components as html 

app= Dash()

colors= {'bg': '#111111',
        'text': '#7FDBFF'}

app.layout = html.Div(children =[
            html.H1('hello world',style={'textAlign':'center',
                                        'color': colors['text']}),
            dcc.Graph(id ='example',
                        figure = {'data':[
                                {'x':[1,2,3],'y': [4,1,2], 'type':'bar','name':'SF'},
                                {'x':[1,2,3],'y': [4,1,2], 'type':'bar','name':'NYC'}
                                ],
                                'layout': {
                                        'plot_bgcolor':colors['bg'],
                                        'paper_bgcolor':colors['bg'],
                                        'font': {'color': colors['text']},
                                        'title':'Bar plot'
                                        }
                                })
],style= {'backgroundColor': colors['bg']}

)



if __name__ == "__main__":
    app.run_server()

