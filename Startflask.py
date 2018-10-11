from flask import Flask, render_template, request
from flask_mysqldb import MySQL



app = Flask(__name__)

# configure db

app.config['MYSQL_HOST']='127.0.0.1'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Asusfra/12345'
app.config['MYSQL_DB']='sme_tracker'

mysql = MySQL(app)






@app.route("/", methods=['GET','POST'])
def register_form():
    if request.method=='POST':
        userDetails = request.form
        First_Name = userDetails['FirstName']
        Last_Name=userDetails['LastName']
        Gender=userDetails['Gender']
        Wipro_Email_ID=userDetails['Email']
        Password=userDetails['password']
        Confirm_Password=userDetails['confirm_password']
        Location=userDetails['Country']
        cur = mysql.connection.cursor()
        print("Connected to DB")
        cur.execute("insert into register(First_Name,Last_Name,Gender,Wipro_Email_ID,Password,Confirm_Password,Location)values(%s,%s,%s,%s,%s,%s,%s)",(First_Name,Last_Name,Gender,Wipro_Email_ID,Password,Confirm_Password,Location))
        mysql.connection.commit()
        cur.close()
        return "Successfully registered"
    return render_template("firstpage.html")



if __name__=='__main__':
     app.run(debug=True)
     app.run(host='127.0.0.1',port='80')
