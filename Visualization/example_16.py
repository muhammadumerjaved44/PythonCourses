# -*- coding: utf-8 -*-
import pandas as pd
df = pd.read_csv('https://github.com/chris1610/pbpython/blob/master/data/cereal_data.csv?raw=True')
sugar = go.Scatter(
x=df['sugars'].tolist(),
y=df['calories'].tolist(),
mode="markers",
name='rating',
marker=dict(
size=df['rating'].tolist(),
color=[x for x in range(0, len(df['rating']))],
colorscale='Viridis',
showscale=True
),
hovertext = 'rating',
)
data = [sugar]
layout = go.Layout(
title = dict(
text = "Sugar vs Calories",
font = dict(
family = "Open Sans",
size = 34,
color = '#2a3f5f'
),
x = 0.5
),
showlegend = True,
legend = dict
(
y = 1.03
),
xaxis = dict(
title = dict (
text = 'Sugar',
font = dict(
family = "Open Sans",
size = 18,
color = '#2a3f5f'
),
),
tickprefix = None
),
yaxis = dict(
title = dict (
text = 'Calories',
font = dict(
family = "Open Sans",
size = 18,
color = '#2a3f5f'
)
),
tickprefix = None,
showticklabels = True
),
)
fig = go.Figure(data=data, layout=layout)
fig.show()

