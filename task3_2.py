# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 15:16:38 2021

@author: Роман
"""




def get_user_data(first_name,last_name,birth_year,city,email,phone_nbr):
    result=f'Имя: {first_name}, фамилия: {last_name}, год рождения: {birth_year}, город проживания: {city}'
    result+=f', email: {email}, номер телефона: {phone_nbr}'
    return result    
    
print('Данные пользователя')
print(get_user_data(last_name='Петрович',first_name='Петр',birth_year=1992,city='Москва',phone_nbr='9999999999',email='test@t.ru'))