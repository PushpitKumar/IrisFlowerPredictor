from flask import Flask, render_template, request
from flask_cors import cross_origin
import jsonify
import requests
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('iris.pkl','rb'))

@app.route('/',methods=['GET'])
@cross_origin()
def Home():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method=='POST':

        #Petal Length
        petal_length = float(request.form['PetalLength'])

        #Petal Width
        petal_width = float(request.form['PetalWidth'])

        prediction = model.predict([[petal_length,petal_width]])

        result = prediction[0]

        return render_template('home.html',prediction_text='The flower is {}'.format(result))

    return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True)
