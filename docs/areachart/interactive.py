import dash_mantine_components as dmc

from lib.configurator import Configurator

data = [
  {"date": "Mar 22", "Apples": 2890, "Oranges": 2338, "Tomatoes": 2452},
  {"date": "Mar 23", "Apples": 2756, "Oranges": 2103, "Tomatoes": 2402},
  {"date": "Mar 24", "Apples": 3322, "Oranges": 986, "Tomatoes": 1821},
  {"date": "Mar 25", "Apples": 3470, "Oranges": 2108, "Tomatoes": 2809},
  {"date": "Mar 26", "Apples": 3129, "Oranges": 1726, "Tomatoes": 2290}
]

target = dmc.AreaChart(
    h=300,
    dataKey="date",
    data=data,
    series=[
        { "name": 'Apples', 'color': 'indigo.6' },
        { "name": 'Oranges', 'color': 'blue.6' },
        { 'name': 'Tomatoes', 'color': 'teal.6' },
      ],
    curveType="linear",
    tickLine="xy",
    withGradient=False,
    withXAxis=False,
    withDots=False,
)

configurator = Configurator(target)

configurator.add_select(
    "curveType",
    ["Bump", "Linear", "Natural", "Monotone", "Step", "StepBefore", "StepAfter"],
    "Monotone",
)

configurator.add_segmented_control("tickLine", ["x", "y", "xy", "none"], "xy")
configurator.add_segmented_control("gridAxis", ["x", "y", "xy", "none"], "x")
configurator.add_switch("withGradient", False)
configurator.add_switch("withXAxis", False)
configurator.add_switch("withYAxis", False)
configurator.add_switch("withDots", False)


component = configurator.panel

