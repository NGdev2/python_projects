sticks = 10
move = 0
player_1 = str(input('Введите имя первого игрока: '))
player_2 = str(input('Введите имя второго игрока: '))

while sticks > 0:
    move += 1
    if (move%2 != 0):
        print(f'ход игрока: {player_1}\nОсталось палочек: {sticks}\n')
        print('Сколько палочек вы бы хотели взять?(введите число от 1 до 3)')
        number = int(input())
        if (number > 3 or number < 1):
            print('Error value. ')
            break
        sticks -= number
        if sticks <= 0:
            print(f'Игрок {player_2} проиграл, осталось палочек: 0')
        else:
            print(f'Игрок {player_1} взял {number} палочек. Осталось {sticks} палочек')

    elif (move%2 == 0):
        print(f'ход игрока: {player_2}\nОсталось палочек: {sticks}\n')
        print('Сколько палочек вы бы хотели взять?(введите число от 1 до 3)')
        number = int(input())
        if ((number > 3) or (number < 1)):
            print('Error value. ')
            break
        sticks -= number
        if sticks <= 0:
            print(f'Игрок {player_2} проиграл, осталось 0 палочек')
        else:
            print(f'Игрок {player_2} взял {number} палочек. Осталось {sticks} палочек')