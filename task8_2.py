# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 23:35:43 2021

@author: Роман
"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
        
        

x, y = input("Введите делимое и делитель: ").split()

try:
    x=int(x)
    y=int(y)
    #res=x/y
    if y==0:
        raise OwnError('Вы ввели нуль, а деление на нуль запрещено!')
    
except ValueError:
    print("Вы ввели не число!")
except OwnError as err:
    print(err)
else:
    res=x/y
    print(res)