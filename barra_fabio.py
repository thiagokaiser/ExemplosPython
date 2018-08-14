from math import ceil
barras_ini = 6
barras_fim = 100
barras_dia = 3
num_dias = 0

num_dias = (barras_fim - barras_ini) * barras_dia

print('dias:' ,num_dias)
print('semanas:' ,ceil(num_dias / 7))

print('---------------')

num_dias = 0

while barras_ini < barras_fim:
    i = 0
    while barras_dia > i:
        num_dias = num_dias + 1
        i = i + 1
            
    barras_ini = barras_ini + 1
    
print(num_dias)

