import csv
from pathlib import Path

#import
filename ="exported.csv"
path = Path(__file__).parent
with open (f'{path}\\{filename}') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        for element in row:
            print(element)

#export
filename ="exported23.csv"
file_name = open(filename,'x')
csv_writer = csv.writer(file_name)
inventory_to_export = ['One','Twoo',12343]
csv_writer.writerow(inventory_to_export)


