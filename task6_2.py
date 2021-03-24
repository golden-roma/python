# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:37:07 2021

@author: Роман
"""


class Road:
    
    def __init__(self,length,width):
        self._r_length=length
        self._r_width=width
        self._r_massa=25
        self._r_volume=5
    
    def get_massa(self):
        self.__tot_massa=self._r_length*self._r_width*self._r_massa*self._r_volume
        print(self.__tot_massa)
        
road1=Road(20,5000)

road1.get_massa()



        
