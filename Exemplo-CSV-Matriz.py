import csv
matriz = []
with open('2014.csv' ) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')

    for row in reader:        
        matriz.append([row['Número'], row['Série']])    
    
for i in matriz:
    if i[0] == '45569':
        print(i)



