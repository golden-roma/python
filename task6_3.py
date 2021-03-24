# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:55:01 2021

@author: Роман
"""


class Worker:
    
    def __init__(self,name,surname,position,wage,bonus):
        self._worker_name=name
        self._worker_surname=surname
        self._worker_position=position
        self._worker_income={'wage':float(wage),'bonus':float(bonus)}
        
        
class Position(Worker):
    
    def get_full_name(self):
        self.__full_name=self._worker_name+' '+self._worker_surname
        print(f'Employee\'s full name: {self.__full_name}, position: {self._worker_position}')
    
    def get_total_income(self):
        self.__total_income=sum(self._worker_income.values())
        print(f'Employee\'s total income: {self.__total_income}')
    
pos1=Position('Michael','Jordan','CEO',300000,50000)

pos1.get_full_name()
pos1.get_total_income()

pos2=Position('Michael','Phelps','Swimmer',250000,41116)

pos2.get_full_name()
pos2.get_total_income()