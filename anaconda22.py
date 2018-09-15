# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:48:12 2017

@author: roshi
"""

import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv('temp.csv')

#df.plot()
#plt.show()

#df.plot(subplots=True)
#plt.show()

#plotting line with 1 column
column_list1 = ['vapPress']

print(df[['vapPress']])

df[column_list1].plot()
plt.show()

#plotting line with 2 column
column_list2 = ['tempDiff','BtempDiff']

print(df[['vapPress']])

df[column_list2].plot()
plt.show()
