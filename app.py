
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('decision.pkl','rb'))
model = pickle.load(open('gaussian.pkl','rb'))
model = pickle.load(open('knear.pkl','rb'))
model = pickle.load(open('linear.pkl','rb'))
model = pickle.load(open('logistic.pkl','rb'))
model = pickle.load(open('random.pkl','rb'))

@app.route('/')
def home():
  
    return render_template("index1.html")

@app.route('/index2')
def index2():
    return render_template('index2.html')


@app.route('/index3')
def index3():
    return render_template('index3.html')


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')
@app.route('/MiniProjects')
def MiniProjects():
    return render_template('MiniProjects.html')

@app.route('/index4',methods=['GET'])
def index4():
    prediction="Neutral"
    return render_template('index4.html', prediction_text='Predicted sentimental analysis for given dataset is : {}'.format(prediction))

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
