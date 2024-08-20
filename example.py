import mysql.connector

# Connect to the database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="test_db"
)

cursor = db_connection.cursor()

# SQL query with properly formatted placeholders
#insert_data_query = """
#INSERT INTO test_table(id,name, age) VALUES (%s, %s, %s)
#"""

# Data to insert
#data_to_insert = [
 #   (1,"shriya", 21),
  #  (2,"shravani", 22),
   # (3,"mrunal", 22)
#]

# Execute the query
#cursor.executemany(insert_data_query, data_to_insert)

# Commit the transaction
#db_connection.commit()

# Close the cursor and connection
#cursor.close()
#db_connection.close()
#all_data= """ SELECT * FROM test_table"""
#cursor.execute(all_data)
#my_data=cursor.fetchall()
#for d in my_data:
 #   print(d)
#db_connection.commit()

#Update 
#my_update='UPDATE test_table\
#    SET age=100 WHERE name="shriya"'
#cursor.execute(my_update)
#db_connection.commit()   
#all_data= """ SELECT * FROM test_table"""
#cursor.execute(all_data)
#my_data=cursor.fetchall()
#for d in my_data:
 #   print(d)
#db_connection.commit()    
    
#delete
my_delete="""DELETE FROM test_table WHERE id=3"""
cursor.execute(my_delete)
db_connection.commit()