# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:15:51 2021

@author: jeff
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('water.csv')
df.info()

df.plot()
ax = df.plot(subplots=True, title="Water measurements off the Dutch coast.")

ax = df['temp'].plot(title="Water temperature")

df['datetime'] = pd.to_datetime(df['datetime'])
df.info()

ax = df.plot(title="Water temperature", x="datetime", y="temp")

df['temp'].plot.hist()
df['temp'].plot.box()

df = pd.read_csv('nobel.csv')
df.head()

prizes_countries = df['Country'].value_counts()
prizes_countries.plot.pie()

top_countries = prizes_countries[:10]
ax = top_countries.plot.bar(title="Top Nobel Prize Winning Countries")
