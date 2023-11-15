"----------------------------------------Работа с файлами-----------------------------------"
# open - функция, которая открывает файл в определенном режиме 

'''
Режимы:
r - read (только для чтения)
w - write (только для записи каждый раз файл очищается)
a - append (только для добавление записи, добавляется в конец файла)
x - создает файл, но если он уже существует выйдет ошибка
b - binary (окрывает файл в бинарном виде)
'''

# new_file  = open('test1.txt', 'x')
# print(dir(new_file))
# new_file.close()

'------------------------------------------Read----------------------------------'

# file = open('/home/esen/Desktop/ada/test1.txt', 'r')
# print(file.read())
# # print(file.writable()) # метод который проверять можно ли что-то написать в файл
# # print(file.readable()) # метод проверяет можно ли прочитать файл
# file.seek(0)
# # print(file.read())
# # print(file.readline()) # выводит только строку документа, возращает строку, можно использовать методы строк
# # print(file.readline(2)) # выводит только два первых символа
# print(file.readline().replace('\n', ''))
# print(file.readline().replace('\n', ''))
# print(file.readline().replace('\n', ''))
# file.seek(0)
# print(file.readlines()) # возращет список с элементами строки

# print(file.tell()) # возращает список с элементами строки
# file.seek(5)
# print(file.tell())

# file.close()

'---------------------------------Write--------------------------------------'
# file = open('test2.txt', 'w') # очищает файла происходит при открытии
# print(file.readable())
# print(file.writable())
# file.write('Ada Incubator')
# file.write('1\n')
# # перед тем как записать данный файл очищается полностью
# file.writelines(('bootcamp','incubator','room'))
# # принимает список только со строками
# file.close()
'-------------------------------Append---------------------------------'
# file = open('test2.txt', 'a') # если файла нету, то он его создаст
# print(file.readable())
# print(file.writable())
# file.write('\nAda')


# file.close()


'----------------------------------Контекстный менеджер-----------------------------'
# конструкция with работает с любыми обьектами у которых есть два метода 
# _enter_, _exit_

#_enter_ работает в начале конструкции with (Try)
#_exit_ работает когда конструктор закончил работу и заканчивается конструкция через finally

# with open('test2.txt', 'w+') as file:
#     print(file.readable())
#     print(file.writable())
#     file.write('1,2,3,4,5')
#     print(file.tell())
#     file.seek(0)
#     print(file.read())
"----------------------------Задание----------------------------------"
#1
# with open('test3.txt', 'w+') as file:
#     file.write('Hello would')
#     file.seek(0)
#     print(file.read())

#2
# name = input('Введите имя: ')
# password = input('Введите пароль: ')
# with open('users.txt','a+') as file:
#     file.write(f' логин: {name}\n пароль: {password}\n')
#     print(file.read())

#3
# with open('/home/esen/Desktop/ada/test1.txt', 'r') as file:
#     if 'w' in file:
#      print('ДА, в тексте есть w')
#     else:   
#         print('Нет, в тексте нету w')

#4

# o_words=[]
# with open('python.txt', 'r') as file:
#     data = file.read().split()
#     for word in data:
#         if 'o' in word:
#             o_words.append(word)
#     print('Finish')

# print(o_words)

#5
with open('text4.txt', 'r') as file:
    print(file.read())
    for i in reversed(file):
        print(i)