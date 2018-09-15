# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 13:13:15 2017

@author: roshi
"""

import matplotlib.pyplot as plt

lst_life_exp = [30,40,50,60,70,80]
lst_gdp_cap=[10000,20000,30000,40000,50000,60000]
plt.scatter(lst_life_exp,lst_gdp_cap)
plt.xscale('log')
plt.show()