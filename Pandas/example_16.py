# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
df = pd.DataFrame({
'name':['john','david','anna'],
'country':['USA','UK',np.nan]
})
df.query('country.notnull()')
