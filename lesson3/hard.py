# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

print("\nTask1")
#функция разбивает строку на числа и знаки
def my_drob(s):
    #разбиваем строку
    elements=s.split(" ")
    znak=""
    ch1=0
    zn1=0
    ch2=0
    zn2=0
    chislo={"znak":"","celoe":"0","chislitel":"0","znamenatel":"1"}
    for element in elements:
        if element.count("/")==1:
            if element[0]=="-":
                chislo["znak"]="-"
                chislo["chislitel"]=element[1:element.index("/")]
                chislo["znamenatel"] = element[element.index("/")+1:]
            else:
                if chislo["znak"]=="":
                    chislo["znak"]="+"
                chislo["chislitel"] = element[0:element.index("/")]
                chislo["znamenatel"] = element[element.index("/")+1:]
        elif element=="-" or element=="+":
            znak=element
            #получили первое число
            ch1=float(chislo["znak"]+"1")*(float(chislo["celoe"])*float(chislo["znamenatel"])+float(chislo["chislitel"]))
            zn1=float(chislo["znamenatel"])
        else:
            if element[0]=="-":
                chislo["znak"]="-"
                chislo["celoe"]=element[1:]
            else:
                chislo["znak"]="+"
                chislo["celoe"]=element
    #получили второе число
    ch2 = float(chislo["znak"] + "1") * (float(chislo["celoe"]) * float(chislo["znamenatel"]) + float(chislo["chislitel"])) * float(znak + "1")
    zn2 = float(chislo["znamenatel"])
    #ищем общий знаменатель
    znam=1
    while znam<(zn1*zn2):
        if znam%zn1==0 and znam%zn2==0:
            break
        else:
            znam+=1
    #считаем
    ch1=ch1*(znam/zn1)
    ch2=ch2*(znam/zn2)
    ch=ch1+ch2
    #находим целую часть
    cel=int(ch/znam)
    ch=abs(ch-cel*znam)
    #сокращаем дробь
    for i in range(int(ch),1,-1):
        if ch%i==0 and znam%i==0:
            ch=ch/i
            znam=znam/i
    return str(cel)+" "+str(int(ch))+"/"+str(int(znam))

print(my_drob("-5 5/10 + -5 3/10"))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

print("\nTask2")
import os
path_to_workers=os.path.join("data","workers.txt")
workers=[]

def read_file(path):
    with open(path, "r") as w:
        mass=[]
        line = w.readline()
        words = line.split(" ")
        redact_words = []
        for word in words:
            if word != "":
                word=word.rstrip("\n")
                redact_words.append(word)
        # создаём словарь
        worker = dict.fromkeys(redact_words)
        # считываем данные
        lines = w.readlines()
        for line in lines:
            words = line.split(" ")
            redact_words = []
            for word in words:
                if word != "":
                    word = word.rstrip("\n")
                    redact_words.append(word)
            iter = 0
            for key in worker.keys():
                worker[key] = redact_words[iter]
                iter += 1
            mass.append(worker.copy())
    return mass

workers=read_file(path_to_workers)

#в файле пришлось изменить "Отработано часов" на "Отработано_часов" т.к split разделял их на разные части
path_to_hours=os.path.join("data","hours_of.txt")
hours=[]
hours=read_file(path_to_hours)

#сравниваем строки и считаем:
for worker in workers:
    for hour in hours:
        if worker["Имя"]==hour["Имя"] and worker["Фамилия"]==hour["Фамилия"]:
            salary=int(worker["Зарплата"])
            norma=int(worker["Норма_часов"])
            otrabotal=int(hour["Отработано_часов"])
            salary=salary + salary/norma*(otrabotal-norma)
            print("{} {}: {} \nразница по норме: {}".format(worker["Имя"],worker["Фамилия"],salary,otrabotal-norma))

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

print("\nTask3")
import os.path
bigLetters=list(map(chr, range(ord('А'), ord('Я')+1)))
path=os.path.join("data","fruits.txt")
folder="new_fruits"
#создаем папку, куда будем записывать новвые файлы
if not os.path.exists(folder):
    os.mkdir(folder)
#очищаем её от предыдущих использований
for root, dirs, files in os.walk(folder,topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))

with open(path,"r") as f:
    fruits = f.readlines()
    for letter in bigLetters:
        listOfFruits=[]
        for fruit in fruits:
            if letter==fruit[0].upper():
                listOfFruits.append(fruit)
        if len(listOfFruits)>0:
            pathToWrite=os.path.join(folder,"fruits_"+letter+".txt")
            with open(pathToWrite,"w",encoding="UTF-8") as w:
                w.writelines(listOfFruits.copy())
            print("В файл {} записано {} фруктов".format("fruits_"+letter, len(listOfFruits)))