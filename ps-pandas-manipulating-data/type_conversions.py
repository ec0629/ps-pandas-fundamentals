# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:19:35 2021

@author: jeff
"""

import pandas as pd

athletes = pd.read_csv('athletes.csv')
# object data type implies they are a string
athletes.info()

# medal count has been import as string type but should hold ints
athletes[['gold', 'silver', 'bronze']].head()

# type conversion fails because a O is incorrectly included instead of a 0
athletes['bronze'].astype(int)

# row with index 7521 is the offending row
athletes[athletes['bronze'] == 'O']

# correct the row
athletes.loc[7521, ['gold', 'silver', 'bronze']] = 0
# retry type conversion
athletes[['gold', 'silver', 'bronze']] = athletes[['gold', 'silver', 'bronze']].astype(int)

athletes[['gold', 'silver', 'bronze']].sum()
athletes.info()
# weight column rounds to the nearest kg and therefore
# is probably best as an integer instead of float but
# weight column has nulls and therefore must be a float
# since float/object are the only types that allow null