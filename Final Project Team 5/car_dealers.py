import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template,send_from_directory
import pickle 
import sys
import os

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
model = pickle.load(open('pickle/pricing_model.pkl', 'rb'))
cosine_sim = pickle.load(open('pickle/cosine_sim.pkl', 'rb'))
indices = pickle.load(open('pickle/indices.pkl', 'rb'))
car_sales = pickle.load(open('pickle/car_sales.pkl', 'rb'))

df = pickle.load(open('pickle/User_Details.pkl', 'rb'))
discount_rate = 1


@app.route('/')
def index():
    return render_template('index.html')	


@app.route('/segmentation')
def segmentation():
    return render_template('segmentation.html')


@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html')

@app.route('/pricing',methods=["GET", "POST"])
def pricing():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == 'GET':
        return render_template('pricing.html')
    
    elif request.method == 'POST':
        int_features = [float(x) for x in request.form.values()]
        final_features = [np.array(int_features)]

        prediction = model.predict(final_features)
        output = round(prediction[0], 2)
        final_price = prediction * discount_rate
        price = round(final_price[0], 2)
        if(discount_rate == 1):
            return render_template('pricing.html',  base_price='The base price of the car is $ {}K'.format(output))
        else:
	        return render_template('pricing.html',  base_price='The base price of the car is $ {}K'.format(output),
			prediction_text='The price for your segment is $ {}K'.format(price))


@app.route('/segment', methods=['GET', 'POST'])
def segment():
    global discount_rate
    if request.method == 'GET':
        return render_template('segmentation.html')

    elif request.method == 'POST':
	
        customer_id = request.form.get('cust_id')
        cust = np.int(customer_id)
        if cust in df['CustomerID'].values:
            score = df[df['CustomerID'] == cust]['OverallScore'].to_numpy()[0]
            revenue = df[df['CustomerID'] == cust]['Revenue'].to_numpy()[0]
            #price = round(revenue, 2)
            if (score <= 3 & score >= 0):
                cust_type = 'Silver Customer'
                disc = 10
                discount_rate = 0.9
                segment_name = 'silver.JPG'
            elif (score <= 6 & score >= 4):
                cust_type = 'Gold Customer'
                disc = 20
                discount_rate = 0.8
                segment_name = 'gold.JPG'
            elif (score >= 7):
                cust_type = 'Platinum Customer'
                disc = 30
                discount_rate = 0.7
                segment_name = 'platinum.JPG'
				
				
            return render_template('segmentation.html', customer_score='Customer score is  {} out of 9'.format(score),
                                   customer_type=cust_type,
                                   revenue='Customer Net worth is {}'.format(revenue), discount=discount_rate,segment_name=segment_name)
        else:
            segment_name = 'bronze.JPG'
            discount_rate = 1
            return render_template('segmentation.html', customer_message='Welcome, You are our new Customer!',segment_name=segment_name)
			

@app.route('/recommend',methods = ['GET', 'POST'])
def recommend():
    if request.method == 'GET':
        return render_template('recommendation.html')

    elif request.method == 'POST':
        model=request.form.get('model_id')
        if model in car_sales['Model'].values:
            idx = indices[model]

            sim_scores = list(enumerate(cosine_sim[idx]))

            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

            sim_scores = sim_scores[1:5]

            car_indices = [i[0] for i in sim_scores]
            arr = car_sales[['Model', 'Manufacturer','Path']].iloc[car_indices]
            image_names = arr['Path'].to_numpy()[0:4]

            return render_template('recommendation.html', model_mod="Model", model_man="Manufacturer" ,model_mod1=arr.iloc[0,0], model_mod2=arr.iloc[1,0], model_mod3=arr.iloc[2,0], model_mod4=arr.iloc[3,0], model_man1=arr.iloc[0,1], model_man2=arr.iloc[1,1], model_man3=arr.iloc[2,1], model_man4=arr.iloc[3,1],image_names=image_names)
        else:
            return render_template('recommendation.html', model_message='Please enter a valid model name')

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("static/images", filename)


if __name__ == "__main__":
    app.run(debug=True)