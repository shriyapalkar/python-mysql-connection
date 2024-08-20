#CRUD
#C-Create
import mysql.connector
db_connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root')
#print("connection sucessfull")

#create cursor to execute sql query
#cursor=db_connection.cursor()
#create a database
#create_database_query="CREATE SCHEMA test_db"
#cursor.execute(create_database_query)
#commit changes
#db_connection.commit()

#create table
#create_table_query="""CREATE TABLE `test_db`.`test_table`(
 #   `id` INT AUTO_INCREMENT PRIMARY KEY,
 #   `name` VARCHAR(50),
 #  `age` INT
#)"""
#cursor=db_connection.cursor()
#cursor.execute(create_table_query)
#db_connection.commit()

#Insert data into table
insert_data_query="""
INSERT INTO test_table(id,name,age) VALUES (%s,%s,%s)
"""
data_to_insert = [(1,"shriya", 21,2,"shravani", 22,3,"mrunal", 22)]
cursor=db_connection.cursor()   
cursor.executemany(insert_data_query, data_to_insert)
db_connection.commit()

#R-Read



#U-Update



#D-Delete