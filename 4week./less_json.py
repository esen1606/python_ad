'----------------------------------------Json---------------------------'
#JavaScript Object Notation - универсальный формат, в котором мы можем  хранить данные в типах данных, понятных
# почти для всех языков програмирование

import json

# десериализация - перевод с json строки в python обькт
"""
loads - метод для десериализации с json строки
load - метод для десериализации с json файла
"""
# сериализация - перевод python обьекта в json строку
""""
dumps - метод для сериализации в json строку
dump - метод для сериализации в json файл
"""

with open('/home/esen/Desktop/ada/4week./db.json', 'r') as file:
    list_ = json.load(file)

# print(list_)
# list_.append([1,2,3])

# with open('/home/esen/Desktop/ada/4week.py/db.json','w') as file:
#     json.dump(list_, file)

# def create_(id, title, description, price):
#     


# def create_(id, title, description, price):
#     with open('db.json', 'r') as file:
#         text = json.load(file)
#     with open('db.json', 'w') as file:
#         text.append({'id':id, 'title':title, 'description': description, 'price': price})
#         json.dump(text,file,ensur
# e_ascii=False)

# create_(3,'Самсы','Vkusniy sushi',150)

for _ in range(True):
    print(1)
    

