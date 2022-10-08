str = '66 7 34 0 9'
lst = str.split(sep=' ')
max = int(lst[0])
min = int(lst[0])
print(lst)
for i in range(len(lst)):
    lst[i] = int(lst[i])
for i in range(1,len(lst)):
    if lst[i] > max:
        max = lst[i]
    if lst[i] < min:
        min = lst[i]
print(f'Максимальное число -{max}, Минимальное число - {min}')


########

# Найдите корни квадратного уравнения Ax² + Bx + C = 0

a = int(input ('введите число a '))
b = int(input ('введите число b '))
c = int(input ('введите число c '))
d = b**2-4*a*c
if d>0:
    x1 = (-b+d**0.5)/(2*a)
    x2 = (-b-d**0.5)/(2*a)
    print (x1,x2)
elif d == 0:
    x1 = -b/(2*a)
    print(x1)
else:
    print('Уравнение не имеет решений')

# найти библиотеку* для уравнения выше

# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a = int(input('Input A :'))
b = int(input('Input B :'))

nod = 2
while True:
    if b%nod == 0 and a%nod == 0:
        print(nod)
        break
    else:
        nod +=1

if a > b:
    nok = a
else:
    nok = b

while True:
    if nok%b == 0 and nok%a == 0:
        print(nok)
        break
    else:
        nok += 1

