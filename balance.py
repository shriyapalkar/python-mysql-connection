import mysql.connector;
db=mysql.connector.connect(
    host='localhost',
    username='root',
    password='root',
    database="Bank_Opeartions"
)
'''#create table
create_table_query="""CREATE TABLE `Bank_Opeartions`.`Balance_inquiry`(
       `cust_Id` int,
      `dob` date,
      `NAME` VARCHAR(50),
    `GENDER` VARCHAR(50),
    `PAN` VARCHAR(10),
    `acc` VARCHAR(10)
)"""
#create cursor
cursor=db.cursor()
cursor.execute(create_table_query)
db.commit()'''
'''#insert
insert_db=""" INSERT INTO Balance_inquiry(cust_Id,dob,NAME,GENDER,PAN,acc)
VALUES (%s,%s,%s,%s,%s,%s)
   """
data_insert=[("1001","2004-03-03","shriya guru palkar","Female","23456","saving"),
             ("1002","2003-06-08","shravani shakha shedge","Female","9523","saving"),
             ("1003","2002-07-05","mansi  sanjay sawant","male","2875","debit"),
             ("1004","2001-02-02","harsh guru palkar","male","276","credit"),
             ("1005","2000-01-01","guru nana palkar","male","2873","saving")
             ]
cursor=db.cursor()   
cursor.executemany(insert_db,data_insert)
db.commit()'''

'''#read
all_data= """ SELECT * FROM Balance_inquiry"""
cursor=db.cursor()  
cursor.execute(all_data)
my_data=cursor.fetchall()
for d in my_data:
   print(d)
db.commit()'''

'''#Update 
my_update='UPDATE Balance_inquiry\
   SET cust_Id=1006 WHERE cust_Id=1005'
cursor=db.cursor()  
cursor.execute(my_update)
db.commit()   
all_data= """ SELECT * FROM Balance_inquiry"""
cursor=db.cursor()  
cursor.execute(all_data)
my_data=cursor.fetchall()
for d in my_data:
   print(d)
db.commit()  '''

#delete
my_delete="""DELETE FROM Balance_inquiry WHERE cust_Id=1006"""
cursor=db.cursor() 
cursor.execute(my_delete)
db.commit()