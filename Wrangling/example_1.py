# -*- coding: utf-8 -*-
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
file=pd.read_csv('https://forge.scilab.org/index.php/p/rdataset/source/file/master/csv/datasets/airquality.csv')
#%% display first 5 entries
first_rows = file.head()
print(first_rows)
#%% display first 10 entries
first_10_rows = file.head(10)
print(first_10_rows)
#%% display last 7 entries
last_rows = file.tail(7)
print(last_rows)
#%% size of the columns and rows
23
rows, cols = file.shape
print(rows,cols)
#%% find the datatypes of the columns
print(file.dtypes)
#%% drop the un_named cols
new_file = file.drop(columns=['Unnamed: 0'])
new_file.head()
#%% rename the cols names
columns_names = {'Ozone': 'ozone', 'Solar.R': 'solar',
'Wind':'wind', 'Temp':'temp', 'Month':'month', 'Day':'day'}
file_col_renames = new_file.rename(columns=columns_names)
file_col_renames.head()
#%% check the null values if any
null_values = (file_col_renames
.isna()
)
#%% count null values in each col
null_count = (
file_col_renames
.isna()
.sum()
)
#%% remove null values from rows
clean_file = file_col_renames.dropna()
print(clean_file.isna().sum())
#%% replace numbers with month name
cleanup_nums = {
"month": {5: 'May', 6: 'June', 7:'July', 8:'Aug', 9:'Sep'}
}
month_file = clean_file.replace(cleanup_nums)
