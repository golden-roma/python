# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 22:11:46 2021

@author: Роман
"""


num_list=[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [num_list[x] for x in range(len(num_list)) if num_list[x]>num_list[x-1] and x!=0]

print(new_list)