from employees_connection import db_connection

import mysql.connector
connection = mysql.connector.connect(user='',
                                     password='',
                                     host='',
                                     database='db_empresa')

print('Connection:\n', connection)


cursor = connection.cursor()
sql = ''' create table tb_funcionario(
    idt INT,
    nome varchar(45) not null,
    salario decimal(9,2) null,
    primary key (idt)
    )'''
cursor.execute(sql)
cursor.close()
connection.close()
print("\nConnection closed.")
