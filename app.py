
from flask import Flask, render_template, request, url_for, redirect, session,jsonify
import pymongo
import bcrypt
import pandas as pd
import numpy as np
import joblib
from logger.logger import Logs



log = Logs("logs.log")
log.addLog("INFO", "Execution started Successfully !")



app = Flask(__name__)
app.secret_key = "testing"

try:

    file1 = open("Userinfo.txt","r")
    userinfolist=file1.readlines()
    Userkey=""+userinfolist[0][9:-1]+":"+userinfolist[1][9:-1]
    print(Userkey)
    file1.close()
    mongodbcompassURlconnection="mongodb+srv://"+Userkey+"@cluster0.bp2fo.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(mongodbcompassURlconnection)
except Exception as error:
    print("mongodb client connection error")
    log.addLog("ERROR","Error while connecting client")

try:
    db = client.get_database('Mushroom')
    records = db.register
except Exception as error:
    print("Error while getting/creating database")
    log.addLog("ERROR","Error while getting/creating database")




model=joblib.load("model.pkl")
log.addLog("INFO","model loaded")

data_columns=joblib.load("data_columns.pkl")
log.addLog("INFO","columns loaded")

model_cols=joblib.load("data_cols.pkl")
log.addLog("INFO","columns loaded")

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    if "email" in session:
        email = session["email"]
        return render_template('dashboard.html', email=email)
    else:
        return render_template("login.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    message = 'Please login to your account'
    if "email" in session:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

       
        email_found = records.find_one({"email": email})
        if email_found:
            email_val = email_found['email']
            passwordcheck = email_found['password']
            
            if bcrypt.checkpw(password.encode('utf-8'), passwordcheck):
                session["email"] = email_val
                log.addLog("INFO","Login Successful")

                return redirect(url_for('dashboard'))
            else:
                if "email" in session:
                    return redirect(url_for("dashboard"))
                message = 'Wrong password'
                return render_template('login.html', message=message)
        else:
            message = 'Email not found'
            return render_template('login.html', message=message)
    return render_template('login.html', message=message)

@app.route("/signin", methods=['post', 'get'])
def signin():
    message = ''
    if "email" in session:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        user = request.form.get("fullname")
        email = request.form.get("email")

        password1 = request.form.get("password1")
        recheck_password = request.form.get("recheck_password")

        user_found = records.find_one({"name": user})
        email_found = records.find_one({"email": email})

        if user_found:
            message = 'There already is a user by that name'
            return render_template('signin.html',message = message)

        if email_found:
            message = 'This email already exists in database'
            return render_template('signin.html',message = message)

        if password1 != recheck_password:
            message = 'Passwords should match!'
            return render_template('signin.html',message = message)
        else:
            hashed = bcrypt.hashpw(recheck_password.encode('utf-8'), bcrypt.gensalt())
            user_input = {'name': user, 'email': email, 'password': hashed}
            records.insert_one(user_input)
            
            user_data = records.find_one({"email": email})
            new_email = user_data['email']
            session["email"] = new_email
            log.addLog("INFO","Signin Successful")

            if "email" in session:
                    return redirect(url_for("dashboard"))
            return render_template('dashboard.html',email = new_email)    
    return render_template("signin.html")

@app.route("/dashboard" , methods=["GET","POST"])
def predict():
    if "email" in session:
        email = session["email"]
        data= [str(i) for i in request.form.values()]
        input = pd.DataFrame(np.array(data).reshape(1,-1), columns=  data_columns)
        final_input= pd.get_dummies(input)
        final= final_input.reindex(columns=model_cols, fill_value=0)
        log.addLog("INFO","Model is running")
        output = model.predict(final)[0]
        log.addLog("INFO","Model given output")
        if output == 0:
            return render_template('dashboard.html', mushroom ="The mushroom is Poisonous.",email = email)
        else:
            return render_template('dashboard.html', mushroom ="The mushroom is Edible.",email = email)
    else:
        return render_template("login.html")



@app.route("/logout", methods=["POST", "GET"])
def logout():
    if "email" in session:
        session.pop("email", None)
        log.addLog("INFO","Logout successful")
        return render_template("login.html")
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False)