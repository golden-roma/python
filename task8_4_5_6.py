# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 15:03:55 2021

@author: Роман
"""


class Warehouse:
    
    def __init__(self):
        self._equip_dict={}
        self._unit_list=[]
    
    
    def add_unit(self,*off_equips):
        printer_amount=0
        scanner_amount=0
        xerox_amount=0
        for off_equip in off_equips:
            if off_equip.get_equip_type().lower()=='принтер':
                printer_amount+=1
            elif off_equip.get_equip_type().lower()=='сканер':
                scanner_amount+=1
            elif off_equip.get_equip_type().lower()=='ксерокс':
                xerox_amount+=1
            self._equip_dict['тип устройства']=off_equip.get_equip_type()
            self._equip_dict['описание']=off_equip.get_info()
            self._unit_list.append(self._equip_dict)
        
        self._unit_list.append({
            'общее кол-во ксерокс':xerox_amount,
            'общее кол-во принтер':printer_amount,
            'общее кол-во сканер':scanner_amount
            
        })
        
    def get_unitlist(self):
        return f'На складе сейчас есть следующая техника: {self._unit_list}'

class OfficeEquipment:
    
    def __init__(self,price,model,issue_year):
        self._price=price
        self._model=model
        self._issue_year=issue_year
    
    def get_equip_type(self):
        return self._equip_type

class Printer(OfficeEquipment):
    
    def __init__(self,price,model,issue_year):        
        super().__init__(price,model,issue_year)
        self._equip_type='принтер'
        
    def get_info(self):
        return f'Принтер: цена - {self._price} руб, модель - {self._model}, год выпуска - {self._issue_year}'
    
class Scanner(OfficeEquipment):
    
    def __init__(self,price,model,issue_year):        
        super().__init__(price,model,issue_year)
        self._equip_type='сканер'
    
    def get_info(self):
        return f'Сканер: цена - {self._price} руб, модель - {self._model}, год выпуска - {self._issue_year}'
    

class Xerox(OfficeEquipment):
    
    def __init__(self,price,model,issue_year):        
        super().__init__(price,model,issue_year)
        self._equip_type='ксерокс'
    
    def get_info(self):
        return f'Ксерокс: цена - {self._price} руб, модель - {self._model}, год выпуска - {self._issue_year}'

wh1=Warehouse()

printer1 = Printer(5000,'Samsung-200',2018)
printer2 = Printer(5200,'Samsung 5TX',2019)
print(printer1.get_info())

scanner1 = Scanner(3000,'Toshiba-2MX',2019)

print(scanner1.get_info())

xerox1 = Xerox(2500,'Sony 53M65',2017)

print(xerox1.get_info())

wh1.add_unit(printer1,scanner1,xerox1,printer2)

print()
print(wh1.get_unitlist())