from flask import Flask, render_template, request,session

app = Flask(__name__)
app.secret_key ='a'
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
        print("The Contact is : ",  dictionary["DATE"])
        print("The Adress is : ",  dictionary["DOCTOR"])
        print("The Role is : ",  dictionary["EMAIL"])
        print("The Branch is : ",  dictionary["TIME"])
        dictionary = ibm_db.fetch_both(stmt)
        
def insertdb(conn,service,name,date,doctor,email,time):
    sql= "INSERT into APP VALUES('{}','{}','{}','{}','{}','{}')".format(service,name,date,doctor,email,time)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))
    
def insertdb1(conn,name,email,subject,msg):
    sql= "INSERT into CONTACT VALUES('{}','{}','{}','{}')".format(name,email,subject,msg)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))

    
def insertdb2(conn,date,service):
    sql= "INSERT into DOCTOR VALUES('{}','{}')".format(date,service)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))


    
def insertdb6(conn,email):
    sql= "INSERT into SIGNUP VALUES('{}')".format(email)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))


import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=32286;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=dzy09011;PWD=c2cuoQO0QZnNcPWc",'','')
print(conn)
print("connection successful...")

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/appointment1')
def appointment1():
    return render_template('appointment.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/learn')
def learn():
    return render_template('learn.html')
@app.route('/xray')
def xray():
    return render_template('xray.html')
@app.route('/lab')
def lab():
    return render_template('lab.html')
@app.route('/pharma')
def pharma():
    return render_template('pharma.html')
@app.route('/op')
def op():
    return render_template('op.html')
@app.route('/ambulance')
def ambulance():
    return render_template('ambulance.html')
@app.route('/acco')
def acco():
    return render_template('acco.html')
@app.route('/med')
def med():
    return render_template('med.html')
@app.route('/dis')
def dis():
    return render_template('dis.html')
@app.route('/sch')
def sch():
    return render_template('sch.html')






@app.route('/apply', methods=['POST','GET'])
def apply():
    if request.method == "POST":
        service = request.form['service']
        name = request.form['name']
        date = request.form['date']
        doctor = request.form['doctor']
        email = request.form['email']
        time = request.form['time']
        #inp=[name,email,contact,address,role,branch,password]
        insertdb(conn,service,name,date,doctor,email,time)
    return render_template('home.html')



if __name__ =='__main__':
    app.run( debug = True)