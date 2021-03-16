
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.
import os
import csv
from pathlib import Path


def isWritable(directory):
    try:
        tmp_prefix = "write_tester";
        count = 0
        filename = os.path.join(directory, tmp_prefix)
        while(os.path.exists(filename)):
            filename = "{}.{}".format(os.path.join(directory, tmp_prefix),count)
            count = count + 1
        f = open(filename,"w")
        f.close()
        os.remove(filename)
        return True
    except Exception as e:
        #print "{}".format(e)
        return False


def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""

    for key, value in inventory.items():
        print(f'{key}:{value}')


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    if added_items in inventory:
        inventory[added_items] += 1
    else:
        inventory[element] = 1
    


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    if removed_items in inventory:
        inventory[removed_items] -= 1
        if inventory[removed_items] == 0:
            inventory.pop(removed_items)
    else:
        pass


def print_table(inventory, order):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """
    if order == 'count,desc':
        sorted_inventory = sorted(inventory.items(), key=lambda x: x[1])
    elif order == 'count,asc':
        sorted_inventory = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    else: 
        sorted_inventory = [(key,value) for key,value in inventory.items()]
    
    print("-"*23)
    print("{:<10} | {:>10}".format("item name","count"))
    print("-"*23)
    for key,value in sorted_inventory:
        print("{:<10} | {:>10}".format(key,value))
    print("-"*23)


def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""
    try:
        path = Path(__file__).parent
        csv_file = open(f'{path}\\{filename}',"rt",  encoding="utf8",)
        csv_reader = csv.reader(csv_file)
        lista = []
        for row in csv_reader:
            for element in row:
                if element in inventory:
                    inventory[element] += 1
                else:
                    inventory[element] = 1    
    except:
        print(f"File {filename} not found!")



    
def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""
    try:
        if not isWritable(path):
            raise ValueError(f'You don\'t have permission creating file {filename}!')

        path = Path(__file__).parent
        csv_file = open(f'{path}\\{filename}',"w",  encoding="utf8",)

        csv_writer = csv.writer(csv_file)


        # inventory_to_export = ['One','Twoo',12343]
        # csv_writer.writerow(inventory_to_export)

        for element in inventory:
            element_times = inventory[element]
            while element_times > 0:
                csv_writer.writerow([element])
                print(element)
                element_times -= 1 
    except:
        print(f"File {filename} not found!")
    pass

def main_menu():

    user_inventory = {}

    # default filenames
    filename_to_import = "import_inventory.csv"
    filename_to_export = "export_inventory.csv"

    import_inventory(user_inventory,filename_to_import)
    #import_inventory(user_inventory,filename_to_export)
    display_inventory(user_inventory)
    print_table(user_inventory, 'count,asc')
    #print_table(user_inventory,'')
    add_to_inventory(user_inventory,"diamond")
    remove_from_inventory(user_inventory,"rope")
    remove_from_inventory(user_inventory,"hammer")
    print_table(user_inventory, 'count,asc')
    #export_inventory(user_inventory,filename_to_export)

if __name__ == '__main__':
    main_menu()