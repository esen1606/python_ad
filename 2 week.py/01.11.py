"----------------------------------Функция-----------------------------"
# Функция - это именованный блок кода, которая вызывается множество раз в других частях программы.
# Параметры функции это переменные, которые будет работать с данными, которые попадают в вашу функцию
# Аргументы - данные, которые мы передаем для параметров при вызове функции.

string = 'fegdhkr'
def our_len(str):
    count = 0
    for i in str:
        count+=1
    return count

print(our_len(str = string))

'--------------------------------Виды аргументов---------------------------'
#1. Позиционные аргументы (передаются в параметры по позиции)
#2. Именованные аргументы (передаются по названием параметр == значение)в

# Аргументы бывают обязательными и необязательными
'''
Обезательные - это те аргументы которым при вызвое функции должны передоваться значения
Необезательные - это аргумент, которые не требуют значение при вызове функции так как при создании функции мы указываем значение по умолчанию.
'''
'------------------------------Распаковка------------------------------------'
 # При распаковке кортежа, списка и множества мы используем одну *
 # При распаковке словаря мы используем **
list1 = [1,2,3,4,5]
print(*list1)
dict1 = {'a':1, 'b':2, 'c':3}
print(dict1)
dict2 = {**dict1, 'f':4}
print(dict2)

"--------------------------------Произвольные аргумент---------------------------"
# Произвольное количество аргументов используется когда нам заранее неизвестно количество аргументов
# *args - данные передаются ввиде tuple
# **kwargs - данные передаются ввиде dict(словаря)

# def sum_ (num1,num2 =0, *args):
#     res = num1 + num2
#     # print(type(args))
#     if args:
#         for i in args:
#             res += i 
#     return res

# print(sum_(1,2))
# print(sum_(1,2,3,4,5,6,7,8,9))
# print(sum_(1))


# def gret(*agrs):
#     for name in agrs:
#         text = f"Hello {name}"
#         print(text)

# gret('Bael','Denis','Kalida')
'---------------------------Виды параметров---------------------------'
# Обезательные
# Необязательные:
        # с дефолтным значением (по умолчанию)
        # agrs (все позиционные аргументы, которые не попали в обезательные)
        # kwargs (все лишние именованные параметры)

# def p_ (num1,num2, *args):
#     res = num1 + num2
#     if args:
#         for i in args:
#             res += i 
#     return res

# def m_(num1,num2, *args):
#     res = num1 - num2
#     if args:
#         for i in args:
#             res += i
#     return res

# def y_(num1, num2, *args):
#     res = num1 * num2
#     if args:
#         for i in args:
#             res += i
#     return res

# def d_(num1, num2, *args):
#     res = num1 / num2
#     if args:
#         for i in args:
#             res += i
#     return res

# def answer():
#     user_number = input('Введите задачу')
#     if user_number == '+':
#         print(p_(user_number))
#     elif user_number == '-':
#          print(m_(user_number))
#     elif user_number == '*':
#          print(m_(user_number))
#     elif user_number == '/':
#      print(m_(user_number))
#     else:
#         print('такого значение нету')

'-----------------------lamda-------------------------------'
# lamda  - анонимная функция, которая записывает в одну строку
# lambda_func = lambda x : x**2
# print(lambda_func(5))

# calculator = {
#     '-': lambda n1,n2: n1 - n2,
#     '+': lambda n1,n2: n1 + n2,
#     '*': lambda n1,n2: n1 * n2,
#     '/': lambda n1,n2: n1 / n2,
#     '//': lambda n1,n2: n1 // n2,
#     '**': lambda n1,n2: n1 ** n2,
#     '%': lambda n1,n2: n1 % n2,
# }

# def main():
#     num1 = int(input('Введите число №1 '))
#     num2 = int(input('Введите число №2 '))
#     oper = input('Знак')
#     func = calculator[oper]
#     res = func(num1,num2)
#     print(num1,oper,num2, '=' ,res)
# main()

'------------------------------------Register, login----------------------------------'

# database = [
#     {'name':'Anton', 'password': 12345}
# ]

# def in_database(name):
#     for user in database:
#         if user['name'] == name:
#             return True
#     return False

# def reg_database(name, password1, password2):
#     if in_database(name):
#         return f'Юзер с таким именем уже существует!'
#     if password1 != password2:
#         return f'Пароли не совпадают'
#     user = {'name':name, 'password':password1}
#     database.append(user)
#     return f'Вы успешно зарегистривовались'

# def login(name, password):
#     if not in_database(name):
#         return('Пользователь не найден')
#     for user in database:
#         if user['name'] == name:
#             if user['password'] != password:
#                 return "Пароли не верный"
#     return 'Вы успешно вошли!'

# def main():
#     print('Добро пожаловать!')
#     while True:
#         action = input("Введите что-то из этого -> register:1, login:2, quit:3")
#         if action =='3':
#             break
#         elif action =="1":
#             name = input("Введите имя пользователя: ")
#             password1 = input("Введите пароль: ")
#             password2 = input("Введите пароль снова: ")
#             print(reg_database(name,password1,password2))
#         elif action =='2':
#             name = input("Введите имя пользователя: ")
#             password = input("Введите пароль")
#             print(login(name,password))
#         else:
#             print('Не корректный выбор!')
# main()
# list1 = [1,2,3,4,5]
# def list_p():
