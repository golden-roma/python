# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:33:34 2021

@author: Роман
"""


from sys import argv

script_name, hours, salary_per_hour, bonus = argv

def get_tot_salary(hours,salary_per_hour, bonus):
    result=(float(hours)*float(salary_per_hour))+float(bonus)
    return result

print('Итоговая зарплата: {}'.format(get_tot_salary(hours, salary_per_hour, bonus)))
