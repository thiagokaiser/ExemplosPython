""" -------------------------- """
""" --------- OBJETO --------- """
""" -------------------------- """
class Pessoa:    

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade = self.idade + 1
        
    
var = []
var.append(Pessoa('thiago', 21))
var.append(Pessoa('fabio', 10))

for i in var:
    i.cor = 'teste'

for i in var:
    if i.nome == 'thiago':
        i.aniversario()
        i.cor = 'azul'

for i in var:    
    print(i.nome, i.idade, i.cor)

""" ------------------------------ """
""" --------- DICIONARIO --------- """
""" ------------------------------ """

varray = []
pessoa = dict()

pessoa = {'nome': 'Thiago', 'idade': 21}
varray.append(pessoa)

pessoa = {'nome': 'Fabio', 'idade': 2222}
varray.append(pessoa)

for i in varray:
    i['cor'] = 'azul'


print(varray)

