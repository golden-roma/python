# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 13:41:38 2021

@author: Роман
"""


num=int(input('Введите целое положительное число: '))

#print(7//10)

max_num=0

while True:
    if((num%10)==9):
        max_num=9
        break
    if((num%10)>max_num):
        max_num=num%10
    #print(num%10)
    num=num//10
    if (num)==0:
        break
    
print(f'Самая большая цифра в числе: {max_num}')

    
