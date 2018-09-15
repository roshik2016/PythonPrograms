# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 12:38:45 2017

@author: roshi
"""

import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv('car.csv')

#summary Statistics
print(df['distance traveled'].min())

print(df['distance traveled'].max())

print(df['distance traveled'].mean())

print(df['distance traveled'].std())
#mean=df.mean(axis='columns')
#mean.plot()
#plt.show()

print(df['distance traveled'].describe())