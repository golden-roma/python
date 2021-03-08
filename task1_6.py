# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:46:34 2021

@author: Роман
"""


first_km=int(input('Введите результат спортсмена в первый день: '))

expected_result=int(input('Введите ожидаемый результат: '))

result=first_km
run_day=1

while True:
    print(f'День №{run_day}, результат: {result}')
    if result>expected_result:
        print(f'Результат был достигнут на {run_day}')
        break
    result=result*1.1
    run_day=run_day+1