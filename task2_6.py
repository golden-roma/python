# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 14:04:11 2021

@author: Роман
"""


#my_tup=[(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'}),(2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед': 'шт.'})]

products=[]

prod_amount=int(input('Введите кол-во категорий товаров для добавления: '))

for prod in range(prod_amount):
    print(f'Характеристики товара №{prod+1}')
    title=input('Введите название товара: ')
    price=input('Введите цену товара: ')
    amount=int(input('Введите кол-во товаров: '))
    unit=input('Введите единицу: ')
    
    products.append((len(products)+1,{'название':title,'цена':price,'количество':amount,'ед':unit}))

for el in products:
    print(el)


products_info={}

titles=[]
prices=[]
amounts=[]
units=[]

for prod in products:
    
    for key,value in prod[1].items():
        #print(key,value)
        if key=='название':
            titles.append(value)
        elif key=='цена':
            prices.append(value)
        elif key=='количество':
            amounts.append(value)
        elif key=='ед':
            units.append(value)
            
products_info={'название':titles,'цена':prices,'количество':amounts,'ед':units}

for key,value in products_info.items():
    print(f'{key}:{value}')