# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 22:51:55 2021

@author: Роман
"""


str=input('Введите текст для файла: ')

f_text=str.split()

with open('text.txt','w') as f_obj:
    for el in f_text:
        f_obj.write(f'{el}\n')
    
