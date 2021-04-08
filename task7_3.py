# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:48:38 2021

@author: Роман
"""


class Cell:
    
    def __init__(self,cells_amount):
        self._cells_amount=int(cells_amount)
        
    def __add__(self,other):
        return self._cells_amount+other._cells_amount
    
    def __sub__(self,other):
        if self._cells_amount-other._cells_amount>0:
            return self._cells_amount-other._cells_amount
        else:
            return 'Разница не больше нуля!'
    
    def __mul__(self,other):
        return self._cells_amount*other._cells_amount
    
    def __truediv__(self,other):
        return round(self._cells_amount/other._cells_amount)
    
    def make_order(self,cells_per_row):
        result_str=''
        for i in range(self._cells_amount):
            
            if (i+1)%cells_per_row==0 and i!=self._cells_amount-1:
                result_str+='*\\n'
            else:
                result_str+='*'
        return result_str                

cell1=Cell(33)
print(cell1.make_order(7))
    

cell2=Cell(13)
print(cell1+cell2)
print(cell1-cell2)
print(cell1*cell2)
print(cell1/cell2)

print(cell2.make_order(5))