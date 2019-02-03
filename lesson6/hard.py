# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os
import re

def read_file(path):
    with open(path, "r") as w:
        #пропускаем первую строчку с заголовками
        line = w.readline()
        # считываем данные
        lines = w.readlines()
    return lines

class Worker:
    def __init__(self,line):
        self.name=line[0]
        self.secondname=line[1]
        self.salary=line[2]
        self.position=line[3]
        self.norma=line[4]
        self.extra=0

    def get_full_info(self):
        print("\n{} {}\nЗарплата:{} \nДолжность:{} \nНорма:{}\nРазница с планом:{}".format(self.name,self.secondname,self.salary,self.position,self.norma,self.extra))
    def get_salary(self,lines):
        for line in lines:
            if self.name==line[0] and self.secondname==line[1]:
                self.extra=int(line[2])-int(self.norma)
                self.salary=int(self.salary)/int(self.norma)*int(line[2])

path_to_workers=os.path.join("data","workers.txt")
lines=read_file(path_to_workers)

workers=[]
for line in lines:
    line=re.findall(r'\w+',line)
    workers.append(Worker(line))

for worker in workers:
    worker.get_full_info()

path_to_hours=os.path.join("data","hours_of.txt")
lines=read_file(path_to_hours)
new_lines=[]
for line in lines:
    line=re.findall(r'\w+',line)
    new_lines.append(line)
for worker in workers:
    worker.get_salary(new_lines)

for worker in workers:
    worker.get_full_info()