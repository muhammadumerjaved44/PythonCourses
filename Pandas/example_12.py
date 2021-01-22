# -*- coding: utf-8 -*-
import pandas as pd
df = pd.DataFrame({
'name':['john','david','anna'],
'country':['USA','UK', 'USA'],
'age':[23,45,45]
})
names_array = ['john','anna']
df.query('name in @names_array')
