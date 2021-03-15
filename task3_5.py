# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:56:22 2021

@author: Роман
"""



tot_sum=0
while True:
    nums=input('Введите строку чисел или символ: ')
    if (nums.upper()=='Q'): 
        break
    else:
        nums_list=nums.split()

        for num in nums_list:
            tot_sum+=int(num) 
   
        print(f'Итоговая сумма: {tot_sum}')
        
print(f'Итоговая сумма: {tot_sum}')

