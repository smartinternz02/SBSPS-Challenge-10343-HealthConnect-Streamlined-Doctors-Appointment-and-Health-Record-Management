# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 13:58:50 2023

@author: Shivani_SB
"""
def showall():
    sql= "SELECT * from APP"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The Name is : ",  dictionary["SERVICE"])
        print("The E-mail is : ", dictionary["NAME"])
        print("The Contact is : ",  dictionary["DATE"])
        print("The Adress is : ",  dictionary["DOCTOR"])
        print("The Role is : ",  dictionary["EMAIL"])
        print("The Branch is : ",  dictionary["TIME"])
        dictionary = ibm_db.fetch_both(stmt)
             
def getdetails(email):
    sql= "select * from APP where email='{}'".format(email)
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The Name is : ",  dictionary["SERVICE"])
        print("The E-mail is : ", dictionary["NAME"])
        print("The Contact is : ", dictionary["DATE"])
        print("The Address is : ", dictionary["DOCTOR"])
        print("The Role is : ", dictionary["EMAIL"])
        print("The Branch is : ", dictionary["TIME"])
        dictionary = ibm_db.fetch_both(stmt)
        
def insertdb(conn,service,name,date,doctor,email,time):
    sql= "INSERT into APP VALUES('{}','{}','{}','{}','{}','{}')".format(service,name,date,doctor,email,time)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))

try:
    import ibm_db
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=6667d8e9-9d4d-4ccb-ba32-21da3bb5aafc.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30376;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=fwt38810;PWD=WdKnRRL5uvCjHjzQ",'','')
    print(conn)
    print("connection successful...")
    #insertdb(conn,"service1","Hari",'01-06-2023','Adarsh','manu@gmail.com','10:00')
    getdetails("manu@gmail.com")
    #showall()

except:
    print("Error connecting to the database")



