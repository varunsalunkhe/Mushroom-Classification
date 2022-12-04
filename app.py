# from flask import Flask, request, jsonify, render_template
# import pandas as pd
# import numpy as np
# import joblib
# import traceback

# app=Flask(__name__)

# model=joblib.load("model.pkl")
# print("model loaded")

# data_columns=joblib.load("data_columns.pkl")
# print("columns loaded")

# model_cols=joblib.load("data_cols.pkl")
# print("columns loaded")

# @app.route("/")
# def hello():
# 	return render_template("home.html")

# @app.route("/api", methods=["GET","POST"])
# def predict_mush():
# 	if model:
# 		try:
# 			json_ = request.json
# 			querry=pd.get_dummies(pd.DataFrame(json_))
# 			querry=querry.reindex(columns=model_cols , fill_value=0)
# 			prediction= int(model.predict(querry))
# 			# return jsonify({"Prediction ": prediction})
# 			if prediction == 0:
# 				return jsonify({"Prediction ": "Poisonous"})
# 			else:
# 				return jsonify({"Prediction ": "Non-Poisonous"})



# 		except:
# 			return jsonify({"trace ": traceback.format_exc()})
# 	else:
# 		print("first train the model")
# 		return ("no model is here to use")


# @app.route("/predict" , methods=["GET","POST"])
# def predict():
# 	data= [str(i) for i in request.form.values()]
# 	print(data)
# 	input = pd.DataFrame(np.array(data).reshape(1,-1), columns=  data_columns)
# 	final_input= pd.get_dummies(input)
# 	final= final_input.reindex(columns=model_cols, fill_value=0)
# 	output = model.predict(final)[0]
# 	if output == 0:
# 		return render_template('home.html', mushroom ="The mushroom is Poisonous.")
# 	else:
# 		return render_template('home.html', mushroom ="The mushroom is Edible.")

	


# if __name__ == "__main__":
# 	app.run(debug= True)

from flask import Flask, render_template, request, url_for, redirect, session,jsonify
import pymongo
import bcrypt
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)
app.secret_key = "testing"
client = pymongo.MongoClient("mongodb+srv://sourabh108:Pass123@cluster0.bp2fo.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('Mushroom')
records = db.register


model=joblib.load("model.pkl")
print("model loaded")

data_columns=joblib.load("data_columns.pkl")
print("columns loaded")

model_cols=joblib.load("data_cols.pkl")
print("columns loaded")

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
        password2 = request.form.get("password2")

        user_found = records.find_one({"name": user})
        email_found = records.find_one({"email": email})

        if user_found:
            message = 'There already is a user by that name'
            return render_template('signin.html',message = message)

        if email_found:
            message = 'This email already exists in database'
            return render_template('signin.html',message = message)

        if password1 != password2:
            message = 'Passwords should match!'
            return render_template('signin.html',message = message)
        else:
            hashed = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
            user_input = {'name': user, 'email': email, 'password': hashed}
            records.insert_one(user_input)
            
            user_data = records.find_one({"email": email})
            new_email = user_data['email']
            session["email"] = new_email
            if "email" in session:
                    return redirect(url_for("dashboard"))
            return render_template('dashboard.html',email = new_email)    
    return render_template("signin.html")

@app.route("/dashboard" , methods=["GET","POST"])
def predict():
    if "email" in session:
        email = session["email"]
        data= [str(i) for i in request.form.values()]
        print(data)
        input = pd.DataFrame(np.array(data).reshape(1,-1), columns=  data_columns)
        final_input= pd.get_dummies(input)
        final= final_input.reindex(columns=model_cols, fill_value=0)
        output = model.predict(final)[0]
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
        return render_template("login.html")
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)