import mysql.connector;
db=mysql.connector.connect(
    host='localhost',
    username='root',
    password='root',
    database="Bank_Opeartions"
)
'''#create table
create_table_query="""CREATE TABLE `Bank_Opeartions`.`KYC`(
       `cust_Id` int,
      `dob` date,
      `NAME` VARCHAR(50),
    `GENDER` VARCHAR(50),
    `PAN` VARCHAR(250)
)"""
#create cursor
cursor=db.cursor()
cursor.execute(create_table_query)
db.commit()'''

'''#insert
insert_db=""" INSERT INTO KYC(cust_Id,dob,NAME,GENDER,PAN)
VALUES (%s,%s,%s,%s,%s)
   """
data_insert=[("1001","2004-03-03","shriya guru palkar","Female","23456789121"),
             ("1002","2003-06-08","shravani shakha shedge","Female","95235678232"),
             ("1003","2002-07-05","mansi  sanjay sawant","male","28756443212"),
             ("1004","2001-02-02","harsh guru palkar","male","27656543423"),
             ("1005","2000-01-01","guru nana palkar","male","28765432123")
             ]
cursor=db.cursor()   
cursor.executemany(insert_db,data_insert)
db.commit()

#read
all_data= """ SELECT * FROM KYC"""
cursor=db.cursor()  
cursor.execute(all_data)
my_data=cursor.fetchall()
for d in my_data:
   print(d)
db.commit()'''

'''#Update 
my_update='UPDATE KYC\
   SET cust_Id=1006 WHERE cust_Id=1005'
cursor=db.cursor()  
cursor.execute(my_update)
db.commit()   
all_data= """ SELECT * FROM KYC"""
cursor=db.cursor()  
cursor.execute(all_data)
my_data=cursor.fetchall()
for d in my_data:
   print(d)
db.commit()  '''

#delete
my_delete="""DELETE FROM KYC WHERE cust_Id=1006"""
cursor=db.cursor() 
cursor.execute(my_delete)
db.commit()