# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 21:52:27 2021

@author: Роман
"""


class Car:
    
    def __init__(self,color,speed,name,is_police=False):
        self._color=color
        self._speed=float(speed)
        self._name=name
        self._is_police=is_police
        print(f'Добавлена машина: {self._name}, имеющая цвет: {self._color}, полицейский флаг: {self._is_police}')
            
        
    def go(self):
        return 'Автомобиль начинает ехать...'
        
    def stop(self):
        return 'Автомобиль остановился.'
        
    def show_speed(self):
        print(f'Скорость автомобиля: {self._speed} км/ч')
        
    def turn(self,direction):
        return f'Автомобиль едет {direction}...'
        
class TownCar(Car):
    def __init__(self,color,speed,name):
        super().__init__(color,speed,name)
        print(f'Тип автомобиля: TownCar')
        
    def show_speed(self):
        super().show_speed()
        if(self._speed>60):
            print('Автомобиль превысил допустимую скорость!')
        else:
            print(f'Автомобиль едет до 60 км/ч')
           
           
class WorkCar(Car):
    
    def __init__(self,color,speed,name):
        super().__init__(color,speed,name)
        print(f'Тип автомобиля: WorkCar')
    
    def show_speed(self):
        super().show_speed()
        if(self._speed>40):
            print(f'Автомобиль превысил допустимую скорость!')
        else:
            print(f'Автомобиль едет до 40 км/ч')
    
class PoliceCar(Car):
    def __init__(self,color,speed,name):
        super().__init__(color, speed, name,True)
        print('Тип автомобиля: полицейский автомобиль')
        
class SportCar(Car):
    def __init__(self,color,speed,name):
        super().__init__(color,speed,name)
        print(f'Тип автомобиля: SportCar')

car1=Car('красный','55','Toyota')

print(car1.go())
car1.show_speed()
print(car1.turn('налево'))
print(car1.stop())

car2=SportCar('черный','230','bugatti veyron'.title())

car2.show_speed()

car3=PoliceCar('бело-синий','50','Lada')

car4=TownCar('белый','70','Audi')

print(car4.go())
print(car4.turn('направо'))
car4.show_speed()

car5=WorkCar('зеленый','41','BMW')

print(car5.go())
print(car5.turn('назад'))
car5.show_speed()

