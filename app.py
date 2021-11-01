from flask import Flask,render_template,request
import jsonify
import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open('vehicle_predictor_model.pkl','rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        Year = int(request.form['Year'])
        Present_price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Owner = int(request.form['Owner'])
        Fuel_Type_Petrol = request.form['Fuel_Type_Petrol']
        if(Fuel_Type_Petrol=='Petrol'):
            Fuel_Type_Petrol = 1
            Fuel_Type_Diesel = 0
        elif(Fuel_Type_Petrol=='Diesel'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        else:
            Fuel_Type_Diesel=0
            Fuel_Type_Petrol=0
        Year = 2021-Year
        Seller_Type_Individual = request.form['Seller_Type_Individual']
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0
        Transmission_Type = request.form['Transmission_Mannual']
        if(Transmission_Type=='Mannual'):
            Transmission_Type=1
        else:
            Transmission_Type=0
        prediction = model.predict([[Present_price,Kms_Driven,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Type]])
        output = round(prediction[0],2)
        return render_template('index.html',prediction_text="Your Cars Value is {}".format(output))
            
    else:
        return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)    