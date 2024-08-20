import mysql.connector;
db=mysql.connector.connect(
    host='localhost',
    username='root',
    password='root',
    database="Bank_Opeartions"
)
print("sucess")

'''#create cursor
cursor=db.cursor()
create_db="CREATE SCHEMA Bank_Opeartions"
cursor.execute(create_db)
db.commit() '''

'''#create table
create_table_query="""CREATE TABLE `Bank_Opeartions`.`Account_Opening`(
       `cust_Id` int,
      `dob` date,
      `FULL_NAME` VARCHAR(50),
    `GENDER` VARCHAR(50),
    `city` VARCHAR(10),
   `pincode` INT,
   `phone` VARCHAR(10)
)"""
cursor=db.cursor()
cursor.execute(create_table_query)
db.commit() '''

'''#insert
insert_db=""" INSERT INTO Account_Opening(cust_Id,dob,FULL_NAME,GENDER,city,pincode,phone)
VALUES (%s,%s,%s,%s,%s,%s,%s)
   """
data_insert=[("1001","2004-03-03","shriya guru palkar","Female","Kudal",416,"8767666218"),
             ("1002","2003-06-08","shravani shakha shedge","Female","sawantwadi",417,"9523567823"),
             ("1003","2002-07-05","mansi  sanjay sawant","male","Kudal",416,"8756443212"),
             ("1004","2001-02-02","harsh guru palkar","male","mangaon",418,"7656543423"),
             ("1005","2000-01-01","guru nana palkar","male","Kudal",416,"8765432123")
             ]
cursor=db.cursor()   
cursor.executemany(insert_db,data_insert)
db.commit()'''

'''#read
all_data= """ SELECT * FROM Account_Opening"""
cursor=db.cursor()  
cursor.execute(all_data)
my_data=cursor.fetchall()
for d in my_data:
   print(d)
db.commit() '''

'''#Update 
my_update='UPDATE Account_Opening\
   SET pincode=419 WHERE cust_Id=1004'
cursor=db.cursor()  
cursor.execute(my_update)
db.commit()   
all_data= """ SELECT * FROM Account_Opening"""
cursor=db.cursor()  
cursor.execute(all_data)
my_data=cursor.fetchall()
for d in my_data:
   print(d)
db.commit()    '''

#delete
my_delete="""DELETE FROM Account_Opening WHERE cust_Id=1005"""
cursor=db.cursor() 
cursor.execute(my_delete)
db.commit()