# from human import eat

# print(eat('Banan'))

# from animal import eat, get_voice


# print(eat('cat', 'fish'))
# print(get_voice('cat', 'Meow'))
#3
# import random
# names = ['Beka','Alymbek','Aziz','Nursultan','Timur','Dastan','Isa','Emir','Ilim']
# def r(names):
#     random_n = random.sample(names,3)
#     return random_n
# print(r(names))
#4
# import sys
# print(sys.platform)
#5
# a = int(input('Введите первое значение: '))
# b = input('Введите второе значение: ')
# print('Размер занимающий память 1: ', sys.getsizeof(a))
# print('Размер занимающий память 2: ', sys.getsizeof(b))

#6 '----------------Регенерации пароли---------------'
# import random
# import string
# def generator_password(lengts):
#     digits = string.digits
#     letters = string.ascii_letters
#     data = digits+letters
#     password = ''.join(random.choice(data) for i in range(lengts))
#     return password

# n = int(input("Введите длину пароля: "))
# password = generator_password(n)
# print(password)

#7
import random
choice = ['камень', 'бумага' , 'ножницы']

def play_2():
    while True:
        you = input('Сделайте выбор: камень ножницы или бумага: ')
        laptor = random.choice(choice)
        print(f"\n Вы выбрали {you}, ноутбук выбрал {laptor}.")
        if you == laptor:
            print(f'Оба выбрали {you} Ничья!')
        elif you == "камень":
             if laptor == "ножницы":
                 print('Камень бьет ножницы! Вы победили!' )
             else:
                 print('Бумага оборачивает камень! Вы проиграли')
        elif you == 'бумага':
            if laptor == 'камень':
                print('Бумага оборачивает камень! Вы победили!')
            else:
                print('Ножницы режут бумагу! Вы проиграли!')
        elif you ==  'ножницы':
            if laptor == 'бумага':
                print('Ножницы режут бумагу! Вы победили!')
            else:
                print('Камень бьет ножницы! Вы проиграли!')
            play_again= ""
            play_again = input('Сыграем еще? (д/н): ')
            if play_again.lower() != "д":
                break

play_2()



