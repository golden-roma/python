# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 23:13:10 2021

@author: Роман
"""

from itertools import count,cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)
        
print('----')

num_list=[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

с = 0
for el in cycle(num_list):
    if с > 20:
        break
    print(el)
    с += 1