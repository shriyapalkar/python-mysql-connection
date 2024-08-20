import mysql.connector;
db=mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="Uni_Results")
#print("success")

#create cursor
#cursor=db.cursor()
#create_db="CREATE SCHEMA Uni_Results"
#cursor.execute(create_db)
#db.commit()

#create table
#create_table_query="""CREATE TABLE `Uni_Results`.`Result_Data`(
 #       `Student_Id` int,
#      `PRN` VARCHAR(50),
#      `FULL_NAME` VARCHAR(50),
#    `GENDER` VARCHAR(50),
#    `GPA` VARCHAR(10),
#    `RESULT_STATUS` VARCHAR(50)
#)"""
#cursor=db.cursor()
#cursor.execute(create_table_query)
#db.commit()"""

#insert
#insert_db=""" INSERT INTO Result_Data(Student_Id,PRN,FULL_NAME,GENDER,GPA,RESULT_STATUS)
#VALUES (%s,%s,%s,%s,%s,%s)
#    """
#data_insert=[("1","2021651","shriya guru palkar","Female","2.3","FAIL"),
#             ("2","2021652","shravni sakharam shedge","Female","2.6","FAIL"),
#             ("3","2021653","mrunal vivek salunkhe","Female","8.6","PASS"),
#             ("4","2021654","harsh guru palkar","Male","8.6","PASS"),
#             ("5","2021655","sangita guru palkar","Female","8.6","PASS"),
#             ("6","2021656","guru nana palkar","Male","8.6","PASS"),
#             ("7","2021657","mansi sanjay sawant","Female","2.6","FAIL"),
#             ("8","2021658","amit balu kamble","Male","8.6","PASS"),
#             ("9","2021659","niraj nitin dalvi","Male","8.6","PASS"),
#             ("10","2021650","anant sanjay patkar","Male","8.6","PASS")
#             ]
#cursor=db.cursor()   
#cursor.executemany(insert_db,data_insert)
#db.commit()

#read
#all_data= """ SELECT * FROM Result_Data"""
#cursor=db.cursor()  
#cursor.execute(all_data)
#my_data=cursor.fetchall()
#for d in my_data:
#   print(d)
#db.commit()

#Update 
#my_update='UPDATE Result_Data\
#   SET Student_Id=7 WHERE GPA="4.4"'
#cursor=db.cursor()  
#cursor.execute(my_update)
#db.commit()   
#all_data= """ SELECT * FROM Result_Data"""
#cursor=db.cursor()  
#cursor.execute(all_data)
#my_data=cursor.fetchall()
#for d in my_data:
#   print(d)
#db.commit()    

#delete
my_delete="""DELETE FROM Result_Data WHERE Student_Id=10"""
cursor=db.cursor() 
cursor.execute(my_delete)
db.commit()