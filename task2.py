# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений
# предикат.



x = int (input('Введите х: '))
y = int (input('Введите y: '))
z = int (input('Введите z: '))

xyz = [x,y,z]

def Predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result

if x == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")