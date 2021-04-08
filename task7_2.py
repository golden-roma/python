# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 20:59:04 2021

@author: Роман
"""

from abc import ABC,abstractmethod

class Clothing(ABC):
    
    @abstractmethod
    def get_tissue_consumption(self):
        pass
    
class Coats(Clothing):
    
    def __init__(self,size):
        self._size=float(size)
    
    @property
    def get_tissue_consumption(self):
        tissue_consumption=round(self._size/6.5 + 0.5,2)
        return f'Расход на пальто: {tissue_consumption}'
        
class Suits(Clothing):
    
    def __init__(self,height):
        self._height=height
    
    @property
    def get_tissue_consumption(self):
        tissue_consumption=round(2 *self._height + 0.3,2)
        return f'Расход на костюм: {tissue_consumption}'    
    
    
coat1=Coats(40)

suit1=Suits(185)

print(coat1.get_tissue_consumption)
print(suit1.get_tissue_consumption)
        

