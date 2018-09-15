# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 12:29:00 2017

@author: roshi
"""

import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv('car.csv')

cols=['distance traveled','starting point']

df[cols].plot(kind='box',subplots=True)

plt.show()