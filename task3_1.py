# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 15:14:44 2021

@author: Роман
"""

#n1=9
#n2=3

def my_func(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
    
num1=int(input('Введите первое число: '))
num2=int(input('Введите второе число: '))
print(my_func(num1,num2))