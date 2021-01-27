# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 07:56:04 2021

@author: jeff
"""

import pandas as pd

athletes = pd.read_csv('athletes.csv')
athletes.info()

athletes.plot.scatter(x='height', y='weight')

heights = athletes['height']
heights.plot.box()

# bottom edge of box in boxplot
q1 = heights.quantile(.25)
# top edge of box in boxplot
q3 = heights.quantile(.75)
# space inside the boxplot
iqr = q3 - q1

# calculate whiskers of boxplot
pmin = q1 - 1.5 * iqr
pmax = q3 + 1.5 * iqr
nwh = heights.where(heights.between(pmin, pmax))

compare = pd.DataFrame({'before': heights, 'after': nwh})
compare.plot.box()
compare.describe()

heights.where(heights.between(pmin, pmax), inplace=True)

athletes.plot.scatter(x='height', y='weight')
