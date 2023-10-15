import streamlit as st 
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer,SimpleImputer
from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import OneHotEncoder , StandardScaler , LabelEncoder , MinMaxScaler , RobustScaler
from category_encoders import BinaryEncoder
from imblearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score 
from sklearn.feature_selection import SelectFromModel
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix , ConfusionMatrixDisplay
from sklearn.model_selection import cross_validate , train_test_split , StratifiedKFold , GridSearchCV , RandomizedSearchCV
from sklearn import set_config
from xgboost import XGBRegressor
import joblib
def app() :
    st.title('Used Cars Price Prediction')
    df=pd.read_csv('Cleaned_Vehicles_Data.csv')
    df.drop('Unnamed: 0',axis=1,inplace=True)
    XGB=joblib.load('XGB')
    man =  st.selectbox(
    'Please, Select The Manufacturer',
    df['manufacturer'].unique()
    ,index=None,
    placeholder="Select Manufacturer...")
    cond =  st.selectbox(
    'Please, Select The Condition with considering that new condition is like new condition and salvage condition is fair condition',
    df['condition'].unique()
    ,index=None,
    placeholder="Select Condition Of The Car...")
    cylinder =  st.selectbox(
    'Please, Select The Number of Cylinders',
    df['cylinders'].unique(),index=None,
    placeholder="Select Number Of Cylinders...")
    fuel =  st.selectbox(
    'Please, Select The Fuel Type',
    df['fuel'].unique(),index=None,
    placeholder="Select Fuel Type...")
    tit =  st.selectbox(
    'Please, Select The Title Status',
    df['title_status'].unique(),index=None,
    placeholder="Select Title Status Of The Car...")
    trans =  st.selectbox(
    'Please, Select The Transmission Type',
    df['transmission'].unique(),index=None,
    placeholder="Select Transmiision Type...")
    drive =  st.selectbox(
    'Please, Select The Drive Type',
    df['drive'].unique(),index=None,
    placeholder="Select Drive Type...")
    type =  st.selectbox(
    'Please, Select The Type Of Car',
    df['type'].unique(),index=None,
    placeholder="Select Type Of The Car...")
    odometer = st.number_input("The Traveled Distance of car", value=None, placeholder="Insert a number...")
    year = st.number_input("Model Year", value=None, placeholder="Type a number...")
    if st.button('Submit', type="primary") :
        x , y = df.drop(['price'] , axis = 1) , df['price']
        XGB.fit(x,y)
        pred=XGB.predict(pd.DataFrame(data=[[year,man,cond,cylinder,fuel,odometer,tit,trans,drive,type]],columns=df.columns[1:]))[0]
        st.write('The Expected Price is ',pred)



    
