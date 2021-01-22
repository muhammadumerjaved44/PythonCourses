# -*- coding: utf-8 -*-
import pandas as pd
df = pd.DataFrame({
'name': ['alice','bob','charlie','david'],
'age': [25,26,27,22],
})[['name', 'age']]
# each element of the age column is a string
# so you can call .upper() on it
df['name_uppercase'] = df['name'].apply(lambda element: element.upper())
