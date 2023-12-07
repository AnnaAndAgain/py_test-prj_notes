import os
import datetime

#добавить на старте программы создание пустого файла, если его еще нет --
# #так можно будет писать с ИД сразу



def write_to_file(path1):
    n = 0
    with open('notes.csv', "r") as file1:
        lst_1 = file1.readlines()
        n = len(lst_1)
    tmp_line = str(n) + ";" + input("Введите заголовок заметки: ") + ";"
    tmp_line += input("Введите текст заметки: ") + ";"
    tmp_line += str(datetime.datetime.now())
    with open('notes.csv', "a") as file1:
        file1.write(tmp_line + "\n")


def search_file(path1, search_input):
    with open('notes.csv', "r") as file1:
        lst_1 = file1.readlines()
        flag1 = False
        result = "\n"
        for line in lst_1:
            if search_input in line:
                result = result + line
                flag1 = True
        if not flag1:
            result = "Извините, такой записи нет\n"
    return result


def show_all(path1):
    with open('notes.csv', "r") as file1:
        return file1.read()


def get_user_intention():
    txt_zapros = "Введите номер команды, которую хотите выполнить.\n" \
                 "1. Записать новые данные в файл\n" \
                 "2. Найти конкретную запись в файле\n" \
                 "3. Вывести весь файл\n" \
                 "4. Выйти из программы.\n"
    a = None
    while a != '4':
        a = input(txt_zapros)
        if a == '1':
            write_to_file(os.getcwd())
        elif a == '2':
            to_search = input("Что ищем? ")
            result = search_file(os.getcwd(), to_search)
            print(result)
        elif a == '3':
            result = show_all(os.getcwd())
            print(result)


def start_program():
    if not os.path.exists('notes.csv'):
        with open('notes.csv', "a") as file1:
            file1.write("0;Заголовок;Текст заметки;Дата последнего изменения" + "\n")
    get_user_intention()


start_program()




