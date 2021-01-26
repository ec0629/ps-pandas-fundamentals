# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 07:30:44 2021

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

capitals

# sort by index, returns a new sorted DataFrame
capitals.sort_index()
# sort DataFrame in place
capitals.sort_index(inplace=True)
capitals

# sort DataFrame columns
capitals_sort_cols = capitals.sort_index(axis=1)
capitals_sort_cols

# Sort descending
capitals.sort_index(inplace=True, ascending=False)
capitals

# sort by column other than index
capitals.sort_values(by='Percentage', inplace=True)
capitals

# Sort by multiple columns
capitals.sort_values(by=['Population', 'Percentage'], inplace=True)
capitals
