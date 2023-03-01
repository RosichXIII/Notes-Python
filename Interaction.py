import File_interaction as f_i
import Entry as e
import View as v

simbol_min = 5  # Минимальное кол-во знаков заметки

def add():
    entry = v.create_entry(simbol_min)
    list_n = f_i.read_file()
    for n in list_n:
        if e.Entry.get_id(entry) == e.Entry.get_id(n):
            e.Entry.set_id(entry)
    list_n.append(entry)
    f_i.write_file(list_n, 'a')
    print('Заметка добавлена.')


def show(text):
    boolean = True
    list_n = f_i.read_file()
    if text == 'date':
        date = input('Введите дату (в формате: dd.mm.yyyy): ')
    for n in list_n:
        if text == 'all':
            boolean = False
            print(e.Entry.map_entry(n))
        if text == 'id':
            boolean = False
            print('ID: ' + e.Entry.get_id(n))
        if text == 'date':
            boolean = False
            if date in e.Entry.get_date(n):
                print(e.Entry.map_entry(n))
    if boolean == True:
        print('Заметки отсутствуют.')


def id_interaction(text):
    id = input('Укажите ID интересующей заметки: ')
    list_n = f_i.read_file()
    boolean = True
    for n in list_n:
        if id == e.Entry.get_id(n):
            boolean = False
            if text == 'edit':
                entry = v.create_entry(simbol_min)
                e.Entry.set_title(n, entry.get_title())
                e.Entry.set_body(n, entry.get_body())
                e.Entry.set_date(n)
                print('Заметка изменена.')
            if text == 'del':
                list_n.remove(n)
                print('Заметка удалена.')
            if text == 'show':
                print(e.Entry.map_entry(n))
    if boolean == True:
        print('Заметки с указанным ID не найдено.')
    f_i.write_file(list_n, 'a')
