# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 09:58:12 2021

@author: jeff
"""

import pandas as pd

athletes = pd.read_csv('athletes.csv')
athletes.info()

# determine if a row is a duplicate
athletes.duplicated()
# show whether or not a DataFrame has duplicate rows
athletes.duplicated().any()

# return DataFrame with the duplicate rows
athletes[athletes.duplicated()]

athletes.drop_duplicates(inplace=True)

# show unique nationalities
athletes['nationality'].drop_duplicates()
athletes['nationality'].drop_duplicates().sort_values()

# show unique nationalities with number of occurences
athletes['nationality'].value_counts()
athletes['sex'].value_counts()
