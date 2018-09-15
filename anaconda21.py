# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:42:51 2017

@author: roshi
"""

import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('temp.csv')

df.plot(color='red')

plt.title('Temperature Data')

plt.ylabel('Index')

plt.show()