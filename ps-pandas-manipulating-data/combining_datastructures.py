# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 11:24:02 2021

@author: jeff
"""

import pandas as pd

grades = pd.DataFrame([[6,4,5], [7,8,7], [6,7,9], [6,5,5], [5,2,7]],
                      index=['Mary','John','Ann','Pete','Laura'],
                      columns=['test_1','test_2','test_3'])
grades

# adding a new column to a DataFrame by adding a Series
grades['test_4'] = pd.Series({'John': 5, 'Ann': 8, 'Pete': 9, 'Mary': 7, 'Laura': 10})
grades

# adding a new row using loc
grades.loc['Bob'] = [2,3,4,5]
grades

# appending a series to a DataFrame as a row
# Series must have a name which will be used as the index
new_row = pd.Series({'test_1': 5, 'test_2': 6, 'test_3': 7, 'test_4': 8}, name='Kim')
grades.append(new_row)

grades['stud_nr'] = [113, 121, 123, 135, 139, 141]
grades = grades[['stud_nr', 'test_1', 'test_2', 'test_3', 'test_4']]
grades


other = pd.DataFrame([[139,7,7],
                      [123,8,6],
                      [142,8,6],
                      [113,7,9],
                      [155,10,9],
                      [121,6,4]],
                     columns=['stud_nr','exam1','exam2'])
other

# merge a DataFrame with another DataFrame
# default is 'inner' where matching indexes can be found in both DataFrames
grades.merge(other)
# returns a new DataFrame with values from both DataFrames only if
# the matching index is in the primary
grades.merge(other, how='left')
# returns a new DataFrame with values from both DataFrames only if
# the matching index is in the secondary
grades.merge(other, how='right')
# returns a new DataFrame with values for all cells from both DataFrames
grades.merge(other, how='outer')





























