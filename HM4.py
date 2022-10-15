# Урок 4. Данные, функции и модули в Python. Продолжение
# 1.Вычислить число c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
print('Task 1')
from math import pi
p = float(input())
l = pi
a = int(l/p)
n = float(a*p)
print(n)
# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
print('Task 2')
def Factor(n):
    lst = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            lst.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        lst.append(n)
    return lst
print(Factor(int(input('Введите число '))))
# 3.Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности.
print('Task 3')
import random
lst = []
for i in range(10):
    lst.append(random.randint(1, 10))
print(lst)
lst2 = []
count = 0
for i in lst:
    if lst.count(i) == 1:
        lst2.append(i)
print(lst2)

# 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:  - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
print('Task 4')
from random import randint

def create_polynomial (k):
    new_list = []
    while k >= 0:
        ratio = randint(0, 101)
        if ratio != 0:
            if k > 1:
                new_list.append(str(f'{ratio}*x^{k} + '))
            elif k == 1:
                new_list.append(str(f'{ratio}*x + '))
            elif k == 0:
                new_list.append(str(f'{ratio} = 0'))
        k -= 1
    polynomial = ''
    for i in range(0, len(new_list)):
        polynomial += new_list[i]
    print(polynomial)
    return polynomial

def create_polynomial (k):
    new_list = []
    while k >= 0:
        ratio = randint(0, 101)
        if ratio != 0:
            if k > 1:
                new_list.append(str(f'{ratio}*x^{k}'))
            elif k == 1:
                new_list.append(str(f'{ratio}*x'))
            elif k == 0:
                new_list.append(str(f'{ratio}'))
        elif ratio == 0 and k == 0:
            new_list.append(0)
        k -= 1
    polynomial = ''
    if new_list[-1] != 0:
        for i in range(0, len(new_list) - 1):
            polynomial += new_list[i] + ' + '
        polynomial += new_list[-1] + ' = 0'
    else:
        for i in range(0, len(new_list) - 2):
            polynomial += new_list[i] + ' + '
            print(new_list[i])
        new_list[-1] = ' = 0'
        polynomial += new_list[-2] + new_list[-1]
    return polynomial

k = int(input('Введите натуральное число для степени k: '))

with open('polynomial_1.txt', 'w+') as file_1:
    file_1.write(create_polynomial(k))
    file_1.seek(0)
    print(file_1.read())

with open('polynomial_2.txt', 'w+') as file_2:
    file_2.write(create_polynomial(3))
    file_2.seek(0)
    print(file_2.read())

# Задача 5
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
print('Task 5')
def get_pol_from_file(file):
    with open(str(file), 'r') as f:
        f.seek(0)
        new_str = f.read()
        print(f'Многочлен из файла: {new_str}')
    return new_str

def prepare_str(new_str):
    import re
    new_str = new_str.replace(' = 0', '')
    new_str = re.sub("[*|^| ]", "", new_str).split('+')
    for i in range(len(new_str)):
        if new_str[i][-1] == 'x':
            new_str[i] += '1'
        if not 'x' in new_str[i]:
            new_str[i] += 'x0'
    for i in range(len(new_str)):
        new_str[i] = new_str[i].split('x')
    print(f'Подготовленный список: {new_str}')
    return new_str

def get_pol_sum(list_1, list_2):
    len_1 = len(list_1)
    len_2 = len(list_2)
    if len_1 > len_2:
        sum_list = list_1.copy()
        for i in range(len(sum_list)):
            for j in range(len(list_2)):
                if int(sum_list[i][1]) == int(list_2[j][1]):
                    sum_list[i][0] = int(sum_list[i][0]) + int(list_2[j][0])
    else:
        sum_list = list_2.copy()
        for i in range(len(sum_list)):
            for j in range(len(list_1)):
                if int(sum_list[i][1]) == int(list_1[j][1]):
                    sum_list[i][0] = int(sum_list[i][0]) + int(list_1[j][0])
    print(f'Результирующий список: {sum_list}')
    return sum_list

def compile_pol(list):
    pol_str = ''
    for i in range(len(list) - 2):
        pol_str += str(list[i][0]) + '*x^' + list[i][1] + ' + '
    pol_str += str(list[-2][0]) + '*x' + ' + '
    pol_str += str(list[-1][0]) + ' = 0'
    print(f'Итоговый многочлен: {pol_str}')
    return pol_str

def write_to_file(new_str):
    with open('task_5_result.txt', 'w') as f:
        f.write(new_str)

pol_1 = get_pol_from_file('polynomial_1.txt')
pol_2 = get_pol_from_file('polynomial_2.txt')
new_list_1 = prepare_str(pol_1)
new_list_2 = prepare_str(pol_2)
result_list = get_pol_sum(new_list_1, new_list_2)
result_str = compile_pol(result_list)
write_to_file(result_str)