# from calculator import add,substract
# import os

# pwd = os.getcwd()
# print("Текущая дериктоия! ", pwd)

# ls = os.listdir()
# print("Содержимое текущей директории: ", ls)

# os.mkdir('Новая папка')
# os.remove('Новая папка')

# import random
# def generate_password(name, surname):
#     random_number = random.sample(range(1,10), k = 7)
    # print("Рандоманый набор цифр: ", random_number)
    # random_number = [str(i) for i in random_number]
    # password = name + surname + ''.join(random_number)
    # return password

# def get_info():
#     name = input('Введите имя: ')
#     surname = input('Введите фамилию: ')
#     password = generate_password(name, surname)
#     return password
# print(get_info())


# from hello import hello

# name = 'Anton'
# print(hello(name))


# from my_package import calculator

# print(calculator.add(5,5))


'--------------------------------Модуль и Пакеты-------------------------------'
# Любой файл с расширением .py - модуль 
# пакет - набор модулей (обезательно должен быть файл __init__.py)


'-----------------------------Pip, veny-------------------------------------'
# pip - это установщик пакетов (pip install название пакета)
# venv - это виртуальное окружение (изолированное пространство), куда мы скачиваем пакеты, библиотеки, моудли.

# Установка виртуального окружения происходит через команду 
'python3 -m venv "название виртуального окружения"'
# Чтобы активировать виртуальное окружеение нужно прописать команду
' sourse venv/bin/activate'
# Чтобы деактировать виртуальное окружение нужно использовать команду
' deactivate'

# pip3 list - показывает все установленые пакеты

#rm -rf - удаление виртуального окружение

# def  increase(start,end):
#     print(start)
#     if start == end: # если start и end равны возращаем start
#         return start
#     else:
#         increase(start+1, end)

# increase(1,10)

'-------------------------Рекурсивная функция------------------------------'
# Это функция которая вызывает саму себе в теле своей реализации. 
# Основные характеристики рекурсивных функций:

'''
1.Базовый случай - Функция должна иметь условие выхода!
2. Рекурсивный случай - Внутри функции должен быть вызов самой функций, но уже с измененными параметрами!'''


# def factorial(number):

#     if number == 0:
#         return 1
#     else:
#         return number * factorial(number-1)
    
# print(factorial(5)) # 5 * 4 * 3 * 2 * 1 
# 1*2*3*4*5

