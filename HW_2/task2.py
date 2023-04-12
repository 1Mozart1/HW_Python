x = int(input("Введите число х "))
y = int(input("Введите число у "))

if x < 1 or x > 1000 or y < 1 or y > 1000:
    print("Вне диапозона")
else:
    flag = 0
    for i in range(1001):
        if flag != 1:
            for j in range(1001):
                if flag != 1:
                    if i + j == x and i * j == y:
                        print(i, j)
                        flag = 1