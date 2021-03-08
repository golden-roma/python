# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:02:15 2021

@author: Роман
"""


revenue=int(input('Введите выручку компании: '))
costs=int(input('Введите издержки компании: '))

if revenue<costs:
   print('Компания отработала в убыток!') 
elif revenue>costs:
    print('Компания отработала с выручкой!')
    print(f'Рентабильность выручки: {(revenue-costs)/revenue}')
    employee_amount=int(input('Введите кол-во сотрудников: '))
    print(f'Прибыль в расчете на одного сотрудника: {(revenue-costs)/employee_amount}')
else:
    print('Компания отработала в ноль!')
