# Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension
# Создайте программу для игры в ""Крестики-нолики"".
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
print("Игра в крестики нолики")
import random
def print_board(board):
    for i in range(0, len(board)):
        for i2 in range(0, len(board[i])):
            print(board[i][i2], end=" ")
        print()
def InputNumbers():
    Try = False
    while not Try:
        try:
            number = int(input("Введите ряд (от 1 до 3): ")) - 1, int(input("Введите строку ( от 1 до 2): ")) - 1
            Try = True
        except ValueError:
            print("не вписался в поле игры!")
    return number
def check_num(number, area):
    Try = False
    while not Try:
        if 0 <= number[0] < 3 and 0 <= number[1] < 3:
            if [i for i in area if i == number]:
                print("Уже было")
                number = InputNumbers()
            else:
                Try = True
        else:
            print("Вне пределов доски.")
            number = InputNumbers()
    return number
def get_o(area):
    number = (0, 0)
    while [i for i in area if i == number]:
        number = (random.randint(0, 2), random.randint(0, 2))
    return number
def check_result(board, liter):
    x = ""
    if (
        board[0][0] == board[0][1] == board[0][2] == str(liter)
        or board[1][0] == board[1][1] == board[1][2] == str(liter)
        or board[2][0] == board[2][1] == board[2][2] == str(liter)
        or board[0][0] == board[1][0] == board[2][0] == str(liter)
        or board[0][1] == board[1][1] == board[2][1] == str(liter)
        or board[0][2] == board[1][2] == board[2][2] == str(liter)
        or board[0][0] == board[1][1] == board[2][2] == str(liter)
        or board[0][2] == board[1][1] == board[2][0] == str(liter)
    ):
        x = str(liter)
    return x
area = []
area = [["."] * 3 for i in range(3)]
fill_aria = area
temp = []
print_board(area)

while len(temp) < 9:
    num = InputNumbers()
    num_x = check_num(num, temp)
    temp.append(num_x)
    fill_aria[num_x[0]][num_x[1]] = "x"
    print_board(fill_aria)
    result = check_result(fill_aria, "x")
    if result == "x":
        print("Бот приграл !")
        break
    if len(temp) == 9:
        break
    num_o = get_o(temp)
    print(f"Ход бота: {num_o[0]+1, num_o[1]+1}")
    temp.append(num_o)
    fill_aria[num_o[0]][num_o[1]] = "o"
    print_board(fill_aria)
    result = check_result(fill_aria, "o")
    if result == "o":
        print("УВЫ, бот выиграл!")
        break
print("Конец игры")

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""# Создайте программу для игры с конфетами человек против человека.
# # Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# # Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# # Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# # a) Добавьте игру против бота
# # b) Подумайте как наделить бота ""интеллектом""

import random

def candyGame(gamers, n):
    print(f'Ход игрока №{gamers}!')
    print(f'Конфет осталось: {n}')

def winGamers(gamers, n):
    print(f'Победил игрок №{gamers}!')
    return n - 1

print('Условия игры: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.')
print('Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.')
print('Все конфеты оппонента достаются сделавшему последний ход.')
print()
gamers = random.randint(1, 2)
print(f'Первый ход игрока №{gamers}!')
n = 2021
while n >= 0:
    checkInput = False
    if gamers == 1:
        candyGame(gamers, n)
        while not checkInput:
            try:
                number = int(input('Возьмите от 1 до 28 конфет: '))
                print(f'Игрок взял {number} конфет.')
                checkInput = True if 0 < number <= 28 else print('Вы вышли из диапазона!')
            except:
                print('Введите число от 1 до 28: ')
        n -= number
        if n == 0:
            n = winGamers(gamers, n)
        else:
            gamers = 2
        print()
    elif gamers == 2:
        candyGame(gamers, n)
        if n % 29 == 0:
            number2 = random.randint(1, 28)
        else:
            number2 = n % 29
        print(f'Игрок взял {number2} конфет.')
        n -= number2
        if n == 0:
            n = winGamers(gamers, n)
        else:
            gamers = 1
    print()

