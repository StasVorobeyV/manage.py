#Посчитать, сколько раз встречается определенная цифра в числах. Количество
#введенных чисел и искомая цифра задаются с клавиатуры. Числа выбираются рандомно.


import random

n = int(input('Введите  количество чисел: '))
list = [random.randint(1, 20) for i in range(n)]
print(list)
num = input('Введите искомую цифру: ')
a = ''.join(map(str, list))

f = 0
for x in a:
    if x == num:
        f += 1

print('Количество повторений цифры', num, '-', f, 'раз(а).')