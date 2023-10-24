import streamlit as st

from streamlit_option_menu import option_menu

import Analysis,Data,Description,Prediction
st.set_page_config(
        page_title="Used Cars Prices Project",
)




class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Used Cars Sections',
                options=['Descrption','Analysis','Used Car Price Prediction','Data'],
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Descrption":
            Description.app()
        if app == "Analysis":
            Analysis.app()    
        if app == "Used Car Price Prediction":
            Prediction.app()        
        if app == 'Data':
            Data.app() 
             
    run()          
