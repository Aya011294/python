# # По двум заданным числам проверить является ли одно квадратом второго
# a = int(input("Введите превое чилсо: "))
# b = int(input("Введите второе чилсо: "))
# if b ** 2 == a:
#     print("Первое число является квадратом второго")
# elif a ** 2 == b:
#     print("Второе число является квадратом первого")
# else:
#     print("Числа не является квадротом друг другоа")
#
# print(b ** 2 == a or a ** 2 == b) # булево вырвжение либо правда либо лож
#
# ##########
#
# # Найти максимальное из пяти чисел
# lst = [1, 2, 8, 9, 5]
# max = lst[0]
# for i in range(0, 5): # range(len(lst)
#     if lst[i] > max:
#         max = lst[i]
# print(max)
#
# ############
#
# # Найти максимальное из пяти чисел
# lst = [1, 2, 8, 9, 5]
# max = lst[0]
# for i in range(0, 5): # range(len(lst)
#     if lst[i] > max:
#         max = lst[i]
# print(max)
#
# ############
#
# # Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# a = float(input( "Введите десятичную дробь: "))
# n = a * 10 % 10
# print(int(n))
#
# ##########
# # Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
# a = int(input("Введите чилсо N: "))
# print((a % 5 == 0 and a % 10 == 0) or (a % 15 == 0 and a % 30 != 0))
#
#
#
