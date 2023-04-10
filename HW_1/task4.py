# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).---------------------------------

n = int(input("Введите кол-во долек по длине: "))
m = int(input("Введите кол-во долек по ширине: "))
k = int(input("Введите количество долек, которое хотите отломить: "))

if k > n * m:
    print("Нельзя отломить долек больше размера шоколадки")
else:
    if k % n == 0 or k % m == 0:
        print("Можно отломить", k, "долек(и) сделав один разлом")
    else:
        print("Нельзя отломить", k, "долек(и) сделав один разлом")