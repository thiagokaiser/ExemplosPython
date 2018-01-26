from datetime import date, timedelta

teste1 = [{'mes': '2017-12', 'valor': '555.00'},
         {'mes': '2017-01', 'valor': '381.00'},
         {'mes': '2017-02', 'valor': '2.00'},
         {'mes': '2017-03', 'valor': '8.00'},
         {'mes': '2017-04', 'valor': '212.00'},
         {'mes': '2017-07', 'valor': '3.00'}]

#hoje = datetime.date.today().strftime('%Y-%m')

def funcao_data(i):
    array = []
    dt = date.today()
    while i > 0:
        prev = dt.replace(day=1) - timedelta(days=1)
        dt = prev        
        array.append(prev)
        i = i - 1
    return array
    
teste = funcao_data(12)
newdict = dict()
arraydict = []

for arraydata in teste:
    mes = arraydata.strftime('%Y-%m')
    valor = 0
    for i in teste1:        
        if mes == i['mes']:
            valor = i['valor']        
    newdict = {'mes': mes , 'valor': valor}
    arraydict.append(newdict)    

for i in arraydict:
   print(i)

    
    
    
