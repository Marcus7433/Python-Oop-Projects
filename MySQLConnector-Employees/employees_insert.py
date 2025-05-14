from employees_connection import db_connection

import mysql.connector
connection = mysql.connector.connect(user='',
                                      password='',
                                      host='',
                                      database='db_empresa')
print('Connection:', connection)

cursor = connection.cursor()
sql = ''' INSERT INTO tb_funcionario
    (idt, nome, salario)
    VALUES
    (3, 'Jonas', 4300.00), (4, 'Paulo', 2000) '''
cursor.execute(sql)
connection.commit()
print(cursor.rowcount, "Record inserted.")

cursor.close()
connection.close()
print('Connection closed')
