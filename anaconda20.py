# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:23:29 2017

@author: roshi
"""

import pandas as pd 
#df1=pd.read_csv("file_messy.csv")

#print(df1.head())

df2=pd.read_csv('file_messy.csv',delimiter=' ',header=None,comment='#')
print(df2.head())

df2.to_csv('file_messy.csv',index=False)

df2.to_excel('file_clean.xlsx',index=False)