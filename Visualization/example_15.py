# -*- coding: utf-8 -*-
import plotly.graph_objs as go
# read csv from web
df = pd.read_csv('https://github.com/chris1610/pbpython/blob/master/data/cereal_data.csv?raw=True')
# create trace
trace_1 = go.Scatter(
    x=df['sugars'].tolist(),
    y=df['rating'].tolist(),
    mode="markers",
    name='rating'
)
# create list of plots, for now we have only one
data = [trace_1]
# layout settings
layout = go.Layout(
    title = dict(
        text = "Sugar vs Rating",
        font = dict(
            family = "Open Sans",
            size = 34,
            color = '#2a3f5f'
            ),
        x = 0.5
     ),
    showlegend = True,
        xaxis = dict(
        title = dict (
            text = 'Sugar',
            font = dict(
            family = "Open Sans",
            size = 12,
            color = '#2a3f5f'
),
),
    tickprefix = None
),
yaxis = dict(
    title = dict (
        text = 'Rating',
        font = dict(
        family = "Open Sans",
        size = 12,
        color = '#2a3f5f'
)
),
tickprefix = None,
showticklabels = True
),
)
#pass all data and layout into fig object
fig = go.Figure(data=data, layout=layout)
fig.show()

