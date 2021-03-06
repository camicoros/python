# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print("\nTask1")
myFridge = ["яблоко", "банан", "киви", "арбуз"]
number=0
for meal in myFridge:
    number+=1
    print("{}. {:>7}".format(number,meal))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
print("\nTask2")
List1=[1,2,3,4,5,6]
List2=[1,2,3]
for i in List2:
    kolich=List1.count(i)
    for j in range(0,kolich):
        List1.remove(i)
print("List1: ",List1)
print("List2: ",List2)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
print("\nTask3")
List1=[1,2,3,4,5,6,7,8]
List2=[]
for i in List1:
    k=i%2
    if (k==0):
        List2.append(i/4)
    else:
        List2.append(i*2)
print("List2: ", List2)