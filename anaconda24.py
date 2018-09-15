# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 12:20:25 2017

@author: roshi
"""

import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv('car.csv')

df.plot(kind='scatter',x='distance traveled',y='starting point')

plt.title("Analysis of Relationship between Distance Traveled and Starting Point")

plt.xlabel('Total Distance Travelled')
plt.ylabel('Car Starting Point')

plt.show()
