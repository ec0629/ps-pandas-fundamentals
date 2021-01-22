# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 08:29:13 2021

@author: jeff
"""

import numpy as np
import pandas as pd

df = pd.read_csv('weather.csv').head()
df

# We can reference a column using its label
df['TEMP']

# best practice is to avoid using dot notation
# as has the limitations
df.TEMP

# We cannot reference a column using positional index
df[2]

# label referencing is type sensitive
# for example if we transpose the dataframe
dft = df.T
dft
dft.columns

# We cannot reference column with label 2
# with a string
dft['2']

# We need to reference it using an integer
dft[2]

# Rows can be positional referenced however
df['TEMP'][1]
dft[2]['TIME'] # valid
dft[2][2] # valid

t = pd.DataFrame([['John'], ['Bob'], ['Anne']], index=[4,3,4])
t
# selecting using index value overrides position
# since indexes are integers in this case
t[0][4]


# INDEXING USING LISTS
# On a DataFrame using lists to select multiple columns
df[['PRESSURE', 'TIME', 'TEMP']]
dft[3:][[2,3]]

# On a series using lists will select specific rows in that order
df['TIME'][[3,1,4]]

# Slice notation on a DataFrame will also reference rows
df[2:4]

# Slicing on a DataFrame returns a DataFrame
df[2:4][['TEMP', 'PRESSURE']]

# Slicing on a Series also selects rows
df['PRESSURE'][:4]

dft[:2]
dft['TIME':'PRESSURE']






















