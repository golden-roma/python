# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 23:22:08 2021

@author: Роман
"""


def fact(num):
    fin_result=1
    for x in range(num+1):
        if x==0:
            continue
        fin_result*=x
        yield fin_result
        

for el in fact(6):
    print(el)