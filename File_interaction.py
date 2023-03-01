import Entry as e

def write_file(list_n, mode):
    file = open("Notes.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("Notes.csv", mode=mode, encoding='utf-8')
    for entry in list_n:
        file.write(e.Entry.to_string(entry))
        file.write('\n')
    file.close

def read_file():
    try:
        list_n = []
        file = open("Notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            entry = e.Entry(id = split_n[0], title = split_n[1], body = split_n[2], date = split_n[3])
            list_n.append(entry)
    except Exception:
        print('Заметки отсутствуют.')
    finally:
        return list_n