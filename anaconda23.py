# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 12:08:05 2017

@author: roshi
"""

import pandas as pd 
import matplotlib.pyplot as plt 

df=pd.read_csv('stock.csv')

column_list2 = ['Jan','Feb']

plt.title('Monthly Stock Prices')

plt.ylabel("Price is $US")

my_ticks_lab =[]
my_ticks_val =[]
plt.xticks(my_ticks_lab,my_ticks_val)

df[column_list2].plot()
plt.show()
