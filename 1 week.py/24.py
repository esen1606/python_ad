'------------------------------------------цикл---------------------------------------'
# цикл - 
#for  - цикл который работает 
# while - цикл который который работает пока условия верно (true)
#i = 1
#while true: 
    #print(f"Квадрат числа {i}={i**2}")
   # i = i +1
 #  i += 1

#text= 'Ввелите сообщение:'
#text += "\n или введите слово exit для входа!"

#answer = True
#while answer:
    #message = input(text)
    #if message == 'exit':
      #  answer = False
     #   print('Вы вышли из цикла!')
        #break -- прекращение цикла
    #else:
     #   print(message)
# break - оператор, который останавливает цикл 
#i = 1
#while i<10:
#    if i==5:
 #       i+=1
#       continue
 #       print(f'Квадрат числа {i}={i**2}')
  #      i += 1


#range - диапозон чисе
#print('Начало цикла')
#for i in range(10):
#  print(f'Квадрат числа {i}={i**2}')
#print('Цицл завершен')"
#for i in range(10):
 #   print(f"Python is awesome!")

#i=1
#while i<11:
#    print(f'Python is awesome!')
#    i+=1

# text = input('Напишете какой-либо текст')
# count = int(input('Введите числовое повторение'))
#i=0
#while i<count:
#    print(f'{text}: Отсчет на {i}')
#    i+=1

# for i in range(count):
#     print(f'{text}: Отсчет на {i}')

"--------------------------------------------Range----------------------------------------------------------------"
# range - она позволяет нам генирировать последовательность чисел, в промежутке указанного диапазона
# for i in range(10):
#     print('Privet', i)

# # range(start, end, step)
# for i in range(5, 36, 5):
#     print(i)



#Отрицательный шаг
#for i in range(100,0,-1):
#   print(i)

# m = int(input('Введите число:'))
# n = int(input('Введите число:'))
# for i in range(m,n):
#         if i %2==0:
#           print(i)
# m = int(input('Введите число:'))
# n = int(input('Введите число:'))
# for i in range(m,n):
#     print(i)
  

# num = int(input('Введите число:'))
# # if 7 in b:
# #     print('Yes')
# # else:
# #     print('no')
# has_seven = False
# while num != 0:
#     last_digit = num%10
#     print(f"Наше текущее число: {num}")
#     if last_digit == 7:
#         has_seven = True
#     num = num//10
# if has_seven:
#     print('Yes')
# else:
#     print('No')


# for i in range(1,11):
#     print(i)
# i = 0   
# while i<11:
#     print(i)
#     i+=1

# for i in range(1,20):
#     if i%2 ==0:
#         print(i)
# i = 1
#1 while i<21:
#          if i%2 ==0:
#                  print(i)
#          i = i+1


#2 i = 0
# while i<20:
#         i = i +2
#         print(i)

#Задание №2
# for i in range(1,101):
#     if (i/3)%2==0:
#       print(i)

      
# i=1
# while i<100:  
#      if (i/3)%2==0:
#         print(i)
#      i = i+1

#Задание №3
# for i in range(1,101):
#     if i%3==0 or i%5==0:
#         print(i)
# i=0
# while i<101:
#      if i%3==0 or i%5==0:
#         print(i)
#         i = i +1


#Задание №4
a = 1
b =100
for i in range(a,b):
    # if (i/3)%2==0 and (i/9)%2==0 and 
    if i%3==0  and i%9==0:
        print(i)






