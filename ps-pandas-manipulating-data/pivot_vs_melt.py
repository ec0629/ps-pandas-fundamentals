# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 10:16:52 2021

@author: jeff
"""

import pandas as pd

p = pd.DataFrame({'id': [823905,823905,235897,235897,235897,983422,983422],
                  'item': ['price', 'unit', 'price', 'unit', 'stock', 'price', 'stock'],
                  'value': [3.49, 'kg', 12.89, 'l', 50, 0.49, 4]})
p

# pivot will combine multiple rows into a single
# row based on a common value column
# the first argument is the column that holds
# the connecting value
# the second argument is the column that holds
# the values we wish to convert to columns
p.pivot('id', 'item')


# Melt
grades = pd.DataFrame([[6,4,5], [7,8,7], [6,7,9], [6,5,5], [5,2,7]],
                      index=['Mary','John','Ann','Pete','Laura'],
                      columns=['test_1','test_2','test_3'])
grades

# Melt function will turn multiple columns into a single column
# by column labels into row values
grades.melt()
# we want to keep the student names and therefore we need to create
# a new index column
grades.reset_index(inplace=True)
grades
# id_vars is the column label that contains a group identifier
grades.melt(id_vars=['index'])
