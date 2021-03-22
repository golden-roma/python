# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 23:20:10 2021

@author: Роман
"""


with open('employees.txt',encoding="utf-8") as f_obj:
    f_text=f_obj.readlines()
    salaries=[]
    for el in f_text:
        el=el.replace('\n', '')
        salary=float(el[el.index(' ')+1:])
        if salary<20000:
            salaries.append(salary)
            print(el)
    avg_salary=round(sum(salaries)/len(salaries),2)
    print(avg_salary)