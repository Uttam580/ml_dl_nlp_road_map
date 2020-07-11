from dash import Dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output

app = Dash()

app.layout= html.Div([
                    dcc.Input(id='my_id',value= 'intial text', type='text'),
                    html.Div(id= 'my_div')


])
@app.callback(Output(component_id='my_div',component_property='children'),
                [Input(component_id='my_id',component_property='value')])

def update_output_div(input_value):
    return f'you entered : {input_value}'



if __name__ == "__main__":
    app.run_server()