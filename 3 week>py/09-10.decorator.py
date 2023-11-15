# def my_function(name):
#     print(f'Hello{name}')

# your_function = my_function

# def new_function(func):
#     print('я функция которая принимает другую функцию')
#     func('Python')
#     print('Конец')

# new_function(your_function)



'------------------------------Декораты---------------------------'
# функция высшего порядка - эта функция которая принимает в аргументы функцию, создает внутри себя функцию, 
# вызывает функцию и возвращает функцию


# def func_1(func): # функция высшего порядка
#     print(func)
#     return func

# def func_2():
#     print('Function')
#     return 'hello'

# func_1(func_2)


# Декораторы - это функция высшего порядка, которая нужна чтобы расширять 
# функционал другой функции не изменяя ее (функцию обвертка)
# from functools import wraps
# def decorator12(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         from datetime import datetime
#         print('Start: ', datetime.now())
#         func(*args, **kwargs)
#         print('finish', datetime.now())
#     return wrapper
    
# def hello():             # первый метод вызова декоратора
#     print('Hello')

# hello1 = (decorator(hello))
# hello1()

# @decorator12               # второй метод выхова декоратора
# def hello():
#     print('hello world')

# hello()


# @decorator12
# def func_():
#     """
#     Функция func_  нечего не принимает и возврощает None
#     """

# print(func_.__doc__)
# print(func_.__name__)       

# def decorator(num):
#     def inner_decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(num):
#                 func(*args, **kwargs)
#         return wrapper
#     return inner_decorator

# @decorator(5)
# def sum_(a,b):
#     print(a+b)

# sum_(5,10)

# inner_decorator = (decorator(5))
# wrapper = inner_decorator(sum_)
# wrapper(5,10)

# decorator(3)(sum_)(5,10) # третьй метод выхова декоратора

def double(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res * 2
    return wrapper

# @double
def add(a,b):
    return a + b

# print(add(10,2))

# print(double(add)(10,2))

# #1
# def decorator1(func):
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             return res * 2
#         return wrapper

# @decorator1
# def y_(a,b):
#     return a * b

# print(y_(10,2))

#2
import random
# def upper_case(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args,**kwargs)
#         return res.upper()
#     return wrapper


# @upper_case
# def spisok(list1):
#     return random.choice(list1)

# l = ['dd','ss','rr']
# print(spisok(l))



#3
# def decorator2(func):
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             a =  list(set(res))
#             return a
#         return wrapper
       
# def random_number():
#     lst = [random.randint(10, 50)for _ in range(101)]
#     return lst

# @decorator2
# def generator_():
#     return random_number()

# res1 = random_number()
# res2 = generator_()

# print(res1)
# print(res2)
#4
# def decorator3(func):
#     def wrapper(*args, **kwargs):
#         login, password =  func(*args,**kwargs)
#         login = ''.join(chr(ord(char)+1) for char in login)
#         password = ''.join(chr(ord(char)+1) for char in password)
#         return login, password
#     return wrapper

# @decorator3
# def register():
#     login = input(" Напишите login: ")
#     password = input(" Напишите password: ")
#     return login, password

# a,b = register()
# print('Зашифрованный',a)
# print('Зашифрованный',b)

#4

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         login = input('Введите логин: ')
#         password = input("Введите пароль: ")
#         new_login = ''.join(chr(ord(char)+1) for char in login)
#         new_password = ''.join(chr(ord(char)+1) for char in password)
#         return func(new_login, new_password)
#     return wrapper

# @decorator
# def process_main(login, password):
#     print(f'Ваш зашифрованный логин: {login}')
#     print(f'Ваш зашифрованный пароль: {password}')

# process_main()
#5
# def decorator3(func):
#     def wrapper(*args, **kwargs):
#         with open('file.txt','w+') as file:
#             file.write(str(func(*args, **kwargs)))
#     return wrapper

# @decorator3
# def multiplay(a,b):
#     return a * b

# multiplay(2,3)

# def  repeater(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#         func(*args,**kwargs)
#     return wrapper

# @repeater
# def miltiply(num1,num2):
#     print(num1*num2)

# miltiply(2,6)

# '''
# <table>
# <h1>
# Hello world!
# </h1>
# </table>
# '''
# def header(func):
#     def wrapper(*args, **kwargs):
#         print('<h1>')
#         func()
#         print('</h1>')
#     return wrapper

# def table(func):
#     def wrapper(*args, **kwargs):
#         print('<table>')
#         func()
#         print('</table>')
#     return wrapper

# @table
# @header
# def hello():
#     print('Hello world!')
# hello() #2

# header1 = table(header(hello))
# header1() #1

# table(header(hello))() #3

# def make_bold(func):
#     def wrapper(*args, **kwargs):
#         stroka = func()
#         new = f'<b>{stroka}</b>'
#         return new
#     return wrapper

# def make_italic(func):
#     def wrapper(*args, **kwargs):
#         stroka = func()
#         new = f'<i>{stroka}</i>'
#         return new
#     return wrapper

# def make_underline(func):
#     def wrapper(*args, **kwargs):
#         stroka = func()
#         new = f'<u>{stroka}</u>'
#         return new
#     return wrapper

# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'

# print(hello())
# def decor(name):
#     def inner_decor(func):
#         def wrapper(*args, **kwargs):
#             with open(name,'w+') as file:
#                 file.write(str(func(*args, **kwargs)))
#         return wrapper
#     return inner_decor

# @decor('database.txt')
# def multiplay(a, b):
#     return a * b

# multiplay(2,3)

def write_to_file(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as file:
                file.write(str(result))
            return result
        return wrapper
    return decorator


def decorator(func):
    def wrapper(*args, **kwargs):
        login = input('Введите логин: ')
        password = input("Введите пароль: ")
        new_login = ''.join(chr(ord(char)+1) for char in login)
        new_password = ''.join(chr(ord(char)+1) for char in password)
        return func(new_login, new_password)
    return wrapper

@write_to_file('database.txt')
@decorator
def process_main(login, password):
    print(f'Ваш зашифрованный логин: {login}')
    print(f'Ваш зашифрованный пароль: {password}')
    return f'{login} {password}'

def read_decorator(name):
    def innder_decor(func):
        def wrapper(*args, **kwargs):
            with open(name, 'r') as file:
                text = file.read()
                login, password = text.split()
                new_login = ''.join(chr(ord(char)-1) for char in login)
                new_password = ''.join(chr(ord(char)-1) for char in password)
                func(new_login, new_password)
                return text
        return wrapper
    return innder_decor


@read_decorator('database.txt')
def login_pass(login, password):
    print(f'Ваш  логин: {login}')
    print(f'Ваш  пароль: {password}')

login_pass()
process_main()

