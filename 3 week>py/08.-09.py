# def get_voice(animal,voice):
#     text = f"Я {animal}: {voice*3}!!!"
#     return text


# def eat(animal,food):
#     text = f'Я {animal}, и я кушаю {food}'
#     return text

# if __name__ == '__main__':
#     print(eat('dog', 'meat'))
#     print(get_voice('dog', 'gav'))

# t = lambda:print('hello')
# t()


# t_ = lambda a,b: a**2 + b**2
# print(t_)


# #2
# a = lambda g: g*365  
# print(a(5))

# #1
# a = lambda n1, n2, n3: n1*n2*n3
# print(a(1,2,3))

#3
# def rec(n):
#   if n > 0:
#     rec(n-1)
#     if n % 2: print(n)

# rec(30)

#4

# y =  360
# a = lambda d: y-d
# print(a(307))
#6
# list1 = [1,2,3,4,5,6,7,8,9]

# def remove_one(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         lst = remove_one(lst[1:])
#         return lst
# print(remove_one(list1))
#7
# a = [2,5,20,100,9,1,6,7,12,8]
# c = lambda i: i *2
# b = []
# for i in a:
#     b.append(c(i))
# print(*b)

# b = list(map(lambda x: x *2, a))
# print(b)

#8
# a = [2,5,20,100,9,1,6,7,12,8]
# b = list(filter(lambda x: x%3 == 0, a))
# print(b)


#9
# def sum_d(number):
#     if number == 0:
#         return 0
#     else:
#         res = number % 10 + sum_d(number//10)
#         return res
    
# print(sum_d(256))