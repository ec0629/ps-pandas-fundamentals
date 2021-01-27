# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:20:30 2021

@author: jeff
"""

import pandas as pd

df = pd.read_csv('weather_m4.csv')
df.info()

# returns a DataFrame showing which cells have null values
df.isnull()

# returns a List if a column has ANY null values
df.isnull().any()

# returns a List if a row has ANY null values
df.isnull().any(axis=1)

# returns a DataFrame with the rows that have a null value
df[df.isnull().any(axis=1)]

# returns a List displaying if all the values in a column are null
df.isnull().all()

# returns a List displaying if all the values in a row are null
df.isnull().all(axis=1)

# Returns a scalar value if a row exists with all null values
df.isnull().all(axis=1).any()

# Returns a List displaying if all the value in each column is not null
df.notnull().all()

# determines if the MIN_TEMP_GROUND column in every 6th row is not null
every_6th_row = pd.Series(range(5, len(df), 6))
df['MIN_TEMP_GROUND'][every_6th_row].notnull().all()

# removes every 6th row from the DataFrame and checks for null values in MIN_TEMP_GROUND column
df['MIN_TEMP_GROUND'].drop(every_6th_row).isnull().all()
