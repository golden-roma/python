# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 21:20:21 2021

@author: Роман
"""

from itertools import cycle
import time

class TrafficLight:
    def __init__(self):
        self._color=[['красный',7],['желтый',2],['зеленый',10]]
        
    def running(self):
        x=1
        for el in cycle(self._color):
            if x>len(self._color):
                break
            print(el[0])
            time.sleep(el[1])
            x+=1

t_light=TrafficLight()
t_light.running()

#t_light=(('красный',7),('желтый',2),('зеленый',10))

'''if self._color=='красный':
            self._t_light=[['красный',7],['желтый',2],['зеленый',10]]
        elif self._color=='желтый':
            self._t_light=[['желтый',2],['зеленый',10],['красный',7]]
        elif self._color=='зеленый':
            self._t_light=[['зеленый',10],['красный',7],['желтый',2]]'''

