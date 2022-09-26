# for x in range (2):
#     for y in range (2):
#         for z in range (2):
#             print((x,y,z), not (x or y or z) == (not x and not y and not z))

##########

# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

# q = int(input('Input number of Quoter :'))
#
# match q:
#     case 1:
#         print(' X > 0 and Y > 0')
#     case 2:
#         print(' X < 0 and Y > 0')
#     case 3:
#         print(' X < 0 and Y < 0')
#     case 4:
#         print(' X > 0 and Y < 0')
#     case _:
#         print('Uncorrect number')

#########

# Напишите программу, которая выводит нечетные числа из заданного списка и
# останавливается, если встречает число 554.

#Напишите программу, которая выводит нечетные числа из заданного списка и останавливается,
# если встречает число 554.
#
# import random
#
# lst=[554]
#
# for i in range(random.randint(5,15)): # сколько чисел в списке
#     x = random.randint(500,600)
#     lst.append(x) # добавляем переменную в конец списка
#
# print(lst)
# random.shuffle(lst)  # перемешали список
# print(lst)
#
# for i in lst:
#     if i %2 != 0:
#         print(i)
#     if i == 554:
#         break

###########

# Сложить числа вещественного числа

# number = '5.679'
# sum = 0
# for i in number:
#     if i != '.':
#         sum += int(i)
# print(sum)
###################################

# Посчитайте, сколько раз символ встречается в строке

# # Посчитайте, сколько раз символ встречается в строке
# stroka = 'Посчитайте, сколько раз символ встречается в строке'
# simvol = 'а'
# final = 0
# for i in stroka:
#     if simvol == i:
#         final +=1
# print(final)
