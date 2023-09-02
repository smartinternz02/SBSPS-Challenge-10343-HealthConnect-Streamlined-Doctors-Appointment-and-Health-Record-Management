

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
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=32286;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=dzy09011;PWD=c2cuoQO0QZnNcPWc",'','')
    print(conn)
    print("connection successful...")
    #insertdb(conn,"service1","Hari",'01-06-2023','Adarsh','manu@gmail.com','10:00')
    # getdetails("manu@gmail.com")
    #showall()

except:
    print("Error connecting to the database")