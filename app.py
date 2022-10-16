from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import joblib
import traceback

app=Flask(__name__)

model=joblib.load("model.pkl")
print("model loaded")

model_cols=joblib.load("data_cols.pkl")
print("columns loaded")

@app.route("/predict", methods=["GET","POST"])



def predict():
	if model:
		try:
			json_ = request.json
			querry=pd.get_dummies(pd.DataFrame(json_))
			querry=querry.reindex(columns=model_cols , fill_value=0)
			prediction=list(model.predict(querry))
			return jsonify({"Prediction ": str(prediction)})

		except:
			return jsonify({"trace ": traceback.format_exc()})
	else:
		print("first train the model")
		return ("no model is here to use")

if __name__ == "__main__":
	app.run(debug= True)