import mysql.connector

def create_conection():
    conexao = mysql.connector.connect(user= '',
                                    password = '',
                                    host='',
                                    database = 'db_loja2')
    
    return conexao

def create_database():
    sql_create = 'CREATE DATABASE IF NOT EXISTS db_loja3'
    cursor.execute(sql_create)
    sql_use = 'use db_loja3'
    cursor.execute(sql_use)

def create_table():
    sql_table = '''CREATE TABLE IF NOT EXISTS tb_produto2(
        id INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(100) NOT NULL UNIQUE,
        preco DECIMAL(9, 2) NOT NULL,
        data_validade DATE NULL,
        PRIMARY KEY(id)
    )'''
    cursor.execute(sql_table)

def insert_tb_produto2():
    a_nome = input('Nome: ')
    a_preco = float(input('Preco: '))
    a_data_validade = input('Data validade: ')

    sql_insert = f'''INSERT INTO tb_produto2 (nome, preco, data_validade)
    VALUES ('{a_nome}', {a_preco}, '{a_data_validade}')'''
    cursor.execute(sql_insert)

def select_tb_produto2():
    sql_select = f'''SELECT *
        FROM tb_produto2
        WHERE preco >= 3'''
    cursor.execute(sql_select)
    l_registros = cursor.fetchall()
    for registro in l_registros:
        print(registro)

def delete_instance():
    delecao = int(input('Digite o id da instancia a ser deletada: '))
    sql_delete = f'''DELETE FROM tb_produto2 WHERE id = {delecao}'''
    cursor.execute(sql_delete)

def update_instance():
    pesquisa = input('Digite o nome da instacia a ser atualizada: ')
    novo_valor = input('Digite o novo valor: ')
    sql_update = f'''UPDATE tb_produto2 SET preco = {novo_valor} WHERE nome = '{pesquisa}' '''
    cursor.execute(sql_update)

if __name__ == '__main__':
    conexao = create_conection()
    cursor = conexao.cursor()
    create_database()
    create_table()

    while(True):
        comando = input('[x] = sair: \n[i] = insert: \n[s] = select: \n[u] = update: \n[d] = delete: \nDigite o comando: ')
        if comando == 'i':
            insert_tb_produto2()
        elif comando == 's':
            select_tb_produto2()
        elif comando == 'u':
            update_instance()
        elif comando == 'd':
            delete_instance()
        elif comando == 'x':
            break

    conexao.commit()
    cursor.close()
    conexao.close()
