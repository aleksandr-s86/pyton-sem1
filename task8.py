"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом 
по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
"""
print("Введите количество долек по первой стороне и нажмите Enter")
n=input()
print("Введите количество долек по второй стороне нажмите Enter")
m=input()
print("Ввведите количество долек которые хотите отломить и нажмите Enter")
k =input()
if int(k)%int(n) ==0 or int(k)%int(m)==0:
    print("Шоколадка делится нацело на 2 прямоугольника")
else:
    print("Остаётся нецелый остаток от шоколадки")