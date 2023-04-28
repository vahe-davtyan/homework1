# 85

# def traingls(a, b, c):
#     return(a + b + c)
# a = int(input('Enter length traingls: '))
# b = int(input('Enter length traingls: '))
# c = int(input('Enter length traingls: '))
# print(traingls(a, b, c))

# 86

# def 
# chanapar(n):
#     return (n * 1000 / 140) * 0.25
# n = int(input('Qani kilometr: '))
# # print(f'{round (chanapar(n),1}')
# print(f'{round (chanapar(n),1) + 4}$')

# 87

# def patver(qanak):
#     return((qanak - 1) * 2.95 + 10.95)
# qanak = int(input('Enter product count: '))
# print(f'Product count ={qanak}\nProfuct sum ={patver(qanak)}')

# 88

# def number(**kwargs):
#     return kwargs
# dic = number(a = 1,b = 22,c = 8)
# sort = sorted(dic.values())
# print(sort[1])

# 89

# import random
# def number(n,text = ''):
#     while len(text) + 1 <= n :
#         text += random.choice('qwertyuiooooooooooooopalskjfgvzcxbnm')
#     if n > 12:
#         text = ''
#     return text
# n = int(input('Enter number:'))
# print(number(n))

# 93

# def patuhan(s, w):
#     if len(s) >= len(w):
#         return s,w
#     else:
#         s = len(s) // 2
#         return s * ' ',w,s * ' '
# s = input('enter prabel: ')
# w = input('enter w: ')
# print(patuhan(s,w))

# 94

# def erankyun(koxm1, koxm2, koxm3):
#     if koxm1 <= 0 or koxm2 <= 0 or koxm3 <= 0:
#         return False
#     if koxm1 + koxm2 > koxm3 and koxm2 + koxm3 > koxm1 and koxm1 + koxm3 > koxm2:
#         return True
#     else:
#         return False
# koxm1 = int(input('Enter number: '))    
# koxm2 = int(input('Enter number: '))
# koxm3 = int(input('Enter number: '))
# print(erankyun(koxm1,koxm2, koxm3))

# 95 ?????????

# strok = 'what time do i have to be there? whats the address? this time ill try to be on time!' 
# char = 's'
# print(strok)
# def text():    
#     for i in strok:
#         if i in char: 
#             i += i.istitle()
#             return strok.capitalize()
# print(text())

# 98 ?????????????????????

# n = 0
# def number():
#     for i in range(1, 101):
#         n = 0
#         for j in range(2, (i // 2 + 1)):
#             if(i % j == 0):
#                 n =  n + 1
#     if (n == 0 and i != 1):
#           print(n)
# number()

# for Number in range (1, 101):
#     count = 0
#     for i in range(2, (Number//2 + 1)):
#         if(Number % i == 0):
#             count = count + 1
#     if (count == 0 and Number != 1):
#         print(Number, end = ' ')

