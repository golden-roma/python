# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 15:35:28 2021

@author: Роман
"""


class Matrix:
    
    def __init__(self,matr):
        self._matr=matr
        
    def __str__(self):
        return f'Итоговое значение: {self._matr}'
    
    def __add__(self,other):
        fin_list=[]
        i=0
        while i<len(self._matr):
           #print(list1[i])
           k=0
           fin_list.append([])
           while k<len(list1[i]):
               fin_list[i].append(self._matr[i][k]+other._matr[i][k])
               k+=1
           i+=1
        
        return f'Сумма матриц: {fin_list}'
    
    
list1=[[5,0,1],[1,1,4]]
list2=[[3,4,2],[-2,6,-2]]

matrix1=Matrix(list1)
matrix2=Matrix(list2)

print(matrix1)
print(matrix2)
print(matrix1+matrix2)

list3=[]

i=0
while i<len(list1):
   #print(list1[i])
   k=0
   list3.append([])
   while k<len(list1[i]):
       list3[i].append(list1[i][k]+list2[i][k])
       k+=1
   i+=1

#print(list3)

