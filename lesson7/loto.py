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


class Bochonok:
    '''
    класс Мешок с бочонками
    '''

    def __init__(self):
        self.container = []
        for i in range(1, 91):
            self.container.append(i)

    def get_number(self, container):
        '''
        получаем рандомое число, удаляем его из контейнера, чтобы избежать повторений
        :return: рандомое число
        '''
        number = random.choice(container)
        container.remove(number)
        return number


class Lottery_card:
    def __init__(self, name):
        self.bochonok = Bochonok()
        self.card = [[],[],[]]
        self.make_card()  # лотерейный билет
        self.__name = name

    def make_card(self):
        '''
        создает лотерейную карточку
        -выбирает позиции на карточке, которые будут заполнены
        -выбирает список номеров, которыми эти позиции будут заполнены
        -заполняет карточку
        '''
        # заполняем карточку нулями
        for i in range(0, 27):
            self.card[i%3].append(" ")
        list_of_numbers = []
        for i in range(0, 15):
            n = self.bochonok.get_number(self.bochonok.container)
            list_of_numbers.append(n)
        list_of_numbers.sort()

        for i in self.card:
            while i.count(" ")>4:
                position=random.randint(0,8)
                if i[position]==" ":
                    i[position]="_"

        counter=0
        for i in range(0,9):
            for j in range(0,3):
                if self.card[j][i]=="_":
                    self.card[j][i]=list_of_numbers[counter]
                    counter+=1

    def get_name(self):
        return self.__name

    def print_card(self):
        '''
        вывод карточки
        '''
        print("-- {}'s lottery card ---".format(self.__name))
        for i in self.card:
            print("{0[0]:>2} {0[1]:>2} {0[2]:>2} {0[3]:>2} {0[4]:>2} {0[5]:>2} {0[6]:>2} {0[7]:>2} {0[8]:>2}".format(i))
        print("--------------------------")

    def check_the_win(self):
        '''
        Проверка на выигрыш
        :return:в случае победы возвращает строку с победителем, иначе пустую строку
        '''
        n = self.find_number("-")
        if n == 15:
            return "win"
        else:
            return ""

    def find_number(self, number):
        n=0
        for i in self.card:
            if i.count(number)>0:
                n=i.count(number)
        return n

class Card_for_computer(Lottery_card):
    '''
    класс Лотерейная карточка компьютера
    '''

    def __init__(self, name):
        super().__init__(name)

    def cross_the_number(self, number):
        '''
        зачеркивает номера в карточке
        :param number: номер, который необходимо зачеркнуть
        '''
        n = self.find_number(number)
        if n == 1:
            for i in range(len(self.card)):
                for j in range(len(self.card[i])):
                    if self.card[i][j]==number:
                        self.card[i][j] = "-"


class Card_for_player(Lottery_card):
    '''
    класс Лотерейная карточка игрока
    '''

    def __init__(self, name):
        super().__init__(name)

    def cross_the_number(self, number, answer):
        '''
        Зачеркивает номера в карточке с учетом ответа,
        в случае неверного ответа побеждает компьтер
        :param number: номер, который нужно зачеркнуть
        :param answer: ответ игрока
        :return: в случае победы возвращает строку с победителем, иначе пустую строку
        '''
        n=self.find_number(number)
        if n == 1 and answer == "y":
            for i in range(len(self.card)):
                for j in range(len(self.card[i])):
                    if self.card[i][j]==number:
                        self.card[i][j] = "-"
            return ""
        elif (n == 1 and answer == "n") or (n == 0 and answer == "y"):
            print(n)
            return "error"
        else:
            return ""


player = Card_for_player("Player")
computer = Card_for_computer("Computer")
b = Bochonok()
winner = ""
list_of_bochonki = []

while winner == "":
    print("\n\n=================== turn - {} ====================".format(len(list_of_bochonki) + 1))
    print("Ранее выпали номера: {}".format(list_of_bochonki))
    player.print_card()
    computer.print_card()
    number = b.get_number(b.container)
    list_of_bochonki.append(number)
    print("Выпал номер: {}".format(number))
    computer.cross_the_number(number)
    answer = input("Зачеркнуть выпавший номер? (y/n)")
    # проверка ответа игрока
    while answer != "y" and answer != "n":
        answer = input("Зачеркнуть выпавший номер? (y/n)")

    condition1 = player.cross_the_number(number, answer)
    condition2 = computer.check_the_win()
    condition3 = player.check_the_win()
    if condition1 == "error":
        print("NO,NO,NO!")
        winner = computer.get_name()
    elif condition2 == "win" and condition3 == "win":
        print("Both win! so strange...")
        winner = "Friendship"
    elif condition2 == "win":
        winner = computer.get_name()
    elif condition3 == "win":
        winner = player.get_name()
    if winner != "":
        print("{} wins!!!".format(winner))
