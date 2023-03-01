import Entry as e

def menu():
    print("\nМеню \"Заметки\".\nВыберите действие:\n1) Показать все заметки\n2) Добавить заметку\n3) Удалить заметку\n4) Редактировать заметку\n5) Фильтр заметок по дате\n6) Просмотр заметки по ID\n7) Выход\n\nДействие: ")

def create_entry(number):
    title = check_minimal_input(input('Введите название заметки: '), number)
    body = check_minimal_input(input('Введите текст заметки: '), number)
    return e.Entry(title=title, body=body)

def check_minimal_input(text, n):
    while len(text) <= n:
        print(f'Текст должен содержать не менее {n} символов\n')
        text = input('Введите текст: ')
    else:
        return text

def shutdown():
    print("-FIN-")