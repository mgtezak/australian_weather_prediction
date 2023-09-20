import streamlit as st
import pandas as pd

title = "Modeling"
sidebar_name = "Modeling"

def run():

    st.title(title)
    text_1 = st.button('Naive modeling pipeline')
    if text_1 == True:
        st.write('''
        - Divide dataset into individual locations''')
        st.write('*Data Cleaning:*')
        st.write('''
        - delete all rows with any NaNs''')

        st.write('*Feature engineering:*')
        st.write('''
        - Binary encoding of rain feats
        - Only use numerical Feats
        ''')

        st.write('*Preprocessing:*')
        st.write('''
        - Standardization
        ''')
        
        st.write('*Modeling:*')
        st.write('''
        - Model with Random Forest Classifier with default parameters
        - Save F1 score for each location
        ''')
        st.image('data/images/naive_modeling_pipeline.jpg')

    show_pipeline = st.button('Elaborate modeling pipeline')
    if show_pipeline == True:
        st.write('*Data Cleaning:*')
        st.write('''
        - Delete columns with > 40% missing values
        - Interpolate remaining NaN values
        ''')
        st.image('data/images/modeling_pipeline.jpg')

        st.write('*Feature engineering:*')
        st.write('''
        - Categorical encoding 
        - Unit circle representation of wind directions
        - Using "Month" as seasonal indicator
        - (Geo-mapping of weather stations)
        ''')

        st.write('*Preprocessing:*')
        st.write('''
        - Oversampling the rainy days
        - Standardization of numerical features
        ''')
        

        st.write('*Model selection and hyperparameter tuning:*')
        st.write('''
        - Most success with the Random Forest (RF) and Support Vector Machine (SVM) classifiers
        - Using Grid Search to find optimal hyperparameters
        - Save the best F1 score (with corresponding model parameters) for each location
        ''')



    text_3 = st.button('Evaluation')
    if text_3 == True:
        st.write('*Evaluation:*')
        st.write('''
        - Large variation between different weather stations
        - No significant improvement in F1 score for locations with little rain (although the ability to predict just as well, with less features)
        - Significant improvement in F1 score for locations with more of rain
        - Final F1 score (weighted average) for the entire dataset: 0.6558 (vs 0.6073 as the "naive" score)
        ''')
        st.image('data/images/beeplot.png')

    text_4 = st.button('Challenges')
    if text_4 == True:
        st.write('*Challenges:*')
        st.write('''
        - Main challenge: strong tendency to overfit
        - Especially pronounced in dryer regions due to target imbalance  
        - Lack of data
        ''')
        st.image('data/images/scores_rainfall.png')