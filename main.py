class Item:
    def __init__(self):
        self.to_do_list = dict()

    def add_item(self, name):
        time_frame = int(input('Insert time frame: '))
        priority = int(input('Insert priority from 1 to 10: '))
        self.to_do_list.update({name: [f'Time: {time_frame}', f'Priority: {priority}']})
        print('\n' * 2)
        print('-YOUR ITEMS-')
        print(list(self.to_do_list.keys()))
        print('\n' * 2)

class ItemList(Item):
    def get_all_items(self):
        print('-YOUR ITEMS-')
        print(list(self.to_do_list.keys()))
        print('\n' * 2)

    def get_item_by_name(self, name):
        print('-ITEM INFO-')
        print(f'Name: {name}')
        print(self.to_do_list.get(name)[0])
        print(self.to_do_list.get(name)[1])
        print('\n'*2)

    def get_items_by_time(self, time):
        print(f'-ITEMS BY TIME {time}-')
        result = []
        for i in list(self.to_do_list.keys()):
            if self.to_do_list.get(i)[0] == f'Time: {time}':
                result.append(i)
        print(result)
        print('\n' * 2)


    def get_priority_items(self):
        print(f'-PRIORITY ITEMS-')
        result = []
        for i in list(self.to_do_list.keys()):
            if int(self.to_do_list.get(i)[1][10:]) > 5:
                result.append(i)
        print(result)
        print('\n' * 2)

    def delete_item(self, name):
        self.to_do_list.pop(name)
        print(f'-YOU DELETED {name} TASK-')
        print('\n' * 2)

    def change_time(self, name, time):
        self.to_do_list[name][0] = f'Time: {time}'

    def change_priority(self, name, priority):
        self.to_do_list[name][1] = f'Priority: {priority}'

a = ItemList()
a.add_item("Example")
a.add_item("Another")
a.get_all_items()
a.get_item_by_name("Another")
a.get_items_by_time("1")
a.get_priority_items()
a.change_priority("Another", 10)
a.change_time("Another", 2)
a.get_item_by_name("Another")
a.delete_item("Another")
a.get_all_items()