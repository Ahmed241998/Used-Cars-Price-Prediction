import streamlit as st
import pandas as pd
def app() :
    st.title('Data')
    st.header('This Data is Scraped From Craigslist at 2021')
    df=pd.read_csv("Cleaned_Vehicles_Data.csv")
    df.drop('Unnamed: 0',axis=1,inplace=True)
    st.dataframe(df)