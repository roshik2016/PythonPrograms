# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 12:21:04 2017

@author: roshi
"""

import pandas as pd 

names =['United States','Australia','Japan','Egpyt']

dr = [True,False,False,False]

veh=[800,725,550,385]

country_dict={'country':names,'driving_rule':dr,'veh_per_thous':veh}

cars=pd.DataFrame(country_dict)

print(cars)