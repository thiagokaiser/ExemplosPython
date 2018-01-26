import csv

with open('teste2014.csv' ) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')

    for row in reader:
        print(row['Emitente'])
