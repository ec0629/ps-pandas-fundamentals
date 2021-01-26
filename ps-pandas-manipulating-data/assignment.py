# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 22:33:32 2021

@author: jeff
"""

import pandas as pd

def refreshDataFrame():    
    return pd.DataFrame([[6,4], [7,8], [6,7], [6,5], [5,2]],
                        index=['Mary', 'John', 'Ann', 'Pete', 'Laura'],
                        columns=['test_1', 'test_2'])

grades = refreshDataFrame()
grades

# increase the grades for Laura and John by 1 for test 2
grades.loc[['Laura', 'John'], 'test_2'] += 1

# increase test score for everyone by half a point
grades['test_1'] += 0.5

# add 2 points to each of Mary's test scores
grades.loc['Mary'] += 2

# explicitly set the values of Pete's test 1 and 2
grades.loc['Pete'] = [7,8]

# create DataFrame mapping cells to failing grades
failing = grades < 6
# create DataFrame mapping cells to passing grades
passing = grades >= 6
# for each cell that is true assign the value "Fail"
grades[failing] = "Fail"
# for each cell that is true assign the value "Pass"
grades[passing] = "Pass"

grades = refreshDataFrame()
# calculate student test average
# axis=1 means we are now performing operations row-wise
grades.mean(axis=1)
grades.mean(axis=1) > 6
# create and populate new column
grades['passed'] = grades.mean(axis=1) > 6
