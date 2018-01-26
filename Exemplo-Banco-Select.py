import sqlite3

conn = sqlite3.connect('Bancos/teste01.db')
cursor = conn.cursor()
i_opcao = 0
while i_opcao != 4:
    v_usuar = str(input('Usuario: '))
    # lendo os dados
    cursor.execute("""
            SELECT * FROM usuario WHERE cod_usuar = ? """, (v_usuar,))

    i = 0
    for linha in cursor.fetchall():
        print(linha[1])        
        i = 1
    if i == 0:
        print('Não encontrado')
    else:
        i_opcao = int(input('1 - Deletar, 2- Alterar'))
                        
    if i_opcao == 1:
        cursor.execute("""
            DELETE FROM usuario WHERE cod_usuar = ? """, (v_usuar,))
    elif i_opcao == 2:
        print('Insira os novos dados')
        v_nome = str(input('Nome: '))
        cursor.execute("""
            UPDATE usuario SET nome_usuar =? WHERE cod_usuar = ? """, (v_nome,v_usuar))

    conn.commit()   

conn.close()
