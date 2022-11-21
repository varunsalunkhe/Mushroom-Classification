import pandas as pd
import numpy as np

data=pd.read_csv('mushrooms.csv')
data.head()

x1=data.loc[:,data.columns!='class']
x=pd.get_dummies(x1)
x.head()

y=data['class'].map({'p':0,'e':1})
y.head()

from sklearn.ensemble import RandomForestClassifier
model= RandomForestClassifier(n_estimators=100, criterion='gini')
model.fit(x,y)

import joblib
joblib.dump(model, 'model.pkl')

data_columns=x1.columns
joblib.dump(data_columns, 'data_columns.pkl')

data_cols=x.columns
joblib.dump(data_cols, 'data_cols.pkl')
