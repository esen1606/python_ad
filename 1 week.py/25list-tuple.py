'--------------------------------------------------list--------------------------------------------'

#списки - изменяемый тип данных, индексируемый, упорядочные, интерируемый, предназначенный для хранения любых данных в определенном порядке

# list1 = [1,2,3,4, ' hello', None, True, ['a','b','c']]
# # print(list1[-1][1])

# # list2=list('ada')  # list -с помощью его мы можем создать или переобразовать из других типов данных новый лист
# # print(list2)
# # list3 = list(range(10)) # range генeрация какого-либо диапозона числе с созранением их в лесте
# # print(list3)
# # list4 = list2 + list3 # сложение двух листов приводит к слиянию всех элементов в один лист
# # print(list4)
# # list5 = [1] * 5 # умножение, создает одинаковых элементы на число множителя 
# # print(list5)


# # count_list3 = len(list3) # функция лен находит количество элементов в листе 
# # print(count_list3)



# '-----------------------------------------------Методы списка----------------------------------------------'

# #append - добавляет элемент в наш лист, в конец списка
# list1=['ПРИВЕТ']
# list1.append(2)
# print(list1)
# #pop - удаляет элементы из списка по индексу и возврощает этот удаленный элемент, если не указать индекс то он удалит поcледний элемент списка

# list1.pop(2)
# print(list1)
# # remove - удаляет элемент из списка по значению
# list1.remove(5)
# print(list1)
# #count -  считает кoличество принятого элемента в списке
# a = list1.count(1)
# print(a)
# #index - возврощает индекс первое # List №1
import io


l = ['Sanjar', 'Tilek', 'Kalys', 'Eldar', 'Elina', 'Beka', 'Elzar', 'Bael', 'Atajan', 'Emir', 'Mamed', 'Beka']

# List №2
l = ['integer', 'float', 'string', 'list', 'loop', 'tuple', 'while', 'for']

# List №3
l = [1, 2, 5, 3]
        
# String № 1
s = 'Integers 1,2,3 Floats 44 Strings 5 Lists 10Tuples'
# print(list1.index('Привет'))
# #insert - добовляет в список по индексу
# list.insert(5, 'Начало')
# print(list1)
# #extend - расширяет список за счет другого списка
# list1=[0,0,0]
# list2=[1,1,1]
# # list1.append(list2)
# # print(list1)
# list1.extend(list2)
# print(list1)
# # reverse - изменяет список, расставляя его элементы в обратном порядке 
# list1 = [1,2,3,4,5,6]
# list1.reverse()
# print(list1)
# # sort -  сортирует список, состоящий из за одного типа данных
# list1= [2,3,1,5,6,7,8,11,10]
# list1.sort(reverse=True)
# # list1.sort(key=)  функция с логикой сортировки, reverse
# # list.reverse()
# print(list1)
# #clear - очищает список 
# list1.clear()
# print(list1)

# name,age, prof = ['Anton',25, "Python developer"]
# print(name, age, prof)


# a = int(input('Число'))
# list1 = list(range(1, a+1))
# print(list1)
# total = 0
# for number in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]:
#     total = total+number 
#     print(total)

# list1= [1,2,2,3,4,1,1,1,13,3,1,1,1,1]
# list2=list1.copy()
# # while 1 in list1:
# #     list1.remove(1)
# # print(list1)

# for i in list2:
#     if i ==1:
#         list1.remove(i)
#         print(len(list1), 'в процессе удаление ')
#         print(len(list2), ' наш размер list2')
#         print(list1)

# copy - копирует лист и все его данные делая его отдельным листом но с теми же данными

"--------------------------------------Встроенные функции sum(), min(), max(),-------------"
# #Встроенная функция принимает в качестве параметра список чисел и вычисляет его сумму элементов
# numbers = [1,233,4,5,6,7,8,9,10]
# print('Сумма всех элементов=', sum(numbers))
# # Встроенная функция min() и max() принимают в качестве параметров список и находят минимальный и максимальный элемент в списке
# print(min(numbers), max(numbers))

'---------------------------Кортеж----------------------------------------------------------------'
# tuple_=(1,2,3) # Кортеж 2 метода index и count
# print(type(tuple_))
# tuple_1 =(1) #int
# print(type(tuple_1))

# tuple_2 = tuple('Hello word')
# print(tuple_2[6:])
# tuple_count = len(tuple_2)
# print(tuple_count)

# a = int(input('Число'))
# spisok = []
# for _ in range(a):
#     text = input('Vedite text')
#     spisok.append(text)
#     print(spisok)

#1
# tuple_=(3)
# tuple_1=(tuple_)
# tuple_2=(tuple_1)
# tuple_3=(tuple_2)
# tuple_4=(tuple_3)
# print(tuple_4)


#3
# a = [1,2,3,4, ' hello', None, True, ['a','b','c']]
# print(a)


#4
# name = ['Any, Anton, Esen, Robert, Ly']
# stroka =str()
# s = stroka.join(name)
# print(s)


#5
# list1=[" Hello"]
# list2=['world']
# list1.append(list2)
# print(list1)


#6

l = ['Sanjar', 'Tilek', 'Kalys', 'Eldar', 'Elina', 'Beka', 'Elzar', 'Bael', 'Atajan', 'Emir', 'Mamed', 'Beka']

