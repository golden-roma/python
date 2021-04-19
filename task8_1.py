# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 12:03:39 2021

@author: Роман
"""


class MyDate:
    
    def __init__(self,user_date):
        self._user_date=user_date
        
    @classmethod
    def parse_date(cls,user_date):
        date_list=user_date.split('-')
        
        for i in range(len(date_list)):
            date_list[i]=int(date_list[i])
        
        return date_list
    
    @staticmethod
    def validate_date(user_date):
        date_list=MyDate.parse_date(user_date)
        
        validate_sum=0
        
        if date_list[0]>=1 and date_list[0]<=31:
            validate_sum+=1
        if date_list[1]>=1 and date_list[1]<=12:
            validate_sum+=1
        if date_list[2]>=2000 and date_list[2]<=2100:
            validate_sum+=1
        
        if(validate_sum==3):
            return 1
        else:
            return 0
        

date1=MyDate('05-03-2021')     

print(MyDate.parse_date('05-03-2021'))

print(MyDate.validate_date('31-12-2001'))
    
        
#str='05-03-2021'
#str=str.split('-')
#print(str)