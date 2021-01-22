# -*- coding: utf-8 -*-
import pandas as pd
df = pd.DataFrame({
'name':['john','david','anna'],
'country':['USA','UK',np.nan]
})
df.query("country == 'USA'")
