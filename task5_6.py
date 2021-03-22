# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 14:29:53 2021

@author: Роман
"""


with open("subjects.txt",encoding="utf-8") as f_obj:
    f_text=f_obj.readlines()
    dict_subjects={}
    for el in f_text:
        source_el=el
        el=el[el.find(':')+2:]
        el=el.replace('(л)','')
        el=el.replace('(пр)','')
        el=el.replace('(лаб)','')
        el=el.replace('—','0')
        el=el.replace('\n','')
        subjects=el.split(' ')
        tot_sum=0
        for i in subjects:
            tot_sum+=int(i)
        dict_subjects[source_el[:source_el.find(":")]]=tot_sum
        
print(dict_subjects)