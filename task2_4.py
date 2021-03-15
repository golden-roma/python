# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:57:51 2021

@author: Роман
"""


str='Очень экстраординарный и интересный текст'

str_list=str.split()

for el in range(len(str_list)):
    print(f'Строка №{el}: {str_list[el][:10]}')