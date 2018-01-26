import csv
import os

var_lista  = []
lista_xml  = []

def removeLetras(variavel):
    v_letras = "abcdefghijklmnopqrstuvwxyz.,()"
    for i in v_letras:
        variavel = variavel.replace(i, "")        
    return variavel

def importa_xml(c_caminho):
    v_dir     = os.listdir(c_caminho)

    for file in v_dir:
        v_file = file
        v_file = v_file[17:22]
        v_file = removeLetras(v_file)
        
        lista_xml.append([v_file,c_caminho[-3:]])


v_dir_csv = os.listdir('C:/Temp/python/Notas')

for arq_dir in v_dir_csv:
    print(arq_dir)
    c_caminho = 'C:/Temp/python/Notas/' + arq_dir
    
    with open(c_caminho) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:

            var_estab = row['Emitente']
            var_estab = var_estab[-5:]
            var_estab = removeLetras(var_estab)
            var_lista.append([row['Número'],var_estab, arq_dir])


#importa_xml('C:/Temp/python/xml/111')
#importa_xml('C:/Temp/python/xml/115')
importa_xml('C:/Temp/python/xml/121')
#importa_xml('C:/Temp/python/xml/122')

"""for linha in lista_xml:
    print(linha)

for linha in var_lista:
    print(linha)"""
var_result = []
for linha_xml in lista_xml:

    l_achou = False
    
    for csv in var_lista:
        if csv[0] == linha_xml[0] and csv[1] == linha_xml[1]:
            l_achou = True
            #var_lista.remove(csv)
            
    var_result.append([linha_xml[0],l_achou])               
    
for linha_final in var_result:
    if linha_final[1] == False:
        print(linha_final)
