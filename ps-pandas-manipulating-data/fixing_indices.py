# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 11:55:18 2021

@author: jeff
"""

import pandas as pd

athletes = pd.read_csv('athletes.csv')
athletes.info()
athletes.head()
# the data set already has an id column
# so to use that as the index column we can
# do the following:
athletes.set_index('id', drop=True, inplace=True)
athletes.head()

athletes.rename(
    columns={'nationality': 'country', 'sport': 'discipline'},
    inplace=True)
athletes.head()


# example of resetting index values
# we will create gaps in the index values
# by dropping null rows first
df = pd.read_csv('weather_m4.csv')
df.dropna(inplace=True)
df.info()

df.reset_index(drop=True)
