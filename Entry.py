from datetime import datetime as dt
import uuid


class Entry:
    def __init__(self, id = str(uuid.uuid1())[0:3],  title = "текст", body = "текст", date = str(dt.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def get_id(entry):
        return entry.id

    def get_title(entry):
        return entry.title

    def get_body(entry):
        return entry.body

    def get_date(entry):
        return entry.date

    def set_id(entry):
        entry.id = str(uuid.uuid1())[0:3]

    def set_title(entry, title):
        entry.title = title

    def set_body(entry, body):
        entry.body = body

    def set_date(entry):
        entry.date = str(dt.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(entry):
        return entry.id + ';' + entry.title + ';' + entry.body + ';' + entry.date

    def map_entry(entry):
        return '\nID: ' + entry.id + '\n' + 'Название: ' + entry.title + '\n' + 'Описание: ' + entry.body + '\n' + 'Дата: ' + entry.date
