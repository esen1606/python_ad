'===========================================Области видимости================================================'
# LEGB - Local Enclosed Global Build-in

'---------------------------------------Buid-in---------------------------------'
# встроенное пространство имен (list, sum, print, input)

'------------------------------------Global--------------------------------------'
# все переменные, которые мы создали внутри одного файла 
# Чтобы посмотреть глобальные переменные можно использовать globals
# a = 5
# b = 6
# c = 7
# print(globals())

'---------------------------------Enclosed (nonlocal)--------------------------------'
# Замкнутное пространство имен - локальное пространство, у которого есть внутреннее локальное пространство

# var = 'global'

# def func():
#     var = 'enclosed'
#     def inner_func():
#        var = 'local'
#        print(var)
#     print(var)
#     inner_func()
# print(var)
# func()
'--------------------------------Local-----------------------------------'
#   Локальное пространство имен - переменные, созданные внутри функции
# a = 10

# def func(a,b):
#     print("Global", globals())
#     print('from animal import eat, get_voice


# print(eat('cat', 'fish'))
# print(get_voice('cat', 'Meow'))Local', locals())
#     print(a,b)

# func(5,7)
# print(a)

# count_1 = 1

# def count():
#     print(count_1)
#     count_2 = count_1 +1
#     return count_2

# print(count())

def counter(i):
    count_ = 0

    def inner_counter():
        nonlocal count_ # доступ на изменение переменной замкнутого пространство
        print(count_)
        count_ +=1

    for _ in range(i):
        inner_counter()

counter(10)