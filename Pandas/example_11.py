# -*- coding: utf-8 -*-
import pandas as pd
df = pd.DataFrame({
'name':['john','david','anna'],
'country':['USA','UK', 'USA'],
'age':[23,45,45]
})
df.query("country=='USA' and age==23")
