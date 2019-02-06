#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random
class Randomizer:
    def __init__(self):
        self.container=[]
        for i in range (1,91):
            self.container.append(i)

    def get_number(self,container):
        '''
        получаем рандомое число, удаляем его из контейнера, чтобы избежать повторений
        :return: рандомое число
        '''
        number=random.choice(container)
        container.remove(number)
        return number

class Bochonok(Randomizer):
    '''
    класс Мешок с бочонками
    '''
    def __init__(self):
        super().__init__()

class Card_for_computer(Randomizer):
    '''
    класс Лотерейная картока компьютера
    '''
    def __init__(self):
        super().__init__()
        self.card=[] #лотерейный билет
        self.make_card()

    def make_card(self):
        '''
        создает лотерейную карточку
        -выбирает позиции на карточке, которые будут заполнены
        -выбирает список номеров, которыми эти позиции будут заполнены
        -заполняет карточку
        '''
        list_of_positions=[]
        for i in range(0,27):
            list_of_positions.append(i)
            self.card.append(" ")
        list_of_numbers=[]
        new_list_of_positions=[]
        for i in range(0,15):
            m=self.get_number(list_of_positions)
            n=self.get_number(self.container)
            list_of_numbers.append(n)
            new_list_of_positions.append(m)
        list_of_numbers.sort()
        new_list_of_positions.sort()
        counter=0
        for i in new_list_of_positions:
            self.card[i]=list_of_numbers[counter]
            counter+=1

    def print_card(self):
        '''
        вывод карточки
        '''
        print("-- Карточка компьютера ---")
        s=["","",""]
        counter=0
        for i in self.card:
            if i!=" " and i!="- ":
                if int(i)//10 == 0:
                    s[counter % 3] += str(i) + "  "
                else:
                    s[counter % 3] += str(i) + " "
            elif i==" ":
                s[counter % 3] += str(i) + "  "
            else:
                s[counter % 3] += str(i) + " "
            counter+=1
        for i in s:
            print (i)
        print("--------------------------")

    def cross_the_number(self,number):
        '''
        зачеркивает номера в карточке
        :param number: номер, который необходимо зачеркнуть
        '''
        n=self.card.count(number)
        if n==1:
            self.card[self.card.index(number)]="- "

    def check_the_win(self):
        '''
        Проверка на выигрыш
        :return:
        '''
        n = self.card.count("- ")
        if n==15:
            return "computer wins!!!"
        else:
            return ""

class Card_for_player(Card_for_computer):
    '''
    класс Лотерейная карточка игрока
    '''
    def __init__(self):
        super().__init__()

    def print_card(self):
        '''
        Вывод карточки игрока
        '''
        print("------ Ваша карточка -----")
        s = ["", "", ""]
        counter = 0
        for i in self.card:
            if i != " " and i!="- ":
                if int(i) // 10 == 0:
                    s[counter % 3] += str(i) + "  "
                else:
                    s[counter % 3] += str(i) + " "
            elif i==" ":
                s[counter % 3] += str(i) + "  "
            else:
                s[counter % 3] += str(i) + " "
            counter += 1
        for i in s:
            print(i)
        print("--------------------------")

    def cross_the_number(self,number,answer):
        '''
        Зачеркивает номера в карточке с учетом ответа,
        в случае неверного ответа побеждает компьтер
        :param number: номер, который нужно зачеркнуть
        :param answer: ответ игрока
        :return:
        '''
        n=self.card.count(number)
        if n==1 and answer=="y":
            self.card[self.card.index(number)]="- "
            return ""
        elif (n==1 and answer=="n")or(n==0 and answer=="y"):
            return "computer wins!!!"
        else:
            return ""

    def check_the_win(self):
        '''
        проверка выигрыша
        :return:
        '''
        n = self.card.count("- ")
        if n==15:
            return "player wins!!!"
        else:
            return ""

player=Card_for_player()
computer=Card_for_computer()
b=Bochonok()
winner=""
list_of_bochonki=[]

while winner=="":
    print("=======================================")
    print("Ранее выпали бочонки: {}".format(list_of_bochonki))
    player.print_card()
    computer.print_card()
    number=b.get_number(b.container)
    list_of_bochonki.append(number)
    print("Выпал бочонок: {}".format(number))
    computer.cross_the_number(number)
    answer=input("Зачеркнуть цифру? (y/n)")
    winner=player.cross_the_number(number,answer)
    if winner!="":
        print(winner)
        break
    winner=computer.check_the_win()
    if winner!="":
        print(winner)
        break
    winner=player.check_the_win()
    if winner!="":
        print(winner)
        break