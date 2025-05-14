from employees_connection import db_connection

import mysql.connector
connection = mysql.connector.connect(user='',
                                      password='',
                                      host='',
                                      database='db_empresa')
print('Connection:', connection)

cursor = connection.cursor()
sql = '''SELECT * FROM tb_funcionario'''
cursor.execute(sql)
records = cursor.fetchall()
print(records)

cursor.close()
connection.close()
print('Connection closed')
