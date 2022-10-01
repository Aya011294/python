# # №2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# # Пример: N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# n = int(input('Введите число n '))
# proizvedenie = 1
# for i in range(1, n+1):
# proizvedenie *=i
# print(proizvedenie, end = ' ')


#########

# a = int(input("Введите число N: "))
# i = 0
# x = 0
# lst = []
# while i <= a - 1:
# i += 1
# b = (1 + (1 / i)) ** i
# lst.append(b)
# x = x + b
# print("Список последовательных чисел числа N:", lst)
# print("Сумма последовательных чисел числа N по формуле (1+ (1/n))^n равна", round(x, 2)


###########

rint('\nTask4')
import random

n4 = int(input('Введите N: '))
lst4 = []
for i in range(1, n4+1):
lst4.append(random.randint(-n4,n4))
print(lst4)

f = open('file.txt')
ind1 = int(f.read(1))
ind2 = int(f.read(2))
f.close()
print(f'Indexes from file.txt: {ind1}, {ind2}')

mult4 = lst4[ind1] * lst4[ind2]
print(mult4)



###########

mport math
# Линейный конгруэнтный метод

m=32768
a=23
b=12345
# a=a1+a10*10 # случайный выбор множителя (это мои пробы)
# # можно еще попробовать случайно выбирать из массива рекомендованных констант
#
# def lin_rand_arr_flxd(seed,size):
# if size==1:
# return math.ceil(math.fmod(a*math.ceil(seed)+b,m))
# r=[0 for i in range(size)]
# r[0]=math.ceil(seed)
# for i in range(1,size):
# r[i]=math.ceil(math.fmod((a*r[i-1]+b),m))
# return r[1:size]
#
# arr5 = (lin_rand_arr_flxd(time.time(),len(lst5)+1))
# print(arr5)
# def selection_sort(arr_mix, arr):
# for i in range(len(arr)):
# minimum = i
#
# for j in range(i + 1, len(arr)):
# # Выбор наименьшего значения
# if arr[j] < arr[minimum]:
# minimum = j
#
# # Помещаем это перед отсортированным концом массива
# arr[minimum], arr[i] = arr[i], arr[minimum]
# arr_mix[minimum], arr_mix[i] = arr_mix[i], arr_mix[minimum]
# # здесь первичный массив сортируем вместе со случайным...
#
# return arr_mix
# print(lst5)
# print(selection_sort(lst5, arr5))

# import datetime
#
#
# j = datetime.datetime.now().microsecond % 1000 # текущее время в микросекундах
# print(j)



#сам урок

# 1.Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

stroka1 = 'Привет как у вас дела Привет'
stroka2 = 'Привет'
lst = stroka1.split (sep=' ')
print(lst)
count = 0
  for i in range (len(lst)):
    if lst[i] == stroka2:
      count+=1
print(count)

# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

list1 = ["123", "234", 123, "567"]
stroka1 = '123'
count = 0
for i in range(len(list1)):
if list1[i] == stroka1:
count+=1
if count ==2:
print (i)
break
if count != 2:
print(-1)


