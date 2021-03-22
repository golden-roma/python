# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:14:02 2021

@author: Роман
"""


num_list=[el for el in range(1,35) if el%3==0]

num_str=''
for el in num_list:
    num_str+=str(el)+' '

num_str=num_str[0:-1]

with open("nums_with_nbsp.txt",'w+') as f_obj:
    f_obj.write(num_str)
    f_obj.seek(0)
    sum_of_nums=0
    res_str=f_obj.readline()
    
    res_list=res_str.split(' ')
    #res_list.remove('')
    for el in res_list:
        el=float(el)
        sum_of_nums+=el
    
print(res_list)
print(f'Сумма числе в файле = {sum_of_nums}')