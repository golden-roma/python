# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:28:47 2021

@author: Роман
"""


"""list_seasons = ['зима','весна','лето','осень']

list_month=int(input('Введите номер месяца в виде числа: '))


if list_month in (12,1,2):
    list_result=list_seasons[0]
elif list_month in (3,4,5):
    list_result=list_seasons[1]
elif list_month in (6,7,8):
    list_result=list_seasons[2]
elif list_month in (9,10,11):
    list_result=seasons[3]

print(f'Ваше время года: {list_result}')
"""
dict_seasons={'зима':[1,2,12],'весна':[3,4,5],'лето':[6,7,8],'осень':[9,10,11]}


dict_month=int(input('Введите номер месяца в виде числа: '))



for key,value in (dict_seasons.items()):
    if dict_month in value:
        dict_result=key
        
print(f'Ваше время года: {dict_result}')