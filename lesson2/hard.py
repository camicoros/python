# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

print("\nTask 1")
equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
k=""
xPosition=equation.index("x")
for i in equation[3:xPosition]:
    k+=i
k=float(k)
b=""
for i in equation[xPosition+1:]:
    if i!=" ":
        b+=i
b=float(b)
y=k*x+b
print("k = ",k)
print("b = ",b)
print("y = ",y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат

date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

print("\nTask 2")
firstPoint=date.index(".")
secondPoint=date.index(".",firstPoint+1)
print(firstPoint)
print(secondPoint)
day=int(date[:firstPoint])
mounth=int(date[firstPoint+1:secondPoint])
year=int(date[secondPoint+1:])
print(day)
print(mounth)
print(year)
bigMounth=[1,3,5,7,8,10,12]
error=0
if(mounth<1 or mounth>12):
    error+=1
if day<1 or day>31:
    error+=1
if bigMounth.count(mounth)==0 and day>30:
    error+=1
if year<1 or year>9999:
    error+=1
if error==0:
    print("correct")
else:
    print("not correct")


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

import math
print("\nTask 3")
N=int(input("введите комнату: "))
maxRoom=0 #номер последней квартиры в блоке
block=0 #номер блока квартир(1-1, 2-2,3,4,5, 3-6,7,8...)
while N>maxRoom:
    block+=1
    maxRoom+= block ** 2
minRoom=maxRoom-block**2
etaj=0 #этаж
for i in range(0,block):
    etaj+=i
etaj+=1
nomer=0 #порядковый номер слева
while minRoom<N:
    minRoom+=1
    nomer+=1
    if nomer>block:
        nomer=1
        etaj+=1
print("etaj",etaj)
print("nomer",nomer)

