# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 22:57:24 2021

@author: Роман
"""


from functools import reduce

def get_multiplication(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el

num_list=[x for x in range(100,1001) if x%2==0]

print(num_list)
fin_result=reduce(get_multiplication, num_list)
print(fin_result)

tot_sum=1
for x in range(100,1001):
    if x%2==0:
        tot_sum*=x
    
#print(tot_sum==fin_result)