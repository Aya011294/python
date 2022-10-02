# Урок 2. Знакомство с Python. Продолжение
# 1.Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
print('Задание номер 1')
lst = {}
n = int(input("Введите размер списка: "))
for i in range(1, n+1):
  if i <= n:
      key = i
      value = 3*i+1
      lst[key] = value
print(lst)

# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('Задание номер 2')
n = int(input("Введите число: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
    print(factorial, end=' ')
print(' ')
# 3.Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# - Для n = 5: сумма = 11,55
#
print('Задание номер 3')
n = int(input("Введите число: "))
sum = 0
lst = []
for i in range(0, n+1):
    if i <= n - 1:
        i += 1
        b = (1 + (1 / i)) ** i
        lst.append(b)
        sum += b
print("%.2f" % sum)

# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
print('\nЗадание номер 4')
import random
n = int(input('Введите число: '))
lst = []
for i in range(1, n + 1):
    lst.append(random.randint(-n, n))
print(lst)

with open('file.txt', 'w') as data:
    data.write("1\n")
    data.write("2\n")
path = open('file.txt')
a = int(path.read(1))
b = int(path.read(2))
path.close()
sum = lst[a] * lst[b]
print(sum)

# 5.Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)
print('\nЗадание номер 5')
import datetime
def myShuffle2(some_list):
    for i in range(0, len(some_list)-1):
        j = datetime.datetime.now().microsecond % len(some_list)-1
        some_list[j], some_list[i] = some_list[i], some_list[j]
    return some_list

print(myShuffle2([4,2,3,1,5,6]))