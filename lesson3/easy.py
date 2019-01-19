# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили
def convert(km):
    miles=1.609*km
    print(miles)

print("\nTask1")
convert(10)

# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

print("\nTask2")
def my_round(number, ndigits):
    cel=number//1
    drob=number%1
    drob=drob//(10**(-ndigits-1))
    last=drob%10
    drob=drob//10
    if last>5:
        drob+=1
    drob=drob/(10**ndigits)
    return cel+drob

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

print("\nTask3")
def lucky_ticket(ticket_number):
    lev=ticket_number//1000
    prav=ticket_number%1000
    def sum(number):
        s=0
        while number>0:
            s+=number%10
            number=number//10
        return s
    if sum(lev)==sum(prav):
        return True
    else:
        return False


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))