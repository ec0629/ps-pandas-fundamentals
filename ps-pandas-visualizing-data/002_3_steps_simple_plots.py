# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:45:08 2021

@author: jeff
"""

# Step one: prepare the script
import pandas as pd
import matplotlib.pyplot as plt

# Step two: prepare the data
grades = pd.DataFrame([[6,4,5], [7,8,8], [6,7,5], [6,5,7], [5,2,6]],
                      index=['Mary', 'John', 'Ann', 'Pete', 'Laura'],
                      columns=['test_1', 'test_2', 'test_3'])
grades

# Step three: just the appropriate chart function
ax = grades.mean().plot.bar(title="Average test score")

ax = grades.mean(axis=1).plot.barh(title="Average student score")

grades['average'] = grades.mean(axis=1)

grades.plot.barh(title="All test grades")

grades.loc['whole class'] = grades.mean()
grades

grades_t = grades.T
grades_t.drop(columns=['whole class'], inplace=True)
grades_t.drop('average', inplace=True)
grades_t

ax = grades_t.plot(title="Student progress")
