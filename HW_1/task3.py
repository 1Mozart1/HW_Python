# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.---------------

num = input("Введите номер билета: ")
if len(num) != 6:
    print("Такой билет нельзя проверить")
else:
    l = int(num[0]) + int(num[1]) + int(num[2])
    r = int(num[3]) + int(num[4]) + int(num[5])
    if l == r:
        print("Подравляем, у Вас счастливый билет")
    else:
        print("Повезёт в следующий раз")