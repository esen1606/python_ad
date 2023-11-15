# '----------------------------------Множества(set)-------------------------------'
# #множестов - это изменяемый, неупорядочный, итерируемый, неиндексируемый тип данных, 
# # предназначение для хранения уникальных значений (нельзя хранить изменяемые типы данных),
# # даже нельзя хранить данные в tuple([1,2,3])
# #Typeror unhashble

# set_1 = {1,2,3,4,5, 'abc', 'dsf', (1,2,3,4)}
# # print(set_1)
# set_2 = {1,1,1,1,1,1} #set хранит только  уникальные значение
# # print(set_2)
# set_3 = {True,False,0,1} #берет значения по очередности и выведет False и True
# # print(set_3)


# "---------------------------------Методы Множества-----------------------------------------"
# set1={2,3,4,'0.1',5,'a'}
# #pop - удаляет случайный элемент из множества
# a = set1.pop()
# # print(a)

# #remove - удаляет элемент из set по значению, если элемента нету в множестве выводит ошибку KeyError
# # set1.remove('4')
# # print(set1)

# #add - добовляет элемент в set 
# set1.add(4)
# # print(set1)

# #difference находит различные между множеством и другой коллекцией
# set1 = {1,2,3}
# set2 = {3,4,5}
# # print(set1.difference(set2)) #{1,2}
# # print(set2.difference(set1)) #{4,5}

# #symmetric_difference - находит только разные значения в множествах
# # print(set1.symmetric_difference(set2)) #{1,2,4,5}

# #intersection - выводит одинаковые значения коллекций
# # print(set1.intersection(set2)) # {3}

# # update - добовляет все элементы интируемого обьекта в set
# set1= {1,2,3}
# set1.update('aasdadjnfjndjnngnd')
# # print(set1)

# #discard - удаляет элемент по значение, если в множестве не нашелся элемент не выводит ошибку KeyError
# # set1.discard('3')


# #clear - очищает множество
# set1.clear()
# # print(set1)


# spisok = [1,2,3,4,5,1,2,3,6,7,'a','a','a']
# # print(list(set(spisok)))

# "--------------------------Словари(dict)------------------------------------------------"
# #dict - это изменяемый, интерируемый, неупорядочный, неиндексируемый тип данных, предназначен для хранения данных в парах (ключ:значение) (key:values)
# user ={'name':'Anton', 'login':'ada', 'password':'qwerty'}
# # print(user['password'])
# # print(user)
# # ключами в словаре могут быть только неизменяемый типы данных
# # ключи должны быть уникальными, не должны повторяться, если же они повторяются сохранится последний
# ser ={'name':'Anton', 'login':'ada', 'password':'qwerty', 'name':'ADA'}
# # print(user['name'])
# # хранение могут быть любые типы данных, могут повторятся
# dict_1 = {1:'a', 2:'b', 3:'c'}
# # print(dict_1[4]) #KeyError

# '-----------------------------------Создание словаря--------------------------------'
# dict_1 = {1:'a', 2:'b', 3:'c'} # прописать вручную
# dict_2 =  dict([(1,'a'),(2,'b'),(3,'c')])
# # dict_3 =['name']= 'Jhon'
# # dict_3 = ['login']= 'Snow'
# # print(dict_3)


# '----------------------------------------Методы Словарей--------------------------------'

# #get - метод, который возврощает значение по ключу, если такого ключа нету,  то возврощает None или дефолтное значение 
# user ={'name':'Anton', 'login':'ada', 'password':'qwerty'}
# # print(user.get(1, 'Такого юзера нету'))

# # pop - метод, который удаляет пару ключей и возврощает значение
# # name = user.pop('name')
# # print('name')
# # print('user')

# #popitem - метод, который удаляет последнию пару и возврощает ее
# remove_=user.popitem()
# print(remove_)

# #update - метод, который расширяет словарь парами из второго словаря
# dict_1 = {1:'a', 2:'b', 3:'c'}
# dict_2 = {4,'e'}
# # dict_1.update(dict_2)
# print(dict_1)

# # clear - очищает словарь
# # fromkeys -  метод, который создает новый словарь используя список ключей
# dict_1 = dict.fromkeys(['Anton', ' Alina', 'Aman',1,2,3,4], 'значение')
# print(dict_1)

# '''
# Keys, values, iteams
# - keys - метод который возврощает ключи
# - values -  метод который возврощает все значения
# - iteams -  метод который возврощает tuple с ключами и значениями'''

# print(user.keys())
# print(user.values())
# print(user.items())


# '-----------------------------Интерирование словарей----------------------'

# user ={'name':'Anton', 'login':'ada', 'password':'qwerty'}
# user['name'] = 'Alina'
# print(user)

# # for key in user.keys(): # получаем ключи
# #     print(key)

# # for value in user.values(): # получаем значение 
# #     print(value)


# # for item in user.items(): 
# #     print(item)

# dict_ = {}
# for key, values in  user.items():
#     dict_[values] = key
#     print(dict_)



# students ={'программирование':20, 'экономика': 25, 'медицина':30}
# students['программирование'] = 12
# students['лингвистика'] = 22
# students.pop('медицина')
# print(sum(students.values()))
# print(students)



# guests = int(input('Введите количество гостей:'))
# party = {}
# group_name = [] #список
# count = 1
# for i in range(guests): 
#     group_name.append(input('Введите имена: '))


# for name in group_name:
#     party [count] = name
#     print(party) 
  
# r = int(input("Ко.л гостей: "))
# b ={}
# for i in range(r):
#     i+=1
#     x = input(f"Имя гостя {i}: ")
#     a = {i:x}
#     b.update(a)
# print(b)


# person = {"name":"Kelly", "age": 25, "city": "New York"}
# print(person ("age"))

#3
# sample_set = {"Yellow", "Orange","Black"}
# sample_list= ["Blue","Green","Red"]
# sample_list=set(sample_list)
# sample_set.update(sample_list)
# print(sample_list)

# #4
# set1 = {6,4,2,5,7,8,10,9}
# set1.remove(7)
# print(set1)

# #5
# set1={'Python', 'it', 'c++', 'java', 'programming'}
# set2={'html', 'css', 'c++', 'java', 'dart', 'programming'}

# print(set1.intersection(set2))

# #6
# set2={'Python', 'it', 'c++', 'java', 'programming'}
# set1={'html', 'css', 'c++', 'java', 'dart', 'programming'}
# print(set2.difference(set1))
# #7
# set3={'Python', 'it', 'c++', 'java', 'programming'}
# set3.add('choto-to')
# print(set3.pop(),set3)

#8
# menu = {'manty': 200, 'plov': 150, 'lagman': 130, 'borsh': 100}
# menu['besh_barmak'] = 130
# menu['lagman'] = 135
# menu.pop('borsh')
# print(menu)

# #9
# menu = {'manty': 200, 'plov': 150, 'lagman': 130, 'borsh': 100}
# # menu['drinks'] = ['Coca-Cola', 'Sprite', 'Fanta':80]
# print(menu)


# menu = {'manty': 200, 'plov': 150, 'lagman': 130, 'borsh': 100}
# menu=dict.fromkeys(['drinks'] = ['Coca-Cola', 'Sprite', 'Fanta':80])
#10
# set1 = {'pop','difference','add','intersection','remove','symmetric_difference','update','clear','discard'}
# set2 = {'pop','add','fromkeys'}
# print(set.intersection(set2))


# set1 = set(dir(set))
# dict1 = set(dir(dict))
# data = set1.intersection(dict1)
# new_data=[]
# for i in data:
#     if '_' not in 1:
#         new_data.append(i)
# print(new_data)

#11
# s = []
# for _ in range(3):
#     number = int(input('Введите число'))
#     s.append(number)
#     s = set(s)
#     s = frozenset(s)  #frozenset - неизменяемый 
# print(s)


#12
# suitcase = []
# for _ in range(5):
#     item = input('Выбери вещь которую положить в чемодан: ')
#     suitcase.append(item)
# suitcase.pop()
# print(suitcase)

#13
# ferma1 = {'корова', 'курица', 'овца', 'заяц'}
# ferma2 = {'корова', 'козел', 'собака', 'заяц'}
# ferma3 = ferma1.intersection(ferma2)
# print(ferma3)

#14
# 
#15
count = int(input('Напишете количество слов: '))
for i in range(count):
    words = input('Напишите слово:')
    count=len(set(words))
    print(f'В твоем слове {words}, столько уникальных символов = {count}')