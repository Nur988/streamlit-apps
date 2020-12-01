import streamlit as st
import codecs
import pandas as  pd
from pandas_profiling import ProfileReport
import streamlit.components.v1 as components
import ht
from streamlit_pandas_profiling import st_profile_report
import sweetviz as sv

import os


def st_display_sweetviz(report_html,width=1000,height=500):
    report_file=codecs.open(report_html,'r')
    page=report_file.read()
    components.html(page,width=width,height=500,scrolling=True)






def main():
    menu=['Home','Pandas Profiling','SweetViz','About Me']
    choice=st.sidebar.selectbox("MENU",menu)
    if choice=='Pandas Profiling':
        st.subheader("Pandas Profile")
        data_file=st.file_uploader("Upload Csv",type=['csv'])
        if data_file is not None:
            df=pd.read_csv(data_file)
            st.dataframe(df.head())
    elif choice=='SweetViz':
        st.subheader("SweetViz")
        data_file=st.file_uploader("Upload",type=['csv'])
        if data_file is not None:
            df=pd.read_csv(data_file)
            st.dataframe(df.head())
            if st.button("Generate Sweetviz Report"):
                report=sv.analyze(df)
                a=report.show_html
                
                

    elif choice=='About Me':
        st.subheader("About Me")
        components.html(ht.about,height=1200,width=1000)
    else :
        
        #st.header("WELCOME TO MY WEBSITE")
        components.html(ht.bootstrap,height=300,width=800)
        components.html(ht.header,height=100,width=800)           


if __name__=='__main__':
    main()
