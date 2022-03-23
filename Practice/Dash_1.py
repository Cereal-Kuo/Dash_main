from dash import Dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# 該名稱(app)可以做更換
# "app" is the Dash application name which can be replaced by others
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
# pandas dataframe
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# 設定x, y軸的標示參數
# Setup x, y axis indexing parameters
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

# 導入app的外觀，主體以html的code架構為基底
# demonstrate the layout of the application which is based on html code
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

# 與R.shiny相似，透過啟用sever來啟動app
# similar to R.shiny, by activating the server to initiate application
if __name__ == '__main__':
    app.run_server(debug=True)