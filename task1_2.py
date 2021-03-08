# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 13:21:33 2021

@author: Роман
"""


answer=int(input('Введите время в секундах:'))

an_hours=answer//3600
an_minutes=(answer-(an_hours*3600))//60
an_seconds=(answer-(an_hours*3600)-(an_minutes*60))
print(f'Общее время: {an_hours} чч {an_minutes} мм {an_seconds} cc')