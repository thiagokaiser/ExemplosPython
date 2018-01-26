import csv

lista = []
i = 0
while i <= 190:
    i = i + 1
    lista.append(i)
    
print(lista)

with open('c:/temp/testecsv.csv', 'w', newline='') as csvfile:
    arquivo = csv.writer(csvfile, delimiter=';')
    arquivo.writerow(lista)
    
