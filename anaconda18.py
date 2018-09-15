# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:01:18 2017

@author: roshi
"""

import pandas as pd 

cars=pd.read_csv('cars.csv')

#print(cars['Origin'])

#print(cars[['Origin','Model']])

print(cars[0:4])