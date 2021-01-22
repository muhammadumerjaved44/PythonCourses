# -*- coding: utf-8 -*-
import pandas as pd
df = pd.DataFrame({
'name': ['alice','bob','charlie','david'],
'age': [25,26,27,22],
})
# function that takes one value, returns one value
def first_letter(input_str):
    return input_str[:1]
# pass just the function name to apply
df['first_letter'] = df['name'].apply(first_letter)
