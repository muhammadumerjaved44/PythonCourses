# -*- coding: utf-8 -*-
import pandas as pd
# import plotly
import plotly.graph_objs as go
# read csv from web
df = pd.read_csv('https://github.com/chris1610/pbpython/blob/master/data/cereal_data.csv?raw=True')
analysis = df.groupby(['mfr', 'name'])['protein', 'fiber', 'calories'].sum().reset_index()
analysis
single_profile = analysis.query('mfr == "Ralston Purina"')
single_profile
bar2 = go.Bar(
y=single_profile.protein,
x=single_profile.name.tolist(),
# orientation='h',
name='protein',
width=0.6,
marker_color='orange'
)
bar1 = go.Bar(
y=single_profile.fiber,
x=single_profile.name.tolist(),
# orientation='h',
name='fiber',
width=0.8,
marker_color='black'
)
data = [bar1, bar2]
fig = go.Figure(data=data)
fig.update_layout(barmode="overlay")
fig.update_layout(
title = dict(
text = "Ralston Purina (Cerial profile)",
font = dict(
family = "Open Sans",
size = 32,
color = '#2a3f5f'
),
x = 0.1
),
showlegend = True,
legend = dict
(
y = 1.03
),
xaxis = dict(
title = dict (
text = 'Product list',
font = dict(
family = "Open Sans",
size = 24,
color = '#2a3f5f'
),
),
tickprefix = None,
# type='log',
),
yaxis = dict(
title = dict (
text = 'Total Amount found in Cerials',
font = dict(
family = "Open Sans",
size = 24,
color = '#2a3f5f'
)
),
tickprefix = None,
showticklabels = True,
# type='log',
),
)
fig.show()
