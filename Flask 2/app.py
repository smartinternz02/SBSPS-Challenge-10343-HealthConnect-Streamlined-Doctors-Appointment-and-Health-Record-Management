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
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=6667d8e9-9d4d-4ccb-ba32-21da3bb5aafc.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30376;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=fwt38810;PWD=WdKnRRL5uvCjHjzQ",'','')
print(conn)
print("connection successful...")

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index1')
def index1():
    return render_template('index.html')
@app.route('/apply12')
def apply12():
    return render_template('appointment.html')
@app.route('/cont')
def cont():
    return render_template('contact.html')
@app.route('/abt')
def abt():
    return render_template('about.html')
@app.route('/price')
def price():
    return render_template('price.html')
@app.route('/serv')
def serv():
    return render_template('service.html')
@app.route('/team')
def team():
    return render_template('team.html')
@app.route('/test')
def test():
    return render_template('testimonial.html')





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
    return render_template('index.html')




@app.route('/contact', methods=['POST','GET'])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['msg']
        insertdb1(conn,name,email,subject,msg)
    return render_template('index.html')




@app.route('/doc', methods=['POST','GET'])
def doc():
    if request.method == "POST":
        date = request.form['date']
        service= request.form['service']
        
        insertdb2(conn,date,service)
    return render_template('team.html')




@app.route('/sign', methods=['POST','GET'])
def sign():
    if request.method == "POST":
        email = request.form['email']
        
        
        insertdb6(conn,email)
    return render_template('index.html')




@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        email = request.form['email']
        sql= "select * from APP where email='{}'".format(email)
        stmt = ibm_db.exec_immediate(conn, sql)
        userdetails = ibm_db.fetch_both(stmt)
        print(userdetails)
        if userdetails:
            session['register'] =userdetails["EMAIL"]
            return render_template('userprofile.html',name=userdetails["NAME"],email= userdetails["EMAIL"],contact= userdetails["CONTACT"],address=userdetails["ADDRESS"],role=userdetails["ROLE"],branch=userdetails["BRANCH"])
        else:
            msg = "Incorrect Email id or Password"
            return render_template("login.html", msg=msg)
    return render_template('login.html')


if __name__ =='__main__':
    app.run( debug = True,port =5000,host='0.0.0.0')
