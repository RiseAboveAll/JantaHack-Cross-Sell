#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


def outlier_detection(df,col):
    IQR=df[col].quantile(.75) - df[col].quantile(.25)
    upper_bound=df[col].quantile(.75) + (1.5*IQR)
    lower_bound=df[col].quantile(.75) - (1.5*IQR)
    df[col].clip(lower=lower_bound,upper=upper_bound,inplace=True)
    
    


# In[ ]:




