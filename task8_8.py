# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 15:40:50 2021

@author: Роман
"""


class ComplexNum:
    
    def __init__(self,num_real,num_img):
        self.num_real = float(num_real)
        self.num_img = float(num_img)
        
        if self.num_img==0:
            self._num = f'{self.num_real}'
        else:
            self._num = f'{self.num_real}+({self.num_img})*i'
        
    def __add__(self,other):
        return ComplexNum(self.num_real + other.num_real,self.num_img + other.num_img)
    
    def __mul__(self,other):
        return f'{self.num_real * other.num_real-1} + ({self.num_real * other.num_img + self.num_img * other.num_real})*i'
    
    def __str__(self):
        return self._num

num1 = ComplexNum(2,-2)

num2 = ComplexNum(1,3)

print()

print('Сложение комплексных чисел: {}'.format(num1+num2))

print('Умножение комплексных чисел: {}'.format(num1*num2))