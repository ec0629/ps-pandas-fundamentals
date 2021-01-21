# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 08:41:56 2021

@author: jeff
"""

import pandas as pd
import os

df = pd.read_pickle(os.path.join('data_frame.pickle'))

small_df = df.iloc[49980:50019, :].copy()

# Basic Excel
small_df.to_excel('basic.xlsx')
small_df.to_excel('no_index.xlsx', index=False)
small_df.to_excel('columns.xlsx', columns=["artist", "title", "year"])

# writer = pd.ExcelWriter('multiple_sheets.xlsx', engine='xlsxwriter')
# small_df.to_excel(writer, sheet_name='Preview', index=False)
# df.to_excel(writer, sheet_name="Complete", index=False)
# writer.save()

with pd.ExcelWriter('multiple_sheets.xlsx') as writer:
    small_df.to_excel(writer, sheet_name='Preview', index=False)
    df.to_excel(writer, sheet_name="Complete", index=False)
    writer.save()

# Conditional formatting
artist_counts = df['artist'].value_counts()
artist_counts.head()

with pd.ExcelWriter('colors.xlsx') as writer:
    artist_counts.to_excel(writer, sheet_name="Artist Counts")
    sheet = writer.sheets['Artist Counts']
    cells_range = 'B2:B{}'.format(len(artist_counts.index))
    sheet.conditional_format(cells_range, {
        'type': '2_color_scale',
        'min_type': 'percentile',
        'max_value': '99',
        'max_type': 'percentile'})
    writer.save()