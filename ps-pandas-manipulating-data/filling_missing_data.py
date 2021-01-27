# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:09:10 2021

@author: jeff
"""

import pandas as pd

df = pd.read_csv('weather_m4.csv')
df.info()

# WEATHER_CODE does not provide meaningful data and can be removed from the DF
df.drop(columns='WEATHER_CODE', inplace=True)

# return new Series replace null with a default value
df['MIN_TEMP_GROUND'].fillna(0)

# return new Series and replace nulls with the previous non-null value
df['MIN_TEMP_GROUND'].fillna(method='ffill')

# replace nulls with the next non-null value
df['MIN_TEMP_GROUND'].fillna(method='bfill', inplace=True)

df.isnull().any()

# display rows with any null values
df[df.isnull().any(axis=1)]

# display 'YYYYMMDD' column for rows with null values
df.loc[df.isnull().any(axis=1), 'YYYYMMDD']

# dispaly aggregate count of rows with null values by day
df.loc[df.isnull().any(axis=1), 'YYYYMMDD'].value_counts()

# drop rows with null values
df.dropna()
# drop columns with null values
df.dropna(axis=1)
nulls_dropped = df.dropna()
nulls_dropped.info()

# drop rows with 7 null values
drop_thresh = df.dropna(thresh=7)
drop_thresh[drop_thresh.isnull().any(axis=1)]

rows_to_fill = df.isnull().any(axis=1)
df[rows_to_fill]

nulls_filled = df.fillna(df.mean())
nulls_filled[rows_to_fill]

df.fillna(df.mode().iloc[0], inplace=True)
