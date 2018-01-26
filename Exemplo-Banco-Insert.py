import sqlite3

conn = sqlite3.connect('Bancos/teste01.db')
cursor = conn.cursor()

# solicitando os dados ao usuário
p_cod_usuar = input('Cod: ')
p_nome_usuar = input('Nome: ')

# inserindo dados na tabela
cursor.execute("""
INSERT INTO usuario (cod_usuar, nome_usuar) VALUES (?,?)
""", (p_cod_usuar, p_nome_usuar))

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
