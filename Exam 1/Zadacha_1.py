#С клавиатуры вводится 7 значное число.
#Если четных цифр в нем больше, чем нечетных, то найти сумму всех его цифр
#если нечетных больше, то найти произведение 1 3 и 6 цифры.

n = int(input("Вводим семизначное значение: "))  # вводим 7-ми значное число
#numbers = [n // 1000000, (n // 100000) % 10, (n // 10000) % 10, (n // 1000) % 10, (n // 100) % 10, (n // 10) % 10,
           #n % 10]  # находим каждое цифру в числе (отделяем их друг от друга)
chet = 0
nechet = 0

while n > 0:
    if a % 2 == 0:
        chet += 1
    else:
        nechet += 1
    n = [n // 1000000, (n // 100000) % 10, (n // 10000) % 10, (n // 1000) % 10, (n // 100) % 10, (n // 10) % 10,
           n % 10]
    print(numbers[0] * numbers[2] * numbers[5])