'--------------------------------------Встроенные функции------------------------------------'
# map, filter, zip, enumerate

# zip - соединяет несколько последовательностей (получаем генератор, в котором элементы - tuple)

list1 = [1,2,3,4,5,6]
list2 = ['a','b','c']
list3 = [1.5,1/2,1.3]

zipped = zip(list1,list2,list3)
for elem in zipped:
    print(elem)

dict_ = dict(zip(list2,list3))
print(dict_)

#enumerate - нумерует последовательность (по дефолту с 0) так же получаем генератор
enumerated = enumerate('hello')
print(list(enumerated))

#map - функция высшего порядка, принимает другую функцию и интерируемый объект, выполняет задданую функцию на каждый элемент последовательности

# list1 = ['1','2','3']
# mapped = map(int, list1)
# print(list(mapped))

# number = map(int, input('Введите числа через пробел ').split())
# print(f'Summ numbers = {sum(list(number))}')

#filter - функция высшего порядка возращающая генератор, с элементами, прошедшими фильтр (какой-то условие), принимает функцию и элементы последовательность.
# list1 = [1,2,3,-3,-2,-1,0]
# filtered = filter(lambda i : i>0, list1)
# print(list(filtered))

# string = input('Введите слова: через пробел: ').split()
# # result = list(map(len,string))
# # print(string)
# # printl(result)
# res = [len(i) for i in string]
# print(res)

# nums = [1,1,2,3,5,8,13,21,34,55,89]
# nums1= [234,55,89]
# # res = filter(lambda i : i<5, nums)
# res = [i for i in nums if i<5]
# # print(list(res))
# print(res)

# def find_even():
#     for num in nums:
#         if num%2 ==0:
#             print(num)
#         return 'функция завершила свою работу'
# find_even()

# return - функция всегда = None (конец функции), но можноизменять (None)

'---------------------------------Функция--------------------------------------'
# Функция - это именованный блок кода, которая вызывается множество раз в других частях программы.
# Они создаются блогадаря ключевому слову def
# При наименовании функции нужно придерживаться стилю Snake_case (наименование через"_")
def our_sum(num1,num2):
    res = num1 + num2
    return res
print(our_sum(5,6))
