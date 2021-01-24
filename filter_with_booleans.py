# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 12:29:17 2021

@author: jeff
"""

import pandas as pd

capitals = pd.DataFrame(
    [
     ['Ngerulmud',391,1.87],
     ['Vatican City',826,100],
     ['Yaren', 1100,10.91],
     ['Funafuti',4492,45.48],
     ['City of San Marino',4493],
    ],
    index=['Palau', 'Vatican City', 'Nauru', 'Tuvalu', 'San Marino'],
    columns=['Capital', 'Population', 'Percentage'])

# we can filter data by passing in a list of booleans to the index operator
capitals[[True, True, False, True, False]]
# this will display the rows with the same position as a True value in the list

# we can leverage this by combining it with DataFrame logical operators
capitals['Percentage'] > 25
# the above returns a series with Boolean values for each row and whether it passes the logical test

# we can then select the rows passing this test by combining the above
capitals[capitals['Percentage'] > 25]


grades = pd.DataFrame([[6,4], [7,8], [6,7], [6,5], [5,2]],
                      index=['Mary', 'John', 'Ann', 'Pete', 'Laura'],
                      columns=['test_1', 'test_2'])
grades

# we can also the value in one column with the value in another and receive a Series as a return
# students with scores in second test lower or equal to first
grades['test_2'] <= grades['test_1']
grades[grades['test_2'] <= grades['test_1']]

# by combining with loc we can also perform filtering on columns
grades.mean() > 5.5
# will return a series with columns whose aggregate value pass the boolean expression
grades.loc[:, grades.mean() > 5.5]
# we only return columns related to tests that have a mean greater than 5.5