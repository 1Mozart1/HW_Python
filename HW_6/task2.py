# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
s = int(input("Введите размер массива: "))
lst = [random.randint(-10, 10) for _ in range(s)]
print(lst)
min_n = int(input("Начало диапозона: "))
max_n = int(input("Конец диапозона: "))
lst_res = []
for i in range(len(lst)):
    if (min_n - 1) < lst[i] < max_n:
        lst_res.append(i)
print(sorted(lst_res))