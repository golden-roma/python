# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 23:03:53 2021

@author: Роман
"""


with open('text.txt') as f_obj:
        f_text=f_obj.readlines()
        #f_res=[el for el in f_text if el!='\n']
        i=1
        for el in f_text:
            print(f'Строка №{i}, кол-во символов: {len(el)-1}')
            i+=1