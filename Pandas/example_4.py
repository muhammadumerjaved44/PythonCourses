# -*- coding: utf-8 -*-
import pandas as pd
df = pd.DataFrame({
'name':['john','mary','peter','jeff','bill','lisa'],
'age':[23,78,22,19,45,33],
'state':['iowa','dc','california','texas','washington','dc'],
'num_children':[2,2,0,1,2,1],
'num_pets':[0,4,0,5,0,0]
})
# sorting columns
df=df[['name','age','state','num_children','num_pets']]
df
# select the first 2 rows
df.iloc[:2]
# select the last 2 rows
df.iloc[-2:]
# select rows up to and including the one
# with index=2
df.loc[:2]
# by a simple numeric condition
df[df["age"] > 30]
# comparing the value of two columns
df[ df["num_pets"] > df[ "num_children"] ]
# using boolean AND
df[ (df["age"] > 40) & (df["num_pets"] > 0) ]
