"""
Horizontal Stacking
"""

import pandas as pd

# Creating dataframe a
a = pd.DataFrame()
  
# Creating Dictionary
d = {'id': [1, 2, 10, 12],
     'val1': ['a', 'b', 'c', 'd']}
  
a = pd.DataFrame(d)
  
# Creating dataframe b
b = pd.DataFrame()
  
# Creating dictionary
d = {'id': [1, 2, 9, 8],
     'val1': ['p', 'q', 'r', 's']}
b = pd.DataFrame(d)

df = pd.merge(a, b, on='id', how = 'inner')
df = pd.merge(a, b, on='id', how = 'right')
df = pd.merge(a, b, on='id', how = 'left')
df = pd.merge(a, b, on='id', how = 'outer')
