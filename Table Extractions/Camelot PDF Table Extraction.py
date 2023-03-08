#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Example with foo.pdf

import camelot

tables = camelot.read_pdf('foo.pdf', pages='1', flavor='lattice')
print(tables)

tables.export('foo.csv', f='csv', compress=True)
tables[0].to_csv('foo.csv')  # to a csv file, 0 is the first table on page, goes up from there
print(tables[0].df)  # to a df

