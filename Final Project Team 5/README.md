# Final Project Team 5 - Car Dealership

#### Project Proposal : https://drive.google.com/file/d/19eOIXlJmLkiuursX8Awew86xx0ciudGu/view?usp=sharing

#### Web Application Link for User click prediction ad use case : https://cardealers1.herokuapp.com/

#### Analysis Power BI - https://app.powerbi.com/groups/me/reports/aff843c7-d681-4d2d-8647-77c1a54244f5?ctid=6abfc73f-da64-4137-9f9f-15faae56f685

#### User Doc for Application:

This is web application for Car Dearlers to access and provide insights like Price Prediction, User Segmentation and Recommendation requested either by Business End Users or the Customers.

#### Clat Document : https://codelabs-preview.appspot.com/?file_id=1IwvbmM0fHPVk2k8ob-9Y6tMNKFJ_z1RMZMzFlDrkMuM#0

#### Use Cases :
 1. Car Price Prediction
 2. Customer Segmentation and CLTV
 3. Price Prediction as per Customer Segmentation
 4. Car Models Recommendation
 
#### Workflow :

![](https://github.com/KumarAnand11/INFO7374DigitalMarketingAnalytics/blob/master/Final%20Project%20Team%205/static/images/workflow.JPG)

#### Data 

• https://github.com/KumarAnand11/INFO7374DigitalMarketingAnalytics/blob/master/Final%20Project%20Team%205/data/Input/Car_sales.csv

• https://github.com/KumarAnand11/INFO7374DigitalMarketingAnalytics/blob/master/Final%20Project%20Team%205/data/Input/OnlineRetail.csv

• https://github.com/KumarAnand11/INFO7374DigitalMarketingAnalytics/blob/master/Final%20Project%20Team%205/data/Output/Main.csv


#### Python Notebooks

We have one module for each case for manual implementation of predictive models for use cases.


1.  *car_dealers.py* - Flask Application to drive all the models for below mentioned notebooks using the pickle files created in each model
    +   Flask Python files to call pickle file (texts and labels).
    +   html in the static folder

2.  *pricing.ipynb* - Jupyter notebook for Predicting the Price using the Linear Regression model
    
3.  *Car_Recommendation.ipynb* - Jupyter notebook for Car Recommendation- the recommendation model is Content Based

4.  *Customer Segmentation and CLTV.ipynb* - Jupyter notebook for Customer Segmentation & CLTV

#### Requirements

	•   Flask==1.1.1
	•   gunicorn==19.9.0
	•   itsdangerous==1.1.0
	•   Jinja2==2.10.1
	•   MarkupSafe==1.1.1
	•   Werkzeug==0.15.5
	•   numpy>=1.9.2
	•   scipy>=0.15.1
	•   scikit-learn>=0.18
	•   matplotlib>=1.4.3
	•   pandas>=0.19
	•   statsmodels==0.11.1


