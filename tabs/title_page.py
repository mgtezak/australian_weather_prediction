import streamlit as st

title = "Australian Weather Prediction"
sidebar_name = "Introduction"


def run():
    st.title(title)
    st.header('Team: Edgar Arndt, Robert Becker, Michael Tezak, Stefan Thoss')
    st.image('data/images/australia-satellite.jpg')
    st.write("""For several hundreds of years the prediction of the weather has been of large interest for private persons, groups 
            and organizations. Before the invention of computers, people tried to predict weather by measuring a few simple variables,
            like pressure and humidity.\n\nThese variables were already decent in predicting, for example, if it is going to rain or not for the current or next day.
            Today, computers enable weather forecasts to become much more advanced and can reach much further in the future. Traditionally, weather is predicted with physical models, 
            but the rise of machine learning has opened a new path for this task. Using machine learning models in order 
            to predict the likelihood of future rain in different regions is interesting for a number of reasons. 
            From a scientific point of view one might want to gain a deeper understanding of how the weather works 
            in general and find out which factors correlate most strongly with future occurrences of rain.\n\n""")
