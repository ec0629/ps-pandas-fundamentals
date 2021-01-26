# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 07:53:13 2021

@author: jeff
"""

import numpy as np
import pandas as pd

df = pd.read_csv('weather.csv')

# return number of rows and columns of dataframe
df.shape

# return metadata regarding dataframe
df.info()

# return first 5 rows by default
df.head()

# can change number of rows returned
df.head(50)

# return last rows
df.tail()

# returns a summary of statistical measures
df.describe()

# specific measures can be returned separately
df.mean()
df.max()

# we can also return statistical measures on a specific column
df['PRESSURE'].min()
df['TEMP'].mode()

# returns how many times a value is present
# in a Series
df['TEMP'].value_counts()

df['TEMP'].plot()
df['TEMP'].plot.hist()
# explicitly set the number of bins
# for histogram
df['TEMP'].plot.hist(bins=100)
