import os
import datetime


def write_to_file(path1):
    # запись заметок в файл: ID (порядковый номер) и дата присваиваются автоматически,
    # заголовок и текст запрашиваются у пользователя (поочередно)
    n = 0 # будущий ID заметки
    lst2 = parse_file(path1)
    n = int(lst2[-1][0]) + 1
    tmp_line = str(n) + ";" + input("Введите заголовок заметки: ") + ";"
    tmp_line += input("Введите текст заметки: ") + ";"
    tmp_line += str(datetime.datetime.now())
    with open('notes.csv', "a") as file1:
        file1.write(tmp_line + "\n")


def parse_file(path1):
    # считываем файл в массив (список списков) для удобства поиска и редактирования, без заголовков столбцов!
    with open('notes.csv', "r") as file1:
        lst_1 = file1.readlines()
        lst_2 = []
        for i in range(1, len(lst_1)):
            lst_2.append(lst_1[i].split(";"))
    return lst_2


def lookup_by_field(lst_parsed_file, field_num, search_input):
    # находим все заметки, содержащие указанные символы, возвращаем список заметок
    flag1 = False
    result = []
    for i in range(0, len(lst_parsed_file)):
        if search_input in lst_parsed_file[i][field_num]:
            result.append(lst_parsed_file[i])
            flag1 = True
    if not flag1:
        result.append(["Извините, такой записи нет"])
    return result


def search_file(path1, txt1):
    # уточняем поле для поиска и искомую информацию
    lst_parsed_notes = parse_file(path1)
    txt_zapros = "Введите номер команды, которую хотите выполнить.\n" \
                 "1. Искать по ID\n" \
                 "2. Искать по заголовкам\n" \
                 "3. Искать по текстам записок\n" \
                 "4. Искать по дате в формате ГГГГ-ММ-ДД\n"\
                 "5. Вернуться в главное меню\n"
    a = int(input(txt_zapros))
    if a in [1, 2, 3, 4]:
        search_input = input(txt1)
        result = lookup_by_field(lst_parsed_notes, a-1, search_input)
        return result
    else:
        get_user_intention()


def show_all(path1):
    # возвращаем результат чтения файла
    with open('notes.csv', "r") as file1:
        return file1.read()


def update_note_in_file(path1, lst2):
    # перезаписываем файл содержимым массива (с отредактированными или удаленными строками, например)
    str_to_write = "0;Заголовок;Текст заметки;Дата последнего изменения\n"
    for item in lst2:
        str_to_write += ';'.join(item)
    with open('notes.csv', "w") as file1:
        file1.write(str_to_write)


def edit_note(path1):
    # редактируем информацию: парсим файл, уточняем у пользователя и вносим изменения в одну строку, вызываем перезапись
    lst_found = search_file(path1, "Что ищем, чтобы отредактировать? ") # список найденных строк
    txt_zapros = "Введите номер строки, которую хотите изменить.\n"

    if lst_found == ["Извините, такой записи нет"]:
        print("Извините, такой записи нет")
        return
    else:
        for i in range(1, len(lst_found)+1):
            txt_zapros += str(i) + ". " + str(lst_found[i-1]) + "\n"
        txt_zapros += str(len(lst_found)+1) + ". " + "Отредактировать другую строку\n"
        txt_zapros += str(len(lst_found)+2) + ". " + "Выйти в главное меню\n"
    a = int(input(txt_zapros)) # номер нужной строки (на 1 больше, чем индекс в списке найденных)
    if a in range(1, len(lst_found)+1):
        lst2 = parse_file(path1) # список из строк файла (записок), разбитых на поля
        idx_to_edit = lst2.index(lst_found[a-1])
        lst2[idx_to_edit][1] = input("Введите новый заголовок заметки: ")
        lst2[idx_to_edit][2] = input("Введите новый текст заметки: ")
        lst2[idx_to_edit][3] = str(datetime.datetime.now()) + "\n"
        update_note_in_file(path1, lst2)
        print("Записка № " + str(idx_to_edit+1) + " успешно изменена.")
        return
    elif a == (len(lst_found)+1):
        edit_note(path1)
    else:
        return


def delete_note(path1):
    # редактируем информацию: парсим файл, уточняем у пользователя и удаляем одну строку, вызываем перезапись
    lst_found = search_file(path1, "Что ищем, чтобы удалить? ")  # список найденных строк
    txt_zapros = "Введите номер строки, которую хотите удалить.\n"
    if lst_found == ["Извините, такой записи нет"]:
        print("Извините, такой записи нет")
        return
    else:
        for i in range(1, len(lst_found)+1):
            txt_zapros += str(i) + ". " + str(lst_found[i-1]) + "\n"
        txt_zapros += str(len(lst_found)+1) + ". " + "Удалить другую строку\n"
        txt_zapros += str(len(lst_found)+2) + ". " + "Выйти в главное меню\n"
    a = int(input(txt_zapros)) # номер нужной строки (на 1 больше, чем индекс в списке найденных)
    if a in range(1, len(lst_found)+1):
        lst2 = parse_file(path1) # список из строк файла (записок), разбитых на поля
        idx_to_delete = lst2.index(lst_found[a-1])
        lst2.pop(idx_to_delete)
        update_note_in_file(path1, lst2)
        print("Записка № " + str(idx_to_delete+1) + " успешно удалена.")
        return
    elif a == (len(lst_found)+1):
        delete_note(path1)
    else:
        return


def get_user_intention():
    # главное меню
    txt_zapros = "Введите номер команды, которую хотите выполнить.\n" \
                 "1. Записать новые данные в файл\n" \
                 "2. Найти конкретную запись в файле\n" \
                 "3. Вывести весь файл\n" \
                 "4. Редактировать заметку\n" \
                 "5. Удалить заметку\n" \
                 "6. Выйти из программы\n"
    a = None
    while a != '6':
        a = input(txt_zapros)
        if a == '1':
            write_to_file(os.getcwd())
        elif a == '2':
            lst_1 = search_file(os.getcwd(), "Что ищем? ")
            result = ''
            for item in lst_1:
                result += '\n' + '\n'.join(item)
            print(result)
        elif a == '3':
            result = show_all(os.getcwd())
            print(result)
        elif a == '4':
            edit_note(os.getcwd())
        elif a == '5':
            delete_note(os.getcwd())
    quit()


def start_program():
    # начало работы: проверяем наличие файла; если файла нет, создаем и прописываем заголовки; запускаем меню
    if not os.path.exists('notes.csv'):
        with open('notes.csv', "a") as file1:
            file1.write("0;Заголовок;Текст заметки;Дата последнего изменения" + "\n")
    get_user_intention()


start_program()




