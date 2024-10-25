from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data

component = dmc.Group(
    [
        dmc.LineChart(
            id="figure-linechart",
            h=300,
            dataKey="date",
            data=data,
            withLegend=True,
            series=[
                {"name": "Apples", "color": "indigo.6"},
                {"name": "Oranges", "color": "blue.6"},
                {"name": "Tomatoes", "color": "teal.6"},
            ],
            withTooltip=False,
        ),
        dmc.Text(id="clickdata-linechart1"),
        dmc.Text(id="clickdata-linechart2"),
    ]
)



@callback(
    Output("clickdata-linechart1", "children"),
    Output("clickdata-linechart2", "children"),
    Input("figure-linechart", "clickData"),
    Input("figure-linechart", "clickSeriesName"),
)
def update(data, name):
    return f"clickData:  {data}", f"clickSeriesName: {name}"

