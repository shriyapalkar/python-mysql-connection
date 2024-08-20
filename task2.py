#CRUD
#C-Create
import mysql.connector
db_connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database="UserInfo")
print("connection sucessfull")

#create cursor to execute sql query
#cursor=db_connection.cursor()
#create a database
#create_database_query="CREATE SCHEMA UserInfo"
#cursor.execute(create_database_query)
#commit changes
#db_connection.commit()

#create table
#create_table_query="""CREATE TABLE `UserInfo`.`Info`(
  #  `User_id` INT AUTO_INCREMENT PRIMARY KEY,
  #  `Username` VARCHAR(50),
   # `Firstname` VARCHAR(50),
    #`Lastname` VARCHAR(50),
#    `Email` VARCHAR(50),
 #   `Password` VARCHAR(50),
  #  `Contact` INT,
   # `Register_date` DATE,
#    `City_id` VARCHAR(50),
 #  `User_Status` VARCHAR(50)
#)"""
#cursor=db_connection.cursor()
#cursor.execute(create_table_query)
#db_connection.commit()

#Insert data into table
#insert_data_query="""
#INSERT INTO Info(User_id,Username,Firstname,Lastname,Email,Password,Contact,Register_date,City_id,User_Status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#"""
#data_to_insert = [(1,"shriya06","shriya","palkar","shri@gmail.com","shri2611",3334,"2024-01-01","KOP231","Active"),
#(2,"shrav06=2","shravani","shedge","shrav@gmail.com","shrrav2",3112,"2024-01-01","SAN321","InActive"),
#(3,"mrunala6","mrunal","salunkhe","mru@gmail.com","mrun23",3122,"2024-01-01","KOP231","Active"),
#(4,"mansi23","mansi","sawant","man@gmail.com","mansi21",3222,"2024-01-01","KUD789","InActive"),
#(5,"harsh21","harsh","palkar","har@gmail.com","harsh21",3221,"2024-01-01","KUD789","InActive"),
#(6,"vanshita03","vanshita","malani","van@gmail.com","vanshita3",3223,"2024-01-01","KOP231","Active"),
#(7,"sneha08","sneha","gavali","sneh@gmail.com","sneh08",2333,"2024-01-01","RTN456","InActive"),
#(8,"sangita7","sangita","palkar","sang@gmail.com","sangita7",2331,"2024-01-01","KOP231","Active"),
#(9,"guru021","guru","palkar","guru@gmail.com","guru2",2332,"2024-01-01","MUM678","InActive"),
#(10,"niraj26","niraj","palkar","niraj@gmail.com","niraj26",1335,"2024-01-01","KOP231","Active")]
cursor=db_connection.cursor()   
#cursor.executemany(insert_data_query, data_to_insert)
#db_connection.commit()

#R-Read
#all_data= """ SELECT * FROM Info"""
#cursor.execute(all_data)
#my_data=cursor.fetchall()
#for d in my_data:
 #   print(d)
#db_connection.commit()

#U-Update
#my_update='UPDATE Info\
#   SET Username="shrav" WHERE User_id=2'
#cursor.execute(my_update)
#db_connection.commit()   
#all_data= """ SELECT * FROM Info"""
#cursor.execute(all_data)
#my_data=cursor.fetchall()
#for d in my_data:
  # print(d)
#db_connection.commit()    


#D-Delete
my_delete="""DELETE FROM Info WHERE User_id=10"""
cursor.execute(my_delete)
db_connection.commit()
