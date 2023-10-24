import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
def app() :
    st.title('Analysis')
    st.subheader('Customized Graph (Relation Between Price and Odometer) Based On Selection'  , divider='rainbow')
    df=pd.read_csv('Cleaned_Vehicles_Data.csv')
    df.drop('Unnamed: 0',axis=1,inplace=True)
    year = st.select_slider('Please,Select Year .',np.sort(df['year'].unique()),value=(df['year'].min(),df['year'].max())  )
    odometer = st.slider('Please,Select Ododmeter.',value=(df['odometer'].min(),df['odometer'].max()))
    man =  st.multiselect(
    'Please, Select The Manufacturer you Want or Select All',
    np.append(df['manufacturer'].unique(),'All'),
    ['All'])
    cond =  st.multiselect(
    'Please, Select The Condition you Want or Select All with considering that new condition is like new condition and salvage condition is fair condition',
    np.append(df['condition'].unique(),'All'),
    ['All'])
    cylinder =  st.multiselect(
    'Please, Select The Number of Cylinders you Want or Select All',
    np.append(df['cylinders'].unique(),'All'),
    ['All'])
    fuel =  st.multiselect(
    'Please, Select The Fuel Type you Want or Select All',
    np.append(df['fuel'].unique(),'All'),
    ['All'])
    tit =  st.multiselect(
    'Please, Select The Title Status you Want or Select All',
    np.append(df['title_status'].unique(),'All'),
    ['All'])
    trans =  st.multiselect(
    'Please, Select The Transmission Type you Want or Select All',
    np.append(df['transmission'].unique(),'All'),
    ['All'])
    drive =  st.multiselect(
    'Please, Select The Drive Type you Want or Select All',
    np.append(df['drive'].unique(),'All'),
    ['All'])
    type =  st.multiselect(
    'Please, Select The Type Of Car you Want or Select All',
    np.append(df['type'].unique(),'All'),
    ['All'])
    df1=df.copy(deep=True) 
    df1=df1[(df1['year'] > year[0])  &  (df1['year'] < year[1]) ]
    df1=df1[(df1['odometer'] > odometer[0])  &  (df1['odometer'] < odometer[1])]
    if 'All' not in man :
        df1=df1[df1['manufacturer'].isin(man)]
    if 'All' not in cond :
        df1=df1[df1['condition'].isin(cond)]
    if  'All' not in cylinder :
        df1=df1[df1['cylinders'].isin(cylinder)]
    if  'All' not in fuel :
        df1=df1[df1['fuel'].isin(fuel)]
    if  'All' not in tit :
        df1=df1[df1['title_status'].isin(tit)]
    if 'All' not in trans :
        df1=df1[df1['transmission'].isin(trans)]
    if  'All' not in drive :
        df1=df1[df1['drive'].isin(drive)]
    if 'All' not in type :
        df1=df1[df1['type'].isin(type)]
    if st.button("Confirm", type="primary"): 
        fig = px.scatter(data_frame = df1 , x='odometer', y='price', hover_data=df.columns,title = 'Relation Between Price and Odometer' ,size= df1['price'])
        st.plotly_chart(fig, use_container_width=True)
    st.subheader('Pie Chart For Every Feature Based On Selection'  , divider='rainbow')
    option = st.selectbox(
    'Please, Select Feature?',
    df.select_dtypes('object').columns,
    placeholder="Select Feature...")
    fig1 = px.pie(df,names=option)
    st.plotly_chart(fig1, use_container_width=True)
    st.subheader('Line Chart Of Price With Model Year For A Specific Manufacturer Selection'  , divider='rainbow')
    option1 = st.selectbox(
    'Please, Select Manufacturer?',
    df['manufacturer'].unique(),
    placeholder="Select Manufacturer...")
    df5 = df[df['manufacturer'] == option1].groupby('year').mean().reset_index()
    df6 = df[df['manufacturer'] == option1].groupby('year').count().reset_index()
    df5['Count Of Cars In This Year'] = df6['fuel']
    fig2 = px.line(data_frame=df5, x='year',y='price',hover_data=['Count Of Cars In This Year'])
    st.plotly_chart(fig2, use_container_width=True)


