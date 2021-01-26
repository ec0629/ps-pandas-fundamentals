# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 13:12:50 2021

@author: jeff
"""

import pandas as pd
import numpy as np
import os

# Load data from pickle created in CSV import script
df = pd.read_pickle(os.path.join('.', 'data_frame.pickle'))

# Iteration over grouped data
small_df = df.iloc[49980:50019, :].copy()
grouped = small_df.groupby('artist')
type(grouped)

for name, group_df in grouped:
    # name is the value of the characteristic the DataFrame has been grouped by
    print(name)
    # the DataFrame for the grouping
    print(group_df)
    # we are only showing the first group for brevity
    # remove the break statement to show all iterations
    break

# Aggregation
# Min
for name, group_df in small_df.groupby('artist'):
    min_year = group_df['acquisitionYear'].min()
    print("{}: {}".format(name, min_year))
    
# Transformation

# Emulate missing data in small_df
small_df.loc[16441, 'medium'] = np.nan
small_df.loc[11838, 'medium'] = np.nan

def fill_values(series):
    values_counted = series.value_counts()
    if values_counted.empty:
        return series
    most_frequent = values_counted.index[0]
    new_medium = series.fillna(most_frequent)
    return new_medium

def transform_df(source_df):
    group_dfs = []
    for name, group_df in source_df.groupby('artist'):
        filled_df = group_df.copy()
        filled_df.loc[:, 'medium'] = fill_values(group_df['medium'])
        group_dfs.append(filled_df)
    
    new_df = pd.concat(group_dfs)
    return new_df

filled_df = transform_df(small_df)


# Performing the same operations as above
# using built-in methods

# Fill missing values
# Emulate missing data in small_df
small_df.loc[16441, 'medium'] = np.nan
small_df.loc[11838, 'medium'] = np.nan

grouped_mediums = small_df.groupby('artist')['medium']
small_df.loc[:, 'medium'] = grouped_mediums.transform(fill_values)

# Min
df.groupby('artist').agg(np.min)
df.groupby('artist').min()

# Filter
grouped_titles = df.groupby('title')
title_counts = grouped_titles.size().sort_values(ascending=False)
    
    
condition = lambda x: len(x.index) > 1
dup_titles_df = grouped_titles.filter(condition)
dup_titles_df.sort_values('title', inplace=True)