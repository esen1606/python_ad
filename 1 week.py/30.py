'-----------------------------------------------Двумерные списки(массивы)----------------------------------------'
# Двумерных списки - это структура данных, которая предствляет союой таблицу, состоящию из строк и столбцов.
#  в Python двумерные массивы реализуются с помощью вложенных списков.

# martix =[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
'--------------------------------While matrix-----------------------------'
# n = 3 # количество строк
# m = 3 # количество столбцов
# count = 1
# array = []
# i = 0
# while i < n:
#     array.append([])
#     j = 0
#     while j < m:
#         array[i].append(count)
#         count += 1
#         j += 1
#     i += 1 
# print(array)

'----------------------------For martix------------------------------------------'

# n = 3
# m = 3
# array = []
# count = 1
# for i in range(n):
#     array.append([])
#     for j in range(m):
#         array[i].append(count)
#         count += 1
# print(array)

# n = 3
# m = 5
# array = list(range(n))
# for i in range(n):
#     array[i] = list(range(1, m+1))
# print(array)

# matrix = [
#     [1, 2, 3, 4, 5], 
#     [1, 2, 3, 4, 5],
#     [1, 2, 3, 4, 5],
# ]

# n = len(matrix)
# m = len(matrix[0])
# i = 0
# while i < n:
#     j = 0
#     while j < m:
#         print(matrix[i][j], end=' ')
#         j += 1
#     print()    
    # i += 1
# print(matrix)
# matrix = [
#     [1, 2, 3, 4, 5], 
#     [1, 2, 3, 4, 5, 6, 7, 9],
#     [1, 2, 3, 4, 5],
# ]
# n = len(matrix)
# for i in range(n):
#     m = len(matrix[i])
#     for j in range(m):
#         print(matrix[i][j], end = ' ')
#     print()
# print(matrix)
# n = 3
# m = 3
# array = list(range(n))
# for i in range(n):
#     array[i]= list(range(m))
#     for j in range(m):
#         el = input('Введите элемент в {} x {} позицию'.format(i,j))
#         array[i][j] = el
# print(array)

list1 = []
for i in range(1,6):
    list1.append(i)
print(list1)

list2 = [i for i in range(1,6)]
print(list2)
'--------------------------------------------Comprehensions----------------------------------------'
# Генератор - с помощью которого мы можем создавать помледовательность используя цикл for в одну строку.
""""
 Результат for элемент in последовательность
 Результат for элемент in последовательность if фильтр
 Результат if условия else тело for элемент in последовательность
 Результат if условия else тело for элемент in последовательность if фильтр
 """

comperhensions_ = (i**2 for i in range(101) if i % 2 == 0)
print(comperhensions_)
print(type(comperhensions_)) # ()- генератор, [] - лист/list
for i in range(3):
    print(next(comperhensions_)) # 0 

#next -  функция, которая запрашивает у генератора текущий элемент и генератор создают следующий элемент

'--------------------------------List Comprehensions---------------------------------------'
list1 = [i for i in range(10)]

new_list = [1, ' hello', True, 2, False, 'sdsdd', 'dfdfdffd']
string = [i for i in new_list if type(i) == int]
print(string)

'--------------------------------Dict Comprehensions---------------------------------------'
dict_ = {i:i for i in range(10)}
print(dict_)

dict_={'a': [1,2,3,4,5], 'b': [2,3,4,5,6], 'c': [2,3,5,7]}
new_dict ={key:sum(val)  for key, val in dict_.items()}
print(new_dict)
'----------------------------------Set Comprehensions---------------------------------'
set1 = [1,2,3,4,4,5,3,2,1]
set_ = {i for i in set1}
print(set_)

# задание 1
# array = []
# n = 3
# m = 4
# array = list(range(n))
# for i in range(n):
#     array[i]=[1 for i in range(m)]
# print(array)
# for i in range(n):
#     array.append([])
#     for j in range(m):
#         array[i].append(1)
# print(array)


#2
# n = 3
# m = 3
# array =  []
# count = 1
# for i in range(n):
#     array.append([])
#     for j in range(m):
#         array[i].append(count)
#         count += 1
# print(array)

#3
# n = 2
# m = 3
# array = list(range(n))
# for i in range(n):
#     array[i] == list(range(m))
#     for j in range(m):
#         element = input('Введите элемент в {} x {} позицию')
#         array[i][j] = element
# print(array)

#4
# n = 10
# m = 5
# array = []
# count = 1
# for i in range(n):
#     array.append([])
#     array[i].append([number*count for number in range(1,6)])
#     count += 1
# print(array)

#5
# n = 8
# m = 8
# chess_board = []
# for i in range(n):
#     row = []
#     for j in range(m):
#         if ( i + j ) % 2 == 0:
#             row.append('.')
#         else:
#             row.append('*')
#             print(row)
#     chess_board .append(row)
# for row in chess_board:
#     print(' '.join(row))
#6
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
res = [i for i in a if i<5]
# print(res)
#7


print(i)
