# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
print('sys.argv = ', sys.argv)

def copy_file():
    '''
    создаёт копию файла
    '''
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        with open(file_name, 'r') as f:
            s=f.read()
            with open("copy_"+file_name,'w') as g:
                g.write(s)
        print('копия {} создана'.format(file_name))
    except FileNotFoundError:
        print('файл {} не существует'.format(file_name))

def remove_file():
    '''
    удаляет файл
    '''
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        answer=input("вы действительно хотите удалить файл {}? (y/n)".format(file_name))
        if (answer=="y"):
            os.remove(file_name)
            print('файл {} удалён'.format(file_name))
        elif(answer=="n"):
            print('удаление отменено')
        else:
            print('некорректный ответ, удаление отменено')
    except FileNotFoundError:
        print('файл {} не существует'.format(file_name))

def change_dir():
    '''
    создание папки
    '''
    if not dir_name:
        print("Необходимо указать путь вторым параметром")
        return
    if os.path.exists(dir_name):
        os.system('cd '+dir_name)
        print('директория {} изменена на {}'.format(os.getcwd(),dir_name))
    else:
        print('директория {} не была изменена'.format(os.getcwd()))

def lets_see():
    '''
    отображение полного пути текущей директории
    '''
    print(os.getcwd())

def print_help():
    '''
    вывод справки по командам
    '''
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создание копии файла")
    print("rm <file_name> - удаление файла")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")

def make_dir():
    '''
    создание папки
    '''
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def ping():
    '''
    игра в пинг-понг
    '''
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": lets_see
}

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")