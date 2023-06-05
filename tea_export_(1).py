# -*- coding: utf-8 -*-
"""Tea_export (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UAzfuXLFIMXyNqaqKW88JSLOvT8sKGsC
"""

# import necessary lbraries

import  pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

# load the dataset

df = pd.read_excel('/content/Tea Export.xlsx')

df.head()

df

# Preprocessing steps to fill the null values by using Mean and median

df.isnull().sum()



# To fill the null values by using the median
for x in df.columns:
  if (np.dtype(df[x])== 'float' or (np.dtype(df[x]))=='int64'):
    df[x] = np.where(df[x].isnull(),df[x].median(),df[x])

df.isnull().sum()

df.set_index(df['Year'],inplace = True)

df.head()

# based on the graphs which year has maixmum export in south india
df['Tea Export From South India'].plot()
plt.ylabel('Export')
plt.title('Export in south india ')

#Based on the graph which year has maximum year in the North India

df['Tea Export From North India'].plot()
plt.ylabel('Export')
plt.title('Export in North india')

# Based on the Graphs which year has maximum export in India

df['Tea Export From India'].plot()
plt.ylabel('Export')
plt.title('Export in India')

# As comparision which has maximum export happen in north or south india.

df[['Tea Export From South India','Tea Export From North India']].plot(kind='bar',figsize=(10,10))

