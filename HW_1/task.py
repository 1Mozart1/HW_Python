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

num = int(input("Введите общее кол-во журавликов: "))

if not num % 6:
    p = num / 6
    c = num / 6
    k = (c + p) * 2
    print("Петя сделал журавликов: ", p)
    print("Катя сделала журавликов: ", k)
    print("Сережа сделал журавликов: ", c)
else:
    print("невозможно подсчитать")

