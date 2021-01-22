# -*- coding: utf-8 -*-
import pandas as pd
df = pd.DataFrame({
'col1':['foo','bar','baz','quux']
})
df.query('col1.str.contains("ba")')
