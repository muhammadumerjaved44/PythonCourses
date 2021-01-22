# -*- coding: utf-8 -*-
import pandas as pd
df = pd.DataFrame({
'name':['john','david','anna'],
'country of birth':['USA','UK', 'USA'],
'age':[23,45,45]
})
df.query('`country of birth` == "UK"')
