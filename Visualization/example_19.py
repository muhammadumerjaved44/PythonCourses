# -*- coding: utf-8 -*-
import pandas as pd
import plotly
import plotly.graph_objs as go
import math
df = pd.read_csv('https://github.com/chris1610/pbpython/blob/master/data/cereal_data.csv?raw=True')
hover_text = []
bubble_size = []
for index, row in df.iterrows():
    hover_text.append((
'Potasium: {potass}<br>'+
'Sugars: {sugars}<br>'+
'Rating: {rating}<br>'+
'Type: {_type}<br>'+
'Name: {name}').format(
potass=row['potass'],
sugars=row['sugars'],
rating=row['rating'],
_type=row['type'],
name=row['name']))
bubble_size.append(row['rating'])
df['text'] = hover_text
df['size'] = bubble_size
companies_names = df.mfr.unique().tolist()
company_data = {company:df.query("mfr == '%s'" %company)
for company in companies_names}
sizeref = 2.*max(df['size'])/(60**2)
fig = go.Figure()
companies_names = df.mfr.unique().tolist()
company_data = {company:df.query("mfr == '%s'" %company)
for company in companies_names}
for companies_name, company in company_data.items():
    fig.add_trace(go.Scatter(
mode="markers",
x=company['potass'], y=company['sugars'],
name=companies_name,hovertext=company['text'],
marker_size=company['size'],
))
fig.update_traces(mode='markers', marker=dict(sizemode='area',
sizeref=sizeref, line_width=2))
fig.update_layout(
title = dict(
text = "Cerial Analysis",
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
text = 'Potassium in Cerials',
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
text = 'Sugars in Cerial',
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

