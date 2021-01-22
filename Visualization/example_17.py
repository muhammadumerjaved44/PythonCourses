# -*- coding: utf-8 -*-
import pandas as pd
# import plotly
import plotly.graph_objs as go
31
# read csv from web
df = pd.read_csv('https://github.com/chris1610/pbpython/blob/master/data/cereal_data.csv?raw=True')
trace0 = go.Histogram(
x = df['sodium'],
histnorm='probability density',
opacity=0.75,
nbinsx=50,
name='sodium',
)
trace1 = go.Histogram(
x = df['potass'],
histnorm='probability density',
opacity=0.75,
nbinsx=50,
name='potass'
)
data = [trace0, trace1]
fig = go.Figure(data=data)
fig.show()

