# -*- coding: utf-8 -*-
import pandas as pd
# if you wish, you can set column names and dtypes here
df = pd.DataFrame()
# must reassign since the append method does not work in place
df = df.append({'col_a':5,'col_b':10}, ignore_index=True)
df = df.append({'col_a':1,'col_b':100}, ignore_index=True)
df = df.append({'col_a':32,'col_b':999}, ignore_index=True)
df

