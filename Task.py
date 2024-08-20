#C-Create
import mysql.connector
db_connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
     database="Super_Market")
print("connection sucessfull")
#create cursor to execute sql query
cursor=db_connection.cursor()
#create a database
#create_database_query="CREATE SCHEMA Super_Market"
#cursor.execute(create_database_query)
#commit changes
#db_connection.commit()
#------------------------------------------------------------------------#

#create table
#create_table_query="""CREATE TABLE `Super_Market`.`Products`(
 #   `id` INT AUTO_INCREMENT PRIMARY KEY,
  #  `name` VARCHAR(50),
 #  `category` VARCHAR(50),
 #   `price` float
#)"""
#cursor=db_connection.cursor()
#cursor.execute(create_table_query)
#db_connection.commit()
#------------------------------------------------------------------------#


#Insert 
#insert_data_query = """
#INSERT INTO Products(id,name,category,price) VALUES (%s, %s, %s, %s)
#"""

# Data to insert
#data_to_insert = [
#   (1,"milk","food",30),
#    (2,"bread","food", 20),
#   (3,"butter","food", 22),
#  (4,"comb","cosmetic",15)
#]
#cursor = db_connection.cursor()
#cursor.executemany(insert_data_query, data_to_insert)
#db_connection.commit()

#Close the cursor and connection
#cursor=db_connection.cursor()
#cursor.close()
#db_connection.close()
#all_data= """ SELECT * FROM Products"""
#cursor.execute(all_data)
#my_data=cursor.fetchall()
#for d in my_data:
 #   print(d)
#db_connection.commit()

#Update 
#my_update='UPDATE Products\
 #   SET id=5 WHERE name="Comb"'
#cursor.execute(my_update)
#db_connection.commit()   
#all_data= """ SELECT * FROM Products"""
#cursor.execute(all_data)
#my_data=cursor.fetchall()
#for d in my_data:
 #  print(d)
#db_connection.commit()    
    
#delete
my_delete="""DELETE FROM Products WHERE id=5"""
cursor.execute(my_delete)
db_connection.commit()

