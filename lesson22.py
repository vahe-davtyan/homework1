# 95

# def text_name(text):
#     text_list = text.split()
#     for i in text_list:
#         print(i,'',end = '')
#         if '?' in i:
#             index = text_list.index(i)
#             index += 1
#             print(text_list[index].capitalize(),(0 * text_list.pop(index)),end = '')
# text = 'what time do i have to be there? what’s the address? this time i’ll try to be on time!'.capitalize()
# text_name(text)

# 97

# def precedence(text):
#     dic = {
#         1 : '+',
#         2 : '-',
#         3 : '/',
#         4 : '*',
#         5 : '^',
#     }
#     count = 0
#     for i in dic.values():
#         if  i in text:
#             count += 1
#         if count == 5:
#             print(f'1 <{dic[1]} {dic[2]}> 2 <{dic[3]} {dic[4]}> 3 <{dic[5]}> ')
#             break
#     else:
#         print(-1)
# text = '+-/^'   
# precedence(text) 

# 101

# import random

# alpha = 'qwertyuaiopsdfghjklzxcvbnm'
# number_list = []
# text_list = []
# new_number = []
# count = 0
# for i in range(0,3):
#     text_list.append(*random.choices(alpha))
#     number_list.append(random.randint(0,9))
# new_number.append(number_list)
# new_number.append(random.randint(0,9))
# print(f'{text_list}{number_list}\n{new_number}{text_list}')

# def hamaranish(alpha):
#     number = random.randint(0,9)
#     for i in range(0,3):
#         print(random.choice(alpha),random.randint(alpha))
# alpha = 'qwertyuaiopsdfghjklzxcvbnm'
# hamaranish()

# 102

# def parol(text):
#     count_alpha_mec = 0
#     count_alpha_poqr = 0
#     count_number = 0
#     for i in text:
#         if i.isupper() == False:
#             if i.isdigit() == False:
#                 count_alpha_poqr += 1 
#         if i.isupper() == True:
#             count_alpha_mec += 1
#         if i.isdigit() == True:
#             count_number += 1
#     # print(count_alpha_mec,count_alpha_poqr,count_number)
#     sum = count_alpha_mec + count_alpha_poqr + count_number
#     # print(sum)
#     if count_alpha_poqr == 0 or count_alpha_mec == 0 or count_number == 0:
#         print(False)
#     elif sum >= 8:
#         print(text)
# text = input('Enter parol:')

# # 100

# import random

# def ascii():
#     number = random.randint(1,10)
#     asci = "!''#$%&'()*+,-_/0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^abcdefghijklmnopqrstuvwxyz{|}~"
#     for i in range(0,number):
#         if number >= 7 and number <= 10:
#             print(random.choice(asci),end= '')
#         else:
#             print(False)
#             break

# 103

# def code():
#     parol_asci = ascii()
#     parol_text = parol(text)
#     if parol_asci != True and parol_text == True:
#         print(parol_text)
# code()

# 107
    
# def number(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# a = int(input('Enter number:'))
# b = int(input('Enter number: '))

# k = number(a, b)
# p = a // k
# q = b // k
# if p == q:
#     print(p)
# else:
#     print(f'{p}/{q}')

# 108,109????