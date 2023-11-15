'----------------------------------Игра угадай число-------------------------------------'
name = input('Введите имя: ')
print('Здравствуйте', {name})
start = input('Хотите сыграть в игру?' )

from random import randint 
x = randint(1,10)
# print('Угадай число от 1 до 10')
check = 0
attempt = 3


# while start !=('нет'):
while check<attempt: 
    user_number = int(input('Угадайте число от 1 до 10: '))
    check +=1
    if user_number == x:
        print('Поздравляю, вы угадали число! \n Количество ваших попыток:' + str(check) + ' ' 'Cпасибо за игру')
    elif check == attempt:
        print('Вы истратили все попытки')
        break
    else:
         print('Вы не угадали')


game = input('хотите ли вы сыграть еще раз? ')
if game == 'нет':
    print('Спасибо за игру ')
    # break    

# if check == attempt:
#         end = input('если хотите выйти, напишите выход ')
#         if name== 'да':
#              print(start)
#         elif name == 'нет':
#             print('Спасибо за игру')
            
    # else:
    #     print('Неправильный ответ')