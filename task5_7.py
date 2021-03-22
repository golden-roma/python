# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:51:52 2021

@author: Роман
"""

import json

with open("firms.txt",encoding="utf-8") as f_obj:
    f_text=f_obj.readlines()
    tot_revenue=0
    amount=0
    firms_info=[]
    list_of_firms={}
    for el in f_text:
        el=el.replace('\n','')
        firm=el.split(' ')
        firm_revenue=float(firm[2])-float(firm[3])
        if firm_revenue>0:
            tot_revenue+=firm_revenue
            amount+=1
            list_of_firms[firm[0]]=firm_revenue
            
    avg_revenue={'average_profit':(tot_revenue/amount)}
    
    firms_info.append(list_of_firms)
    firms_info.append(avg_revenue)
    
print(avg_revenue)
print(firms_info)

with open('firms_info.json','w') as j_obj:
    json.dump(firms_info,j_obj)
    
