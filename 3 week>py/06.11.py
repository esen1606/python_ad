'-----------------------------------------Try Except------------------------------'
# Исключение -  это обьекты которые прерывают работу кода, если не были обработаны (связаны с логикой программы)

# print('Hello')
# try:
#     print(15/5)
#     print(12/3)
#     print(5/0)
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# print('1234')

# Ошибки - обьекты, которые прерывают работу и их нужно обработать (связаны по большей части с разработчиком)

'''
SyntaxError: unexcepted E0F while parsing 
(когда мы не закрыли скобку либо кавычки)

a =
SyntaxError: invalid syntax
(когда мы сделали что-то не правильно в синтаксисе)'''

NameError
# исключение, которое выходит, когда мы обращаемся к несуществующей переменной
'''
name_1 = 'str'
print(name_2.islower())
NameError: name 'name_2, is not defined '''

IndexError
# исключение, которое выходит, когда мы обращались по несуществующему индексу
'''
list_ = [1,2,3,4,5]
list_=[50]
IndexError:list index out of range
[1,2,3].pop(5)
IndexError:pop index out of range
'''

KeyError
# исключение, которое выходит, когда мы обращаемся по несуществующему ключу
'''
dict_ {}'a':1}
dict_['b']
KeyError: 'b'
dict_ = {'a':1}
dict_.get('b')None
'''

ValueError
# исключение, когда мы передаем в функцию не коректный для нее тип данных
# когда мы распаковываем интерируемый обьект на несколько переменных и количество переменных не совпадает с количеством элементов внутри интерируемого обьекта
'''
int('10b')
ValueError: invalid literal for int() with base 10: '10b'''
'''a,b,c = [1,2]
ValueError: not enough values to unpack (expected 3, got 2)'''

TypeError
# исключение, когда мы  пытаемся использовать методы не свойственные какому-то типу данных или 
# когда мы пытались передать функцию больше или меньше аргументов, чем принимает функция

'''
for i in 55
TypeError: 'int' object is not iterable'''
'''5+'5'
TypeError: unsupported operand  type(s) for +: 'int' and 'str' '''

'''{[1,2,3]:'abc'}
TypeError: unhashable type: 'list' '''
'''input(',1)
TypeError: input expected at most 1 argument, got 2'''

AttributeError
# выходит, когда мы обращаемся к несуществующему или атрибуту обькта(типа данных)
'''[].replace
AttributeError: 'list' object has no attribute 'replace' '''

IndentationError
# выходит, когда мы не правильно используем отступы
"""for i in 5:
IndentationError: expected an indented block after 'for' statement on 
line 80"""
'''
       a= 5
       IndentationError: unexpected indent
'''
Exception
# Исключение, которе создали сами, чтобы его вызвать
# raise Exception('Моя ошибка')

'----------------------Вызов исключений-----------------------'
# raise SyntaxError

'--------------------------------------------Обработка исключение---------------------'
# чтобы код не прекращал свою роботу, мы можем испольвовать конструкцию try-except и обработать вызванное исключение

# try:
#     # код, который возможно вызовет ошибку
#     num = int(input('Введите число: '))
# except ValueError: # исключение, которое может возникнуть
#     print('Вы вели не число!')
# else:   #код который отработает только если никакая ошибка не вызвалась
#     print('Вы ввели число, ',num)
# finally: # код который отработает в любом случае
#     print(' Финал')

# try:
#     num = int(input('Введите число '))
#     if num == 0:
#              raise ValueError
# except ValueError:
#      print('Вы ввели ноль!')

# try:
#       a = int(input())
#       k = 10/a
#       raise Exception
# except:
#       print('Отловленна любая ошибка')

# try:
#          raise TypeError('моя ошибка')
# except: TypeError  as error:
#         print(error)
# def our_sum():
#         try:
#                 n1 = int(input('Введите первое число: '))
#                 n2 = int(input('Введите второе число: '))
#                 print(f'{n1}+{n2} = {n1+n1}')
#         except ValueError:
#                 print('Введите число! ')
        
# our_sum()

# a, b = 1,0
# try:
#     print(a/b)
#     print('Это сообщение не будет напечатано')
#     print(10+'10')
# except TypeError:
#     print("Вы сложили значение несовместимых типов")
# except ZeroDivisionError:
#     print('Деление на 0')

# try:
#         print(a/b)
# except:
#         print("Деление на ноль 0")
# print('Будет ли это сообщение напечатано?')

# try:
#         print('1'+1)
#         print(name)
#         print(1/0)
# except NameError:
#         print("name не существует")
# except (ZeroDivisionError, TypeError):
#         print("Деление на ноль")
# except:
#         print("Что-то пошло не так! ")

'--------------------------------Assert(Утверждение)-------------------------'
# Assert в python используется для проверки утверждения или условий в коде.
# Он предоставляет способ убедиться, что определенное условие верно!
# И если оно не выполняется, генерируется исключение AssertionError

# a = 1
# assert a == 0, "Сообщение об ошибке"
# print(a)

# def devide():
#         try:
#                n1 = int(input('Введите первое число: '))
#                n2 = int(input('Введите второе число: ')) 
#                print(f'{n1} / {n2} = {n1/n2}')
#             #    devide() - бесконечный цикл!
#         except ZeroDivisionError:
#                 print('Делить на ноль нельзя!')
#                 devide()
#         except ValueError:
#                 print('Вы ввели не число!')    
#                 devide()    
# devide()



# with open('data.txt', 'w') as file:
#     file.write('no no no')
# try:
#      with open('data.txt', 'r') as file:
#          text = file.read()  
#          print("Содержимое файла: ")
#          print(text)
# except FileNotFoundError:
#      print("Ошибка: Файл не существует! ")

#2
# with open("text1.txt", 'x') as file:
#     print(file.write())
    
# def f():
    
#1
# try:
#     a = 1+'1'
# except TypeError:
#     print('Что-то пошло не так')

#4
# try:
#     with open('test1.txt' ,  'r') as file:
#         if 'w' in file:
#          print('ДА, в тексте есть w')
#         else:   
#          print('Нет, в тексте нету w')
# except FileNotFoundError:
#    print('Такого файла нету')
   
#6
# import calculator
# try:
#     n1 = int(input())
#     n2 = int(input())
#     a = calculator.add(n1,n2)
#     print(a)
# except ValueError:
#     print('Вы ввели не число!')
# try:
#     n1 = int(input())
#     n2 = int(input())
#     a = calculator.substract(n1,n2)
#     print(a)
# except ValueError:
#     print('Вы ввели не число!')
# try:
#     n1 = int(input())
#     n2 = int(input())
#     a = calculator.multiplay(n1,n2)
#     print(a)
# except ValueError:
#     print('Вы ввели не число!')
# try:
#     n1 = int(input())
#     n2 = int(input())
#     a = calculator.divide(n1,n2)
#     print(a)
# except ValueError:
#     print('Вы ввели не число!')
# except ZeroDivisionError:
#     print('На ноль делить нельзя')