# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 11:26:59 2021

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

# loc vs iloc
# indexing using labels vs indexing using position
# select row with index 'Nauru' and the 'Population' column
capitals.loc['Nauru', 'Population']

# the same selection using bracket notation
capitals['Population']['Nauru']

# Slicing rows and Selecting multiple columns
capitals.loc['Palau':'Nauru',['Population', 'Percentage']]
# alternative
capitals[['Population', 'Percentage']]['Palau':'Nauru']


# Selecting specific rows
capitals.loc[['San Marino', 'Vatican City']]
# no alternative exists for this one

# fifth row and second row, all columns starting with the second
capitals.iloc[[4,1], 1:]

# all rows and the third column (zero-based index)
capitals.iloc[:,2]
