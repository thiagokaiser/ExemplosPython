class Testando:
    def nome(self,name):
        self.name = name
    def sobrenome(self,sobrenome):
        self.sobrenome = sobrenome
    def nomecompleto(self):
        nome_completo = self.name + ' ' + self.sobrenome
        print(nome_completo)


oi = Testando()
oi.nome('Thiago')
oi.sobrenome('Kaiser')
oi.nomecompleto()

emo = Testando()
emo.nome('Fabio')
emo.sobrenome('Prudencio')
emo.nomecompleto()
