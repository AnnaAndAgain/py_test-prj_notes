import os
import datetime

#парсить файл для поиска по ИД, заголовку, тексту и дате
#дату выбирать из списка?


def write_to_file(path1):
    # запись заметок в файл: ID (порядковый номер) и дата присваиваются автоматически,
    # заголовок и текст запрашиваются у пользователя (поочередно)
    n = 0 # будущий ID заметки
    with open('notes.csv', "r") as file1:
        lst_1 = file1.readlines()
        n = len(lst_1)
    tmp_line = str(n) + ";" + input("Введите заголовок заметки: ") + ";"
    tmp_line += input("Введите текст заметки: ") + ";"
    tmp_line += str(datetime.datetime.now())
    with open('notes.csv', "a") as file1:
        file1.write(tmp_line + "\n")


def parse_file(path1):
    # считываем файл в массив (список списков) для удобства поиска и редактирования
    with open('notes.csv', "r") as file1:
        lst_1 = file1.readlines()
        lst_2 = []
        for i in range(1, len(lst_1)):
            lst_2.append(lst_1[i].split(";"))
    return lst_2


def lookup_by_field(lst_parsed_file, field_num, search_input):
    flag1 = False
    result = []
    for i in range(0, len(lst_parsed_file)):
        if search_input in lst_parsed_file[i][field_num]:
            result.append(lst_parsed_file[i])
            flag1 = True
    if not flag1:
        result.append(["Извините, такой записи нет"])
    return result


def search_file(path1):
    lst_parsed_notes = parse_file(path1)
    txt_zapros = "Введите номер команды, которую хотите выполнить.\n" \
                 "1. Искать по ID\n" \
                 "2. Искать по заголовкам\n" \
                 "3. Искать по текстам записок\n" \
                 "4. Искать по дате в формате ГГГГ-ММ-ДД\n"\
                 "5. Вернуться в главное меню\n"
    a = int(input(txt_zapros))
    if a in [1, 2, 3, 4]:
        search_input = input("Что ищем? ")
        result = lookup_by_field(lst_parsed_notes, a-1, search_input)
        return result
    else:
        get_user_intention()


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
            lst_1 = search_file(os.getcwd())
            result = ''
            for item in lst_1:
                result += '\n' + '\n'.join(item)
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




