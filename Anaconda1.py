# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 12:33:44 2017

@author: roshi
"""
import numpy as np
height = [2000,2200,2210,2300]
weight = [100,150,175,200]
np_height = np.array(height)
np_height = np_height * 0.0254
np_weight = np.array(weight)
np_weight = np_weight * 0.453592 
BMI = np_weight/np_height**2
print(BMI)