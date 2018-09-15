# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 13:59:04 2017

@author: roshi
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 13:13:15 2017

@author: roshi
"""

import matplotlib.pyplot as plt

lst_life_exp = [30,40,50,60,70,80]
lst_gdp_cap=[10000,20000,30000,40000,50000,60000]
plt.plot(lst_gdp_cap,lst_life_exp)
xlab='Life Expentancy'
ylab='GDP Capital'
title='GDP comparison'
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)
plt.show()