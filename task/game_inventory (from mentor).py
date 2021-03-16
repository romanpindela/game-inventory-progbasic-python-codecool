
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.
import copy
import csv
from pathlib import Path


def display_inventory(inventory):
    print(inventory.items())


def add_to_inventory(inventory, added_items):
    for key in added_items:
        if key in inventory:
            inventory[key] = inventory[key] + added_items[key]
        else:
            inventory.update({key : added_items[key]})

def remove_from_inventory(inventory, removed_items):
    for item in removed_items:
        if item in inventory:
            if inventory[item] > removed_items[item]:
                inventory[item] -= removed_items[item]
            elif inventory[item] <= removed_items[item]:
                inventory.pop(item)


def print_table(inventory, order = None):
    from operator import itemgetter
    print("-------------------------")
    print("{:>15} | {:>5}".format('item', 'count'))
    print("-------------------------")
    display_inventory = copy.deepcopy(inventory)
    if order == 'count,asc':
        # sorting using lamba - get second element
        display_inventory = dict(sorted(inventory.items(), key = lambda item: item[1]))
    elif order == "count,desc":
        # sorting using itemgetter - similar case as above
        display_inventory = dict(sorted(inventory.items(), key = itemgetter(1), reverse= True))
    for key, value in display_inventory.items():
        print("{:>15} | {:>5}".format(key, value))
    print("-------------------------")

def import_inventory(inventory, filename):
    try:
        path = Path(__file__).parent
        with open(f'{path}\\{filename}') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                for element in row:
                    add_to_inventory(inventory, {element : 2})
    except FileNotFoundError:
        print("File '<filename' not found!")

    print(filename)
    # for row in csv_reader:
    #     print(', '.join(row))


def export_inventory(inventory, filename='export_inventory.csv'):
    try:
        file_name=open(filename,'w')
        csv_writer = csv.writer(file_name)
        inventory_to_export=[]
        for key,value in inventory.items():
            for i in range(value):
                inventory_to_export.append(key)
        csv_writer.writerow(inventory_to_export)
    except PermissionError:
        print(f"You don't have permission creating file '{filename}'!")

def main():
    inventory = {'dagger': 3, 'gold coin': 1, 'battleaxe': 1}

    items_to_add = {'gold coin' : 2, 'dagger': 1, 'bow': 1, 'apple': 3}
    add_to_inventory(inventory, items_to_add)
    # print_table(inventory,'count,asc')

    items_to_remove = {'gold coin' : 1, 'dagger': 7, 'hammer': 1, 'apple': 1}
    remove_from_inventory(inventory, items_to_remove)

    filename = 'import_inventory.csv'
    import_inventory(inventory, filename)
    export_inventory(inventory)
    print_table(inventory,'count,desc')

if __name__ == '__main__':
    main()
