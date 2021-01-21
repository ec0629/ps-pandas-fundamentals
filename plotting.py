# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 13:29:26 2021

@author: jeff
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib import rcParams

df = pd.read_pickle(os.path.join('data_frame.pickle'))
acquisition_years = df.groupby('acquisitionYear').size()

# Simplest default plot
# acquisition_years.plot()


# Set fonts
title_font = {
    'family': 'source sans pro',
    'color': 'darkblue',
    'weight': 'normal',
    'size': 20,
    }

labels_font = {
    'family': 'consolas',
    'color': 'darkred',
    'weight': 'normal',
    'size': 16,
    }

rcParams.update({
    'figure.autolayout': True,
    'axes.titlepad': 20})

fig = plt.figure()

subplot = fig.add_subplot(1, 1, 1)
# rotating labels on the x-axis 45 degrees
# use logarithmic scale on y-axis
# add grid behind graph
acquisition_years.plot(ax=subplot, rot=45, logy=True, grid=True)
subplot.set_xlabel("Acquisition Year", fontdict=labels_font, labelpad=10)
subplot.set_ylabel("Artworks Acquired", fontdict=labels_font)
subplot.set_title("Title Gallery Acquisitions", fontdict=title_font)
# increase the number of tick marks on the x-axis
subplot.locator_params(nbins=40, axis='x')
# Since this is an interactive plot needed to change the following setting:
# Tools -> Preferences -> IPython console -> Graphics -> Backend: Automatic
# Then restart the kernel
fig.show()

# Save to files
fig.savefig('plot.png')
fig.savefig('plot.svg', format='svg')
