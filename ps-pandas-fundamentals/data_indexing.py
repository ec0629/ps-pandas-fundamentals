# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:11:38 2021

@author: jeff
"""

import pandas as pd
import os

# Load data from pickle created in CSV import script
df = pd.read_pickle(os.path.join('.', 'data_frame.pickle'))

# Demo 1 - Slicing data
artists = df['artist']
pd.unique(artists)
len(pd.unique(artists))

# Demo 2 - Filtering data
s = df['artist'] == 'Bacon, Francis'
s.value_counts()

# alternate method
artist_counts = df['artist'].value_counts()
artist_counts['Bacon, Francis']

# Demo 3 - Indexing data
# select artist column from row with id = 1035
df.loc[1035, 'artist']

# select the first row and the first column
# since the first row has the id 1035 and artist is the first column
# this returns the same thing as the index call above
df.iloc[0, 0]

# select first row and all of its columns
df.iloc[0, :]

# select first two columns of first two rows
df.iloc[0:2, 0:2]


# Demo 4 - Calculate painting area
# we can perform row-wise multiplication
# however, we must first clean the data since some rows 
# contain NaN values for their width/height

# force conversion of values to numeric type and then copy back into width column
df.loc[:, 'width'] = pd.to_numeric(df['width'], errors='coerce')

df.loc[:, 'height'] = pd.to_numeric(df['height'], errors='coerce')

area = df['height'] * df['width']
df = df.assign(area=area)

df['area'].max()
df['area'].idxmax()
df.loc[df['area'].idxmax(), :]
