# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 13:26:58 2021

@author: Роман
"""


num_list=[1,9,3,4,1,6,2]

print(num_list)
user_num=int(input('Введите целое число: '))

num_list.append(user_num)
num_list.sort(reverse=True)


print(num_list)