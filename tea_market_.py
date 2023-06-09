# -*- coding: utf-8 -*-
"""Tea Market .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkVzVO1R0L77zMDQDn9nCSIhLAqZkkRn
"""

import  pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

# Area under cultivation
df = pd.read_excel('/content/Area Under Tea Cultivation.xlsx')

df

# By treating that null values in each columns

df.isnull().sum()

# To fill the null values by using the median
for x in df.columns:
  if (np.dtype(df[x])== 'float' or (np.dtype(df[x]))=='int64'):
    df[x] = np.where(df[x].isnull(),df[x].median(),df[x])

df.isnull().sum()

df

df.set_index(df['Year'],inplace = True)

df.head()

df.sort_values('Area Under Tea In Tamil Nadu',inplace=True)

df.plot(kind='barh',y='Area Under Tea In Tamil Nadu',x='Year',color='b')

# In tamil nadu state 2006 has highest year of tea production

df.sort_values('Area Under Tea In Kerala',inplace=True)

df.plot(kind='barh',y='Area Under Tea In Kerala',x='Year',color='b')

# as per the graph kerala is the 2012 has highest production recorded in kerala

df.sort_values('Area Under Tea In Karnataka',inplace=True)
df.plot(kind='barh',y='Area Under Tea In Karnataka',x='Year',color='b')

# as per the graph 2015 has the highes crop prodcutin in Karnataka state

df.sort_values('Area Under Tea In South India',inplace=True)
df.plot(kind='barh',y='Area Under Tea In South India',x='Year',color='b')

# As per the graph 2011 has highest cultivation in South indian state

df.sort_values('Area Under Tea In India',inplace=True)
df.plot(kind='barh',y='Area Under Tea In India',x='Year',color='b')

# In 2011 the highes cultivation in India marker

df.head()

df.drop('Year',axis=1,inplace=True)

df.head()