# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:35:15 2021

@author: Роман
"""


def my_func(num1,num2):
    
    final_num=num1
    i=1
    while i < abs(num2):
        final_num=final_num*num1
        i=i+1
        
    return 1/final_num


print(my_func(2,-4))
print(2**(-4))