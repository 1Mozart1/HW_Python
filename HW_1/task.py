# Задача 2: Найдите сумму цифр трехзначного числа.--------------------------------------------------------------------

# num = int(input("Трехзначное число: "))
# res = 0
# if num > 999 or num < 100:
#     print("Не трехзначное число")
# else:
#     while num > 0:
#         a = num % 10
#         res += a
#         num = num // 10
#     print(res)


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, ----------------------
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?


# num = int(input("Введите общее кол-во журавликов: "))

# if not num % 6:
#     p = num / 6
#     c = num / 6
#     k = (c + p) * 2
#     print("Петя сделал журавликов: ", p)
#     print("Катя сделала журавликов: ", k)
#     print("Сережа сделал журавликов: ", c)
# else:
#     print("невозможно подсчитать")


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
