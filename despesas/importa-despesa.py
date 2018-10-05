import csv

with open('despesas.csv' ) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')

    for row in reader:
        print(row['Data'])
        print(row['descricao'])
        print(row['Categoria'])
        print(row['Valor'])
