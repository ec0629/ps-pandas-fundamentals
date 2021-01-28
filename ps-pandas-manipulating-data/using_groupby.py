# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 08:11:36 2021

@author: jeff
"""

import pandas as pd

athletes = pd.read_csv('athletes_m6.csv')
athletes.info()

# we can break this DataFrame into smaller DataFrame based on a data point
# this will create a separate DataFrame for each unique nationality
g = athletes.groupby('nationality')[['gold','silver','bronze']]
g.sum()

g = athletes.groupby('sport')[['weight', 'height']]
# calculate mean weight and height by sport
g.mean()

# We can DataFrames into smaller components by passing multiple columns
g = athletes.groupby(['sport', 'sex'])[['weight', 'height']]
# calculate mean weight and height by sport
g.mean()
