import dash.dependencies
from dash import Dash
import dash_html_components as html
import dash_core_components as dcc
from dash.exceptions import PreventUpdate
from dash.dependencies import State

app = Dash(__name__)

# 此處主要列出需要的drop down box 作為所需的內容
# labels = ['Taipei', 'Kaohsiung', 'Taichung']
"""
單一選擇
single choice
"""
# app.layout = html.Div([
#     dcc.Dropdown(options=[{'label': x, 'value': x} for x in labels],
#                  value='Kaohsiung')
# ])
"""
多重選擇
multi choices
"""
# app.layout = html.Div([
#     dcc.Dropdown(options=[{'label': x, 'value': x} for x in labels],
#                  value='Kaohsiung', multi=True, placeholder="Select cities")
# ])
"""
避免搜尋值 disable search
>>> search_value=False
可以避免值被搜尋到 Can prevent searching the dropdown value
"""
# app.layout = html.Div([
#     dcc.Dropdown(options=[{'label': x, 'value': x} for x in labels],
#                  value='Kaohsiung', search_value=False, placeholder="Select a city")
# ])
"""
進階動態選項
Dynamic Options
"""
options = [
    {"label": "Taipei", "value": "TPI"},
    {"label": "Kaohsiung", "value": "KHC"},
    {"label": "Taichung", "value": "TCC"},
]

app.layout = html.Div([
    html.Div(["Single dynamic Dropdown",
              dcc.Dropdown(id="Dynamic Dropdown", placeholder="Select a city")
              ]),
    html.Div(["Multiple dynamic Dropdown",
              dcc.Dropdown(id="Multiple Dynamic Dropdown", multi=True, placeholder="Select cities"),
              ]),
])


@app.callback(
    html.Output("Dynamic Dropdown", "options"),
    dcc.Input("Dynamic Dropdown", "search_value"))
def update_options(search_value):
    if not search_value:
        # If not search the value then prevent update
        raise PreventUpdate
    return [o for o in options if search_value in o["label"]]


@app.callback(
    html.Output("Multiple Dynamic Dropdown", "options"),
    dcc.Input("Multiple Dynamic Dropdown", "search_value"),
    State("Multiple Dynamic Dropdown", "value")
)
def update_multi_options(search_value, value):
    if not search_value:
        raise PreventUpdate
    # Make sure that the set values are in the option list, else they will disappear
    # from the shown select list, but still part of the `value`.
    return [
        o for o in options if search_value in o["label"] or o["value"] in (value or [])
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
