import random

chars = '+-/*!&$#?=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

number = int(input('Введите количество символов\n'))
length = int(input('Введите длину пароля\n'))

for x in range(number):
    password = ''

    for j in range(length):
        password += random.choice(chars)

    print(password)

    file = open('password.txt', 'a')
    file.write('\n' + password)
