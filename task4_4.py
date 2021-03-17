# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 22:49:02 2021

@author: Роман
"""



num_list=[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list=[el for el in num_list if num_list.count(el)<=1]

print(new_list)
