import streamlit as st
import pandas as pd


title = "Data Exploration & Visualization"
sidebar_name = "Data Exploration & Visualization"


def run():
    st.title(title)
    st.header('General Information')
    st.image('data/images/climatic_zones.png', width = 500) 
    st.write("""Many different climatic zones in Australia""")
    load_dataframe = st.button('Load Dataframe')
    if load_dataframe == True:
        df = pd.read_csv('data/csv_files/weatherAUS.csv')
        st.dataframe(df)
        statistics = df.describe()
        st.write(statistics)
        st.write("""In total: 145460 entries in 23 columns."""
                "\n\n"
                 "Source: Australian Government: Bureau of Meteorology")

    missingvalues = st.button('Show Missing Values')  
    if missingvalues == True:
        st.image('data/images/missing_values.png')

    heatmap = st.button('Show Heatmap')
    if heatmap == True:
        st.image('data/images/heatmap.png')
        st.image('data/images/heatmap_big.png')
    
    rainfall = st.button('Show Distribution of Rainfall')
    if rainfall == True:
        st.image('data/images/rainfall.png')

    
