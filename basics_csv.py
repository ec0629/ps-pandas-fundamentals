# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 10:34:30 2021

@author: jeff
"""

import pandas as pd
import os

CSV_PATH = os.path.join(
    '.',
    'artwork_data.csv'
)

# Limit rows
df = pd.read_csv(CSV_PATH, nrows=5)

# Specify id column as the index column
df = pd.read_csv(CSV_PATH, nrows=5,
                 index_col='id')

# Limit columns
df = pd.read_csv(CSV_PATH, nrows=5,
                 index_col='id',
                 usecols=['id', 'artist'])

# Columns of interest
COLS_TO_USE = ['id', 'artist',
               'title', 'medium', 'year',
               'acquisitionYear', 'height',
               'width', 'units']

df = pd.read_csv(CSV_PATH,
                 usecols=COLS_TO_USE,
                 index_col='id')

df.to_pickle(os.path.join('.', 'data_frame.pickle'))
