from flask import Flask,render_template,request
import joblib
from os import path
import pandas as pd
import numpy as np
import math

filename = "random_forest_pipeline2.pkl"
rf_model = joblib.load(path.join("model", filename))
crop_yield  = joblib.load(path.join("model", "crop_yield_pipeline2.pkl"))

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


@app.route('/predict2', methods=['POST'])
def predict2():
    sph = request.form["sph"]
    temp = request.form["temp"]
    h = request.form["h"]
    ws = request.form["ws"]
    N = request.form["N"]
    P = request.form["P"]
    K = request.form["K"]
    sq = request.form["sq"]
    st = request.form["st"]
    ct = request.form["ct"]
    
    data = {
    'Soil_pH': sph,
    'Temperature': temp,
    'Humidity': h,
    'Wind_Speed': ws,
    'N': N,
    'P': P,
    'K': K,
    'Soil_Quality': sq,
    'Crop_Type_Barley': 0,
    'Crop_Type_Corn': 0,
    'Crop_Type_Cotton': 0,
    'Crop_Type_Potato': 0,
    'Crop_Type_Rice': 0,
    'Crop_Type_Soybean': 0,
    'Crop_Type_Sugarcane': 0,
    'Crop_Type_Sunflower': 0,
    'Crop_Type_Tomato': 0,
    'Crop_Type_Wheat': 0,
    'Soil_Type_Clay': 0,
    'Soil_Type_Loamy': 0,
    'Soil_Type_Peaty': 0,
    'Soil_Type_Saline': 0,
    'Soil_Type_Sandy': 0
}

    # Check and update soil type encoding
    if st == "Clay":
        data['Soil_Type_Clay'] = 1
    elif st == "Loamy":
        data['Soil_Type_Loamy'] = 1
    elif st == "Peaty":
        data['Soil_Type_Peaty'] = 1
    elif st == "Saline":
        data['Soil_Type_Saline'] = 1
    elif st == "Sandy":
        data['Soil_Type_Sandy'] = 1

    # Check and update crop type encoding
    if ct == "Barley":
        data['Crop_Type_Barley'] = 1
    elif ct == "Corn":
        data['Crop_Type_Corn'] = 1
    elif ct == "Cotton":
        data['Crop_Type_Cotton'] = 1
    elif ct == "Potato":
        data['Crop_Type_Potato'] = 1
    elif ct == "Rice":
        data['Crop_Type_Rice'] = 1
    elif ct == "Soybean":
        data['Crop_Type_Soybean'] = 1
    elif ct == "Sugarcane":
        data['Crop_Type_Sugarcane'] = 1
    elif ct == "Sunflower":
        data['Crop_Type_Sunflower'] = 1
    elif ct == "Tomato":
        data['Crop_Type_Tomato'] = 1
    elif ct == "Wheat":
        data['Crop_Type_Wheat'] = 1

    # Create the dataframe with the updated data
    
    df = pd.DataFrame([data])
    # Now, apply the pipeline to make predictions
    predi2 = crop_yield.predict(df)
    
    return render_template("result2.html",prediction2=math.ceil(predi2[0]))    

if __name__=="__main__":
    app.run(debug=True)