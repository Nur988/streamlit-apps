import streamlit as st
import codecs
import pandas as  pd
from pandas_profiling import ProfileReport
import streamlit.components.v1 as components
import ht
from streamlit_pandas_profiling import st_profile_report
import sweetviz as sv
import matplotlib
import os
from PIL import Image
import eda
import NLP

st.set_page_config(layout='wide',initial_sidebar_state='collapsed')
def st_display_sweetviz(report_html,width=1000,height=500):
    report_file=codecs.open(report_html,'r')
    page=report_file.read()
    components.html(page,width=width,height=500,scrolling=True)






def main():
    menu=['Home','Eda','NLP','About Me']
    choice=st.sidebar.radio("MENU",menu)
    if choice=='Eda':
        st.subheader("EDA")
        eda.eda()
    elif choice=='NLP':
        NLP.NLP()
        

    elif choice=='About Me':
        
        st.subheader("About Me")
        image=Image.open('cv.jpg')
        st.image(image,height=1000,width=1500)
    else :
        
        #HtmlFile = open("index.html", 'r', encoding='utf-8')
        #source_code = HtmlFile.read() 

        #components.html(source_code,height=800,width=800)
        #st.header("WELCOME TO MY WEBSITE")
        image = Image.open('1.jpg')
        components.html(ht.header2,height=150,width=1500)
        #st.title("WELCOME TO MY WEBSITE")
        st.image(image,width=1500)
        components.html(ht.header3,height=1500,width=1500)
        
                   


if __name__=='__main__':
    main()
