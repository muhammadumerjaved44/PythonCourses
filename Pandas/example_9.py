# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
df = pd.DataFrame({
'name':['john','david','anna'],
'country':['USA','UK',np.nan],
'age':[23,45,45]
})
target_age = 45
df.query('age == @target_age')
