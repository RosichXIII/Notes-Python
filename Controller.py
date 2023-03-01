import Interaction as inter
import View as v

def run():
    current_input = ''
    while current_input != '7':
        v.menu()
        current_input = input().strip()
        if current_input == '1':
            inter.show('all')
        if current_input == '2':
            inter.add()
        if current_input == '3':
            inter.show('all')
            inter.id_interaction('del')
        if current_input == '4':
            inter.show('all')
            inter.id_interaction('edit')
        if current_input == '5':
            inter.show('date')
        if current_input == '6':
            inter.show('id')
            inter.id_interaction('show')
        if current_input == '7':
            v.shutdown()
            break
        else:
            print('Введите число от 1 до 7.')