# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 21:02:06 2021

@author: Роман
"""


class Stationery:
    def __init__(self,title):
        self._title=title
        
    def draw(self):
        return 'Запуск отрисовки'
    
class Pen(Stationery):
    
    def draw(self):
        return 'Ручка пишет "{}"'.format(self._title)
    
class Pencil(Stationery):
    
    def draw(self):
        return 'Карандаш пишет "{}"'.format(self._title)

class Handle(Stationery):
    
    def draw(self):
        return 'Маркер пишет "{}"'.format(self._title)

st=Stationery("Chao")

print(st.draw())

pen1=Pen('Hello, world!')

print(pen1.draw())

pencil1=Pencil('Hey, guys')

print(pencil1.draw())

handle1=Handle('See you')

print(handle1.draw())