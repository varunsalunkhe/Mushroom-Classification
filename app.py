from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import joblib
import traceback

app=Flask(__name__)

model=joblib.load("model.pkl")
print("model loaded")

data_columns=joblib.load("data_columns.pkl")
print("columns loaded")

model_cols=joblib.load("data_cols.pkl")
print("columns loaded")

@app.route("/")
def hello():
	return render_template("home.html")

@app.route("/api", methods=["GET","POST"])
def predict_mush():
	if model:
		try:
			json_ = request.json
			querry=pd.get_dummies(pd.DataFrame(json_))
			querry=querry.reindex(columns=model_cols , fill_value=0)
			prediction= int(model.predict(querry))
			# return jsonify({"Prediction ": prediction})
			if prediction == 0:
				return jsonify({"Prediction ": "Poisonous"})
			else:
				return jsonify({"Prediction ": "Non-Poisonous"})



		except:
			return jsonify({"trace ": traceback.format_exc()})
	else:
		print("first train the model")
		return ("no model is here to use")


@app.route("/predict" , methods=["GET","POST"])
def predict():
	data= [str(i) for i in request.form.values()]
	print(data)
	input = pd.DataFrame(np.array(data).reshape(1,-1), columns=  data_columns)
	final_input= pd.get_dummies(input)
	final= final_input.reindex(columns=model_cols, fill_value=0)
	output = model.predict(final)[0]
	if output == 0:
		return render_template('home.html', mushroom ="The mushroom is Poisonous.")
	else:
		return render_template('home.html', mushroom ="The mushroom is Edible.")

	


if __name__ == "__main__":
	app.run(debug= True)