# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 12:52:24 2017

@author: roshi
"""

import matplotlib.pyplot as plt
list_pop = []
for i in range(5):
    list_pop.append(i)
list_pop=[2,6,8,10,11]
lst_year=[2000,2001,2002,2003,2004]
print(lst_year[-1])
print(list_pop[-1])
plt.plot(lst_year,list_pop)
plt.xticks(lst_year,['2000','2001','2002','2003','2004'])
plt.yticks(list_pop,['2','6','8','10','11'])
