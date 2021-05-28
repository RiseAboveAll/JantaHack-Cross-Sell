#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


def missingValue_Treat(df,col):
    if df[col].dtypes.name=='object':
        df[col].replace(np.nan, df[col].value_counts().sort_values(ascending=False)[0],inplace=True)
    elif df[col].dtypes=='int64' or  df[col].dtypes=='int32':
        df[col].replace(np.NAN, -999,inplace=True)
    else:
        df[col].replace(np.NAN, -999.0,inplace=True)
        


# In[ ]:




