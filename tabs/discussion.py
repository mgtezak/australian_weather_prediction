import streamlit as st
from st_clickable_images import clickable_images
import base64

title = "Discussion"
sidebar_name = "Discussion"

PATH_TO_IMAGES = 'data/images/'
IMAGE_NAMES = ['Clustering.png', 'TSA.png', 'RNN.png', 'Monsoon.png']


def run():
    st.title(title)

    images = []
    for image in IMAGE_NAMES:
        with open(PATH_TO_IMAGES + image, "rb") as image:
            encoded = base64.b64encode(image.read()).decode()
            images.append(f"data:image/jpeg;base64,{encoded}")

    clicked = clickable_images(
        images,
        titles=[f"Image #{str(i)}" for i in range(len(images))],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "5px", "height": "200px", "border-radius": "20%", },
    )

    if clicked == 0:
        st.markdown(
            """
            # Clustering
            \U0001f468\u200D\U0001f4bb What we did:
            - computed regional clusters using HCA
            - for 2 clusters, we trained an xgb model with  
                - f1-score: 0.66 for first cluster 
                - f1-score 0.60 for second cluster
            
            \U0001F4AD What we thought about doing :
            - test different cluster sizes (4, 8, 24, ...)
            - try different models on different clusters
            """
            )
        
    elif clicked == 1:
        st.markdown(
            """ 
            # Time Series Analysis
            \U0001f468\u200D\U0001f4bb What we did:
            - analysis of the data, estimating the SARIMA parameters
            - SARIMA (briefly) -> Without success
            
            \U0001F4AD What we thought about doing :
            - train a model to predict multiple days in the future
            - work with the bigger dataset
            - do multivariate timeseries anaylsis
            """
        )

    elif clicked == 2:
        st.markdown(
            """ 
            # Recurrent Neural Networks
            \U0001f468\u200D\U0001f4bb What we did:
            - nothing
                - not enough features to expect a significant increase in predictive power
            """
        )

    elif clicked == 3:
        st.markdown(
            """ 
            # Feature Engineering
            \U0001f468\u200D\U0001f4bb What we did:
            - introduce the features like monsoon, seasons -> With little success
            
            \U0001F4AD What we thought about doing :
            - Exploit wind direction and geographical data
            """
        )

    else:
        st.markdown(
            """ 
            """
        )

   
  
   


