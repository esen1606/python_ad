#1 

# def cal_mini(n1,n2):
#     res = n1 + n2 
#     return res

# # n1 = 5
# # n2 = 7
# print(cal_mini(6,6))

#2
# a = 'sdddsds'
# def stroka_(a):
#     res = [len(a)]
#     return res

# print(stroka_(a))

#3

# def try_(t,p):
#     ti = type(t)
#     pi = type(p)
#     return ti,pi

# t = 56
# p = 'wewe'
# print(try_(t,p))

#4
# def cal_mini(n1,n2):
#     res = n1 / n2 
#     return res


# print(cal_mini(6,2))
#5
# slovar ={'name': 1234,'password': 1234}
# def prinimaet_s(k):
#     for key in slovar.keys():
#         print(key)
         
# print(prinimaet_s(slovar))

# #6
# def r_(number):
#     if number % 2>0:
#         print('its odd number')
#     elif number % 2==0:
#         print('its even number')
#     else:
#         print(".")
#     return number


# print(r_(5))
#7
# stroka = 'dsd'
# def proverka_(s):
#     stroka[::-1]
#     if s == stroka:
#         print('True')
#     else:
#         print('False')
#     return s

# print(proverka_(stroka))


# slovo = 'komok'
# print(slovo[::-1])

#8

# n1 = int(input())
# n2 = int(input())
# def f(n1,n2):
#     a = (n1//n2*n1+n2//n1*n2)//(n1//n2+n2//n1)
#     return a
# print(f(n1,n2))
#9

# def slovar(sl, i):
#     for i in sl:
#      y = [i]*[i+1]
#     return y
 
# a = int(input())
# b = int(input())
# c = int(input())
# sl = range(a, b, c)
# z = slovar(sl)
# print(z)

#10
# n = int(input("Введите число="))   
# def f(n):
#     while n > 0:    
#         sum = 0          
#         d = n%10           
#         n = n // 10           
#         sum += d   
#         print("Сумма всех цифр этого числа =",sum)
# f(n)
