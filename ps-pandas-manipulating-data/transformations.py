# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:16:24 2021

@author: jeff
"""

import numpy as np
import pandas as pd

df = pd.DataFrame(np.ones([5,4]), columns=['a','b','c','d'])
df

# mathematical operation on each element
df * 2
# mathematical operation on each element but in place
df *= 2

# mathematical operation on a row
df.loc[1] /= 2

df2 = pd.DataFrame(np.ones([3,2]), columns=['d','e'], index=[2,4,5])
df2

# element-wise math operations on two data sets
# pandas will try and match the same index and column label
df + df2

# row-wise operation
df.loc[2] * df2.loc[5]

df.mean()
df - df.mean()

# Subtracting a Series from a DataFrame
# will subtract the series from each row in the DataFrame
df - pd.Series({'a': 5, 'b': 5, 'e': 5, 'f': 5})

# mean for each row
df.mean(axis=1)
df.sub(df.mean(axis=1), axis=0)


# Applying Functions
df = pd.DataFrame({'sin': np.arange(0, 5*np.pi, 0.01),
                   'cos': np.arange(0.5*np.pi, 5.5*np.pi, 0.01)})
df

# np.sin is a global function and will apply to each cell in the DataFrame
df = np.sin(df)
df.plot()

# function to be applied column-wise
def iqr(col):
    q1 = col.quantile(.25)
    q3 = col.quantile(.75)
    return q3 - q1

df.apply(iqr)
# we could also apply a function row-wise by providing axis=1 option
# df.apply(iqr, axis=1)

# function to be applied to every cell
def somefunc(x):
    return np.abs(x+.25)

df.applymap(somefunc).plot()
