from dash import Dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.express as px

# 該名稱(app)可以做更換
# "app" is the Dash application name which can be replaced by others
app = Dash(__name__)

# pandas dataframe
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# 設定x, y軸的標示參數
# Setup x, y axis indexing parameters
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# 導入app的外觀，主體以html的code架構為基底
# demonstrate the layout of the application which is based on html code
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# 與R.shiny相似，透過啟用sever來啟動app
# similar to R.shiny, by activating the server to initiate application
if __name__ == '__main__':
    app.run_server(debug=True)
