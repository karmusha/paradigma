"""Крестики-нолики
    1   2   3
   --- --- ---
1 | x | x | x |
   --- --- ---
2 | x | x | x |
   --- --- ---
3 | x | x | x |
   --- --- ---
"""

import random
from itertools import takewhile

def print_mas(mas):
    for line in mas:
        print(' | '.join(list(map(str, line))))
        print("\033[0m{}".format('---------'))

def get_winner(mas):
    match mas:
        case mas if mas[0][0] == mas[0][1] == mas[0][2] and mas[0][2] != ' ': return mas[0][2]
        case mas if mas[1][0] == mas[1][1] == mas[1][2] and mas[1][2] != ' ': return mas[1][2]
        case mas if mas[2][0] == mas[2][1] == mas[2][2] and mas[2][2] != ' ': return mas[2][2]
        case mas if mas[0][0] == mas[1][0] == mas[2][0] and mas[2][0] != ' ': return mas[2][0]
        case mas if mas[0][1] == mas[1][1] == mas[2][1] and mas[2][1] != ' ': return mas[2][1]
        case mas if mas[0][2] == mas[1][2] == mas[2][2] and mas[2][2] != ' ': return mas[2][2]

        case mas if mas[0][0] == mas[1][1] == mas[2][2] and mas[2][2] != ' ': return mas[2][2]
        case mas if mas[0][2] == mas[1][1] == mas[2][0] and mas[2][2] != ' ': return mas[2][2]
    
    return None

def check_mas_filled(mas):
    for line in mas:
        for i in line:
            if i == ' ':
                return False
    
    return True

def get_readble_sign(sign: str):
    if sign ==  'x':
        return 'крестик'
    
    if sign == 'o':
        return 'нолик'

    return 'unknown sign'

def hod(player_name: str, sign: str, mas):
    while True:
        try:
            i, j = tuple(map(int, input(f'{player_name}, ваш ход. Введите через запятую номер строки и столбика, куда хотите поставить {get_readble_sign(sign)}.\n').split(",")))
            if (i, j) == (0, 0):
                print('No')
                continue
            i -= 1
            j -= 1
            if mas[i][j] == 'x' or mas[i][j] == 'o':
                print('Здесь уже занято. Попробуйте другое поле.')
                continue
            mas[i][j] = sign
        except ValueError:
            print('Вы ввели неверно. Попробуйте ещё раз.')
            continue
        except IndexError:
            print('Вы ввели неверно. Попробуйте ещё раз.')
            continue
        break
    return mas


def get_player_name_by_sign(players, sign: str):
    res = list(takewhile(lambda x: x[1] == sign, players))
    return res[0][0]


def next_player_number(current_player_number: int):
    res = 0
    if current_player_number == 0:
        res = 1
    else:
        res = 0
    
    return res


# --- Game ---   
print('КРЕСТИКИ НОЛИКИ')

print(f'Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики). Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает. Первый ход делает игрок, ставящий крестики.')

player1 = input('Игрок 1, введите своё имя:\n')
player2 = input('Игрок 2, введите своё имя:\n')

# player1 = 'Karma'
# player2 = 'Sergey'

input('Кидаем жребий, у кого выпадет большее число, тот ходит первым и ставит крестики. Нажмите Enter.')
while True:
    random_number1 = random.randint(1,6)
    random_number2 = random.randint(1,6)

    print(f'{player1} выпало: {random_number1}')
    print(f'{player2} выпало: {random_number2}')

    if random_number1 > random_number2:
        player1, player2 = player1, player2
        break
    elif random_number1 < random_number2:
        player1, player2 = player2, player1
        break
    
    input('кидаем жребий еще разок. Нажмите Enter')

players = [(player1, 'x'), (player2, 'o')]

mas = [
    [' ', ' ', ' '], 
    [' ', ' ', ' '], 
    [' ', ' ', ' '],
]

print_mas(mas)

player_number = 0
while True:
    player, sign = players[player_number]
    mas = hod(player, sign, mas)

    print_mas(mas)

    match get_winner(mas):
        case sign if sign in ['x', 'o']:
            print(f'{get_player_name_by_sign(players, sign)} победитель')
            break
        case None:
            player_number = next_player_number(player_number)
    
    if check_mas_filled(mas):
        print(f'ничья')
        break

print('Спасибо за игру!\n')
input('Нажмите любую клавишу, чтобы выйти.')
