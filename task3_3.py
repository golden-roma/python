# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:21:42 2021

@author: Роман
"""

def my_func(num1,num2,num3):
    num_list=[num1,num2,num3]
    num_list.remove(min(num_list))
    sum_result=sum(num_list)
    return sum_result


print(my_func(6,8,2))