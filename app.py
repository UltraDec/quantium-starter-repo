import pandas
from dash import Dash, html, dcc, Input, Output, callback

from plotly.express import line

app = Dash()

dash_app = Dash(__name__)

data = pandas.read_csv("./task2complete.csv")
data = data.sort_values(by="date")

line_chart = line(data, x="date", y="sales", color="region", title="Pink Morsel Sales")


region_colors = {
    'north': '#1f77b4',  # Blue
    'south': '#2ca02c',  # Green
    'east': '#ff7f0e',   # Orange
    'west': '#9467bd',   # Purple
}

header = html.H1(
    "Pink Morsel Sales",
    id="header",
    style={"text-align": "center"}
)

dash_app.layout = html.Div(
    [
        header,
        dcc.Graph(id="visualization", figure=line_chart),
        dcc.RadioItems(
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'South', 'value': 'south'},
                {'label': 'East', 'value': 'east'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All Regions', 'value': 'all'}
            ],
            value='all',
            id='options'
        )
    ]
)

@callback(
    Output('visualization', 'figure'),
    Input('options', 'value'))
def set_options(selected):
    if selected == 'all':
        filtered_data = data  
    else:
        filtered_data = data[data['region'] == selected]
    color_column = "region"
    updated_chart = line(filtered_data, x="date", y="sales", color=color_column, color_discrete_map=region_colors, title=f"Region: {selected.capitalize()}")
    return updated_chart

if __name__ == '__main__':
    dash_app.run_server()