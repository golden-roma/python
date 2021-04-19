# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 14:41:00 2021

@author: Роман
"""


class OwnError(ValueError):
    def __init__(self, txt):
        self.txt = txt
        

num_list=[]    



while True:
    
    num=input('Введите элемент списка: ')
    
    if num.lower()=='stop':
        break
    else:
        try:
            num=int(num)
        except ValueError:
            print("Вы ввели не число!")
        else:
            num_list.append(num)
            print(num_list)
            

    
