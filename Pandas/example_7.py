# -*- coding: utf-8 -*-
import pandas as pd
df = pd.DataFrame({
    'value1': [1,2,3,4,5],
    'value2': [5,4,3,2,1],
    'value3': [10,20,30,40,50],
    'value4': [99,99,99,99,np.nan],
})

def sum_all(row):
    return np.sum(row)
# note that apply was called on the dataframe itself, not on columns
df['sum_all'] = df.apply(lambda row: sum_all(row) , axis=1)
