# Урок 4. Данные, функции и модули в Python. Продолжение
# 1.Вычислить число c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# print('Task 1')
# from math import pi
# p = float(input())
# l = pi
# a = int(l/p)
# n = float(a*p)
# print(n)
# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# print('Task 2')
# def Factor(n):
#     lst = []
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             lst.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         lst.append(n)
#     return lst
# print(Factor(int(input('input number '))))
# 3.Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности.
# print('Task 3')
# import random
# lst = []
# for i in range(10):
#     lst.append(random.randint(1, 10))
# print(lst)
# lst2 = []
# count = 0
# for i in lst:
#     if lst.count(i) == 1:
#         lst2.append(i)
# print(lst2)

# 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:  - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# print("Task 4")
#
# from random import randint
# import itertools
#
# k = randint(2, 7)
#
# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10)
#     return ratios
#
# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')
#
#
# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print(polynom1)
#
# with open('polynom1.txt', 'w') as data:
#     data.write(polynom1)


# Второй многочлен для следующей задачи:

# k = randint (2, 5)
#
# ratios = get_ratios(k)
# polynom2 = get_polynomial(k, ratios)
# print(polynom2)
#
# with open('polynom2.txt', 'w') as data:
#     data.write(polynom2)


# 5.Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import re


def read_file(file_name):
    path = file_name
    f = open(path, "r")
    result = f.read().replace(" ", "")
    f.close()
    return result


def convert_pol(pol):
    pol = pol + "+"
    temp = []
    x = 0
    for i in re.finditer("\+|-", pol):
        temp.append(pol[x : i.start()])
        x = i.start()

    temp1 = []
    for i in temp:
        zx = i.find("x")
        if zx != -1:
            if zx == len(i) - 1:
                a = (i[0 : (zx - 1)], 1)
            else:
                a = ((i[0 : (zx - 1)]), (i[(zx + 2) : (len(i))]))
        else:
            a = ((i[0 : len(i)]), "0")
        temp1.append(a)
    return temp1


def fold_pols(pol1, pol2):
    res = []
    for i in range(len(pol1)):
        a = (pol1[i][0], pol1[i][1])
        for j in range(len(pol2)):
            if pol1[i][1] == pol2[j][1] != "":
                a = (eval(pol1[i][0] + "+" + pol2[j][0]), pol1[i][1])
        res.append(a)
    return res

def create_formula(input):
    temp = []
    for i in input:
        a = ["+", str(i[0]), "*", "x", "^", i[1]]
        temp.append(a)

    result = ""
    for i in temp:
        for j in i:
            result += str(j)

    if result[0] == "+":
        result = result[1 : len(result)]
    result = result.replace("*x^0", "")
    result = result.replace("++", "+")
    result = result.replace("+-", "-")
    result = result.replace("x^1", "x")

    return result


polynom1 = read_file("polynom1.txt")
polynom2 = read_file("polynom2.txt")
print("Formula N 1: {}".format(polynom1))
print("Formula N 2: {}".format(polynom2))


polynom11 = convert_pol(polynom1)
polynom21 = convert_pol(polynom2)

pol = fold_pols(polynom11, polynom21)

formula = create_formula(pol)

print("Result formula: {}".format(formula))