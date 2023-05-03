# 4

# def number(n):
#     reverse = int(str(n)[::-1])
#     return reverse
# n = int(input('Enter number: '))
# print(number(n))

# 5

# def count_letters(text):
#     count_text = 0
#     count_number = 0
#     for i in text:
#         if i in user_text:
#             count_number += 1
#         if i in user_number :
#             count_text += 1
#     return (f'{user_text}:{count_number},{user_number}:{count_text}')
# text = input('Enter text: ')
# user_number = input('inch tiv eq pntrum: ')
# user_text = input('inch tar eq pntrum: ')
# print(count_letters(text))

# 6

# def kordinat(x, y):
#     if x >= -1 and x <= 1 and y >= -1 and y <= 1:
#         return 'Metaxadramy inch vor tex mot e'
#     else:
#         return 'Taracqum metaxadram chka '
# x = int(input('Enter number: '))
# y = int(input('Enter number: '))
# print(kordinat(x,y))

# 7

# def numbers(n):
#     while len(n) != 1:
#         if n[0] > n[1]:
#             n.pop(0)
#         else:
#             n.pop(1)
#     return n
# n = [10, 29, 32, 41, 11, 26, 78]
# print(numbers(n))

# 8

# def bajanarar(x, y):
#     maxx = max(x,y)
#     for i in range(2,maxx):
#         if x % i == 0 and y % i == 0 :
#             mec_bajanarar = i
#     return f'Amenamec yndarun bajanarary ={mec_bajanarar}'
# x = int(input('Enter number: '))
# y = int(input('Enter number: '))
# print(bajanarar(x,y))

# 9

# import random
# '''
#     Xax N1 chunga chung
# '''
# def rock_paper_scissors(x,y):
#     if x == y:
#         return 'nichia'
#     if x == 'tuxt' and y == 'qar':
#         return x,'win'
#     if x == 'qar' and y == 'mkrat':
#         return x,'win'
#     if x == 'mkrat' and y == 'tuxt':
#         return x,'win'
#     else:
#         return y, 'win'
# '''
#     Xax N 2 Guess the number
# '''
# def guess_the_number(n):
#     number = random.randint(0,10)
#     if n == number:
#         return f'{number}\nYou win'
#     else:
#         return f'{number}\nYou lose'
# def mainMenu(xax):
#     if xax == 'xax1':
#         x = input('Enter qar or mkrat or tuxt: ')
#         y = input('Enter qar or mkrat or tuxt: ')
#         xax1 = rock_paper_scissors(x,y)
#         return xax1
#     if xax == 'xax2':
#         n = int(input('Enter number: '))
#         xax2 = guess_the_number(n)
#         return xax2
# xax = input('Write the game you want to play')
# print(mainMenu(xax))