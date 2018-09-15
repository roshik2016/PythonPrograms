# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:11:32 2017

@author: roshi
"""
import pandas as pd 
df=pd.read_csv("world_population.csv")
print(df)

new_lables= ("Year of population","World Population")
df2=pd.read_csv('world_population.csv',header=0,names=new_lables)
print(df2)