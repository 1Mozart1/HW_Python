# Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел A i
# Последняя строка содержит число X

import random
s = int(input("Введите размер массива: "))
lst = [random.randint(0, 100) for _ in range(s)]
print(lst)
x = int(input("Введите искомое число: "))
index = 0
min1 = abs(x - lst[0])
for i in range(1, s):
    found = abs(x - lst[i])
    if found < min1:
        min1 = found
        index = i
print("Самый близкий по величине элемент ", lst[index])

# --- ИЛИ

# import random
# s = int(input("Введите размер массива: "))
# lst = [random.randint(0, 100) for _ in range(s)]
# print(lst)
# x = int(input("Введите искомое число: "))
# m = min(lst, key = lambda i: abs(i-x))
# print(m)