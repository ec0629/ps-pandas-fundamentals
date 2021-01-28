# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 09:59:19 2021

@author: jeff
"""

import pandas as pd

athletes = pd.read_csv('athletes_m6.csv')
m = pd.read_csv('monthly_data.csv')
m
m.set_index('YYYY', inplace=True)
m
# The stack function will make the columns into a
# second layer index column under the existing index
# this differs from groupby because the column label
# becomes the second layer index instead of the column value
m.stack()
# now we can aggregate ALL values since
# we now have a single column
m.stack().sum()

w = athletes.groupby(['sport', 'sex'])['weight'].mean()
w
# unstack function will take the deepest index column and
# turn those values into columns
w.unstack()
