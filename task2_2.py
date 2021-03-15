# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 11:51:55 2021

@author: Роман
"""


#result_list = [2, 'text', 456, 45.3, None, True]

result_list=[]

list_length=int(input('Введите кол-во элементво в списке: '))

for list_el in range(list_length):
    el=input(f'Введите элемент №{list_el}: ')
    result_list.append(el)

#for el in result_list:
 #   print(el)

 

for el in range(1,len(result_list),2):
    temp_el=result_list[el-1]
    result_list[el-1]=result_list[el]
    result_list[el]=temp_el
    
print(result_list)