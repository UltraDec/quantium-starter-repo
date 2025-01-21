import pandas
from dash import Dash, html, dcc

from plotly.express import line

app = Dash()

dash_app = Dash(__name__)

data = pandas.read_csv("./task2complete.csv")
data = data.sort_values(by="date")

line_chart = line(data, x="date", y="sales", title="Pink Morsel Sales")
visualization = dcc.Graph(
    id="visualization",
    figure=line_chart
)

header = html.H1(
    "Pink Morsel Sales",
    id="header"
)

dash_app.layout = html.Div(
    [
        header,
        visualization
    ]
)

if __name__ == '__main__':
    dash_app.run_server()