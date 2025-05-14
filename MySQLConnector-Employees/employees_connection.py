import mysql.connector
db_connection = mysql.connector.connect(user='',
                                        password='',
                                        host='')

print('Connection:\n', db_connection)
db_connection.close()
print('\nConnection closed')
