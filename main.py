from flask import Flask,render_template,request
import joblib
from os import path
import pandas as pd
import numpy as np


filename = "random_forest_pipeline2.pkl"
rf_model = joblib.load(path.join("model", filename))

app=Flask(__name__)

@app.route("/")
def my_form():
    return render_template("welcome page.html")

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/prediction2')
def prediction2():
    return render_template('prediction2.html')

# Route to handle form submission and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    N = request.form["N"]
    P = request.form["P"]
    K = request.form["K"]
    pH = request.form["pH"]
    EC = request.form["EC"]
    S = request.form["S"]
    Cu = request.form["Cu"]
    Fe = request.form["Fe"]
    Mn = request.form["Mn"]
    Zn = request.form["Zn"]
    B = request.form["B"]
    
    col = ['N', 'P', 'K', 'ph', 'EC', 'S', 'Cu', 'Fe', 'Mn', 'Zn', 'B']
    input_data = np.array([[float(N), float(P), float(K), float(pH), float(EC), float(S), 
                        float(Cu), float(Fe), float(Mn), float(Zn), float(B)]])

    df_input = pd.DataFrame(input_data, columns=col)

# Now, apply the pipeline to make predictions
    predi = rf_model.predict(df_input)
    crop_dict={0:'pomegranate', 1:'mango' ,2: 'grapes',3: 'mulberry',4: 'ragi',5: 'potato'}
    return render_template("result.html",prediction=crop_dict[predi[0]])
if __name__=="__main__":
    app.run(debug=True)