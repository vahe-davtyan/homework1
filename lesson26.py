def func():
    try :
        n = int(input('Enter number: '))
        k = n - 1
        for i in range(1, n + 1):
            number = 1
            for j in range(0, k):
                print(end=" ")
            k = k - 1
            for j in range(1, i + 1):
                print(number, end=' ')
                number = number * (i - j) // j
            print('\r')
    except ValueError:
        print('Enter number')
func()