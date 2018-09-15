# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 14:20:13 2017

@author: roshi
"""

import numpy as np 
import matplotlib.pyplot as plt

life_exp=[30,40,50,60,70,80]
gdp_cap=[10000,20000,30000,40000,50000,60000]

pop=[14,2,6,8,10,12]
np_pop = np.array(pop)
np_pop_size = np_pop*2
plt.scatter(gdp_cap,life_exp,s=pop)
plt.xlabel('GDP per capita in USD')
plt.ylabel('Life expectancy in years')
plt.title('World Development Information')
plt.show()