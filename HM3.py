# Урок 3. Данные, функции и модули в Python
#   1.Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
print('Task №1')
from random import randint
lst = []
for i in range(randint (1, 10)):
    lst.append(randint (1, 10))
print(lst)
sum = 0
for i in range(len(lst)):
    if i%2 == 1:
        sum+= lst[i]
print(sum)

# 2.Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
print('Task №2')
from random import randint
lst = []
for i in range(randint(3, 9)):
    lst.append(randint(1, 9))
print(lst)
for i in range(len(lst)):
    if i>=len(lst)/2:
        break
    print(lst[i] * lst[-i-1], end = ' ')
print(" ")
# 3.Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
print('Task №3')
import random
lst = [round(random.uniform(0, 10), 2) for lst in range(5)]
print(lst)
lst1 = [round(i%1,2) for i in lst if i%1 !=0]
print(max(lst1)-min(lst1))

# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
print('Task №4')
n = int(input())
print(bin(n))

# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи](https://ru.wikipedia.org/wiki/
# %D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:
# text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%
# D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%
# 80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%
# B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%
# BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%
# BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%
# D0%BD%D0%B0%D1%87%D1%87%D0%B8.)
print('Task №5')
n = int(input())
def get_fib(n):
    fn = []
    a, b = 1, 1
    for i in range (n+1-1):
        fn.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n +1):
        fn.insert(0, a)
        a, b = b, a - b
    return fn
fn = get_fib(n)
print(get_fib(n))
