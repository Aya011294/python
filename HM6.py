# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение
# Формат: Объясняет преподаватель
# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# 3 Исправленные задачи на Отлично!
# Доп задача:
# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
print('*Task 1')
s = (input('Введите арифметическое выражение  '))
def parse(s: str) -> list:
    result = []
    digit =''
    for symbol in s:
        if symbol.isdigit():
            digit += symbol
        elif symbol in [')', '(']:
            if digit:
                result.append(float(digit))
                digit = ''
            result.append(symbol)
        else:
            if digit:
                result.append(float(digit))
            digit = ''
            result.append(symbol)
    else:
        if digit:
            result.append(float(digit))
    return result
def calculate(lst: list) -> float:
    result = 0.0
    while '*' in lst:
        index = lst.index('*')
        result = lst[index - 1] * lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '/' in lst:
        index = lst.index('/')
        result = lst[index - 1] / lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '+' in lst:
        index = lst.index('+')
        result = lst[index - 1] + lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '-' in lst:
        index = lst.index('-')
        result = lst[index - 1] - lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result
def brackets(lst: list) -> list:
    while '(' in lst:
        opening = lst.index('(')
        closing = lst.index(')')
        lst = lst[:opening] + [calculate(lst[opening + 1:closing])] + lst[closing + 1:]
    return lst

result = parse(s)
print(calculate(result))

# # Задача со второго семинара - 3.Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# # Пример:
# # - Для n = 5: сумма = 11,55
# #
print('Task 2')
n = int(input("Введите число: "))
sum = 0
from functools import reduce
sum = 0
sum = reduce(
     (lambda x,y: x+y),
    list(map(lambda x: (1 + 1/ x)**x, range(1,n+1))))
print("%.2f" % sum)

# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
print('Task 3')
from random import randint
lst = []
for i in range(randint (1, 10)):
    lst.append(randint (1, 10))
print(lst)
def sum_odd(array):
    return sum([item for index, item in enumerate(array) if index % 2 == 1])
print(sum_odd(lst))


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
print('Task 4')
import math

a = int(input("Введите число N: "))
b = list(map(lambda x: math.factorial(x), range(1, a + 1)))
print(b)