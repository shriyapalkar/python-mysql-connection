import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='testdb',auth_plugin='mysql_native_password')
print('Connection Success')
cnx.close()