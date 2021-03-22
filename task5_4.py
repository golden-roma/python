# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:49:26 2021

@author: Роман
"""


with open('nums.txt',encoding="utf-8") as fr_obj:
    f_text=fr_obj.readlines()
    
with open('nums_new.txt','w+',encoding="utf-8") as fw_obj:
    for el in f_text:
        if(el.find('One')!=-1):
            el=el.replace('One','Один')
        elif(el.find('Two')!=-1):
            el=el.replace('Two','Два')
        elif(el.find('Three')!=-1):
            el=el.replace('Three','Три')
        elif(el.find('Four')!=-1):
            el=el.replace('Four','Четыре')
        fw_obj.write(el)
        
    fw_obj.seek(0)
    result=fw_obj.read()

#str='One 34243 try'
#print(str.find('34'))
print(result)
        
