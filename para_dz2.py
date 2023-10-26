"""
Таблица умножения
Домашнее задание 
● Условие: На вход подается число n. 
● Задача: Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n. 
Обоснуйте выбор парадигм. 
● Пример вывода: 
1 * 1 = 1 
1 * 2 = 2 
1 * 3 = 3 
1 * 4 = 4 
1 * 5 = 5 
1 * 6 = 6 .. 
1 * 9 = 9
"""

def mult_table_for_one_number(number):
    for i in range(1,11):
        print(f"{number} * {i} = {number * i}")

if __name__ == '__main__':
    num = int(input('Введите число: '))

    mult_table_for_one_number(num)

