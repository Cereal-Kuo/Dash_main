from dash import Dash
import dash_html_components as html
import dash_core_components as dcc

app = Dash(__name__)

# 此處主要列出需要的drop down box 作為所需的內容
labels = ['New York City', 'Montréal', 'San Francisco']
app.layout = html.Div([
    dcc.Dropdown(options=[{'label': x, 'value': x} for x in labels],
                 value='Montréal')
])

if __name__ == '__main__':
    app.run_server(debug=True)
