import map
import time
from datetime import datetime
import pickle as pkl
import warnings
import sys
warnings.filterwarnings("ignore")

import streamlit as st
import pandas as pd
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import matplotlib.pyplot as plt
import shap

title = "Live Prediction"
sidebar_name = "Live Prediction"


def run():

    def coordinate(angle):
        radians = (np.pi / 180) * angle
        return [np.round(np.cos(radians), decimals= 2), np.round(np.sin(radians), decimals=2)]

    def check_empty(var):
        return np.nan if var == ' ' else float(var)

    def check_empty_string(var):
        return np.nan if var == ' ' else var

    columns = ['Date', 'Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation',
        'Sunshine', 'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
        'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
        'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am',
        'Temp3pm', 'RainToday']

    Locations = ['Albury', 'BadgerysCreek', 'Cobar', 'CoffsHarbour', 'Moree',
        'Newcastle', 'NorahHead', 'NorfolkIsland', 'Penrith', 'Richmond',
        'Sydney', 'SydneyAirport', 'WaggaWagga', 'Williamtown',
        'Wollongong', 'Canberra', 'Tuggeranong', 'MountGinini', 'Ballarat',
        'Bendigo', 'Sale', 'MelbourneAirport', 'Melbourne', 'Mildura',
        'Nhil', 'Portland', 'Watsonia', 'Dartmoor', 'Brisbane', 'Cairns',
        'GoldCoast', 'Townsville', 'Adelaide', 'MountGambier', 'Nuriootpa',
        'Woomera', 'Albany', 'Witchcliffe', 'PearceRAAF', 'PerthAirport',
        'Perth', 'SalmonGums', 'Walpole', 'Hobart', 'Launceston',
        'AliceSprings', 'Darwin', 'Katherine', 'Uluru']

    #links = ['http://www.bom.gov.au/climate/dwo/IDCJDW2002.latest.shtml']
    links = ['http://www.bom.gov.au/climate/dwo/IDCJDW2002.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW2005.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW2029.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW2030.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW2084.latest.shtml',
            'http://www.bom.gov.au/climate/dwo/IDCJDW2097.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW2099.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW2100.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW2111.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW2119.latest.shtml',
            'http://www.bom.gov.au/climate/dwo/IDCJDW2124.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW2125.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW2139.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW2145.latest.shtml',
            'http://www.bom.gov.au/climate/dwo/IDCJDW2146.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW2801.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW2802.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW2801.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW3005.latest.shtml',
            'http://www.bom.gov.au/climate/dwo/IDCJDW3008.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW3022.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW3049.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW3050.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW3051.latest.shtml',
            'http://www.bom.gov.au/climate/dwo/IDCJDW3059.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW2110.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW3079.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW3101.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW4019.latest.shtml',
            'http://www.bom.gov.au/climate/dwo/IDCJDW4154.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW4050.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW4128.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW5081.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW5041.latest.shtml',
            'http://www.bom.gov.au/climate/dwo/IDCJDW5049.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW5072.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW6001.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW6081.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW8014.latest.shtml',
            'http://www.bom.gov.au/climate/dwo/IDCJDW6110.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW6111.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW6119.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW6138.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW7021.latest.shtml',
            'http://www.bom.gov.au/climate/dwo/IDCJDW7025.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW8002.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW8014.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW8048.latest.shtml', 'http://www.bom.gov.au/climate/dwo/IDCJDW8056.latest.shtml']


    pages = ['Title Side','Introduction to the Project and Visualization of the Data','Modeling: Preprocessing of the Data, Modeling and Results',
            'Interpretability','Discussion']


    st.title(title)
    flowchart = st.button('Show flowchart')
    if flowchart:
        st.image('data/images/live_prediction.jpg')
    mapbutton = st.button('Show map')
    screenshot = st.button('Show website example')
    if mapbutton == True:
        st.bokeh_chart(map.fig1)
        st.bokeh_chart(map.fig2)
    if screenshot:
        st.image('./data/images/website_scraping.png')
    Location = st.selectbox('Select a Location', tuple(sorted(('Albury', 'BadgerysCreek', 'Cobar', 'CoffsHarbour', 'Moree','Newcastle', 'NorahHead', 'NorfolkIsland', 'Penrith', 'Richmond','Sydney', 'SydneyAirport', 'WaggaWagga', 'Williamtown','Wollongong', 'Canberra', 'Tuggeranong', 'MountGinini', 'Ballarat','Bendigo', 'Sale', 'MelbourneAirport', 'Melbourne', 'Mildura','Nhil', 'Portland', 'Watsonia', 'Dartmoor', 'Brisbane', 'Cairns','GoldCoast', 'Townsville', 'Adelaide', 'MountGambier', 'Nuriootpa','Woomera', 'Albany', 'Witchcliffe', 'PearceRAAF', 'PerthAirport','Perth', 'SalmonGums', 'Walpole', 'Hobart', 'Launceston','AliceSprings', 'Darwin', 'Katherine', 'Uluru'))))
    predict = st.button('Predict')
    if predict:
        with st.spinner('Scraping data from bom.gov.au'):
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
            user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
            options.add_argument(f'user-agent={user_agent}')
            driver = webdriver.Chrome(options=options)
            dict = {}
            link = links[Locations.index(Location)]
            driver.get(link)
            driver.save_screenshot('./data/images/screenshot.png')
            st.image('./data/images/screenshot.png')
            table = driver.find_elements(By.CLASS_NAME, 'data')
            rows = table[0].find_elements(By.TAG_NAME, 'tr')
            last_cells = rows[-7].find_elements(By.TAG_NAME, 'td')
            week_day = last_cells[0].text
            minTemp = check_empty(last_cells[1].text)
            maxTemp = check_empty(last_cells[2].text)
            rainfall = check_empty(last_cells[3].text)
            evaporation = check_empty(last_cells[4].text)
            sunshine = check_empty(last_cells[5].text)
            maxwindgustdir = check_empty_string(last_cells[6].text)
            maxwindgustspeed = check_empty(last_cells[7].text)
            Temperature9am = check_empty(last_cells[9].text)
            humidity9am = check_empty(last_cells[10].text)
            clouds9am = check_empty(last_cells[11].text)
            winddir9am = check_empty_string(last_cells[12].text)
            if winddir9am == 'Calm':
                windspeed9am = 0
                winddir9am = np.nan
                pressure9am = check_empty(last_cells[14-1].text)
                Temperature3pm = check_empty(last_cells[15-1].text)
                humidity3pm = check_empty(last_cells[16-1].text)
                clouds3pm = check_empty(last_cells[17-1].text)
                winddir3pm = check_empty_string(last_cells[18-1].text)
                if winddir3pm == 'Calm':
                    windspeed3pm = 0
                    winddir3pm = np.nan
                    pressure3pm = check_empty(last_cells[20-2].text)
                else:
                    windspeed3pm = check_empty(last_cells[19-1].text)
                    pressure3pm = check_empty(last_cells[20-1].text)
            else:
                windspeed9am = check_empty(last_cells[13].text)
                pressure9am = check_empty(last_cells[14].text)
                Temperature3pm = check_empty(last_cells[15].text)
                humidity3pm = check_empty(last_cells[16].text)
                clouds3pm = check_empty(last_cells[17].text)
                winddir3pm = check_empty_string(last_cells[18].text)
                if winddir3pm == 'Calm':
                    windspeed3pm = 0
                    winddir3pm = np.nan
                    pressure3pm = check_empty(last_cells[20-1].text)
                else:
                    windspeed3pm = check_empty(last_cells[19].text)
                    pressure3pm = check_empty(last_cells[20].text)

            if float(rainfall) >= 2:
                raintoday = 1
            else:
                raintoday = 0
            dict[Location] = [week_day, Location, minTemp, maxTemp, rainfall, evaporation, sunshine, maxwindgustdir, maxwindgustspeed, winddir9am, winddir3pm, windspeed9am, windspeed3pm, humidity9am, humidity3pm, pressure9am, pressure3pm, clouds9am, clouds3pm, Temperature9am, Temperature3pm, raintoday]
            df = pd.DataFrame([dict[Location]], columns = columns)
            averages = pd.read_csv('data/csv_files/subValues2.csv')
            averages.insert(0, 'Date', datetime.day)
            if averages.Rainfall.iloc[0] > 2:
                raintoday_average = 1
            else:
                raintoday_average = 0
            averages.insert(21,'RainToday', raintoday_average)
            st.write('The following features were missing in the scraped data and then replaced by the average of the last 5 years of that Location:')
            for i in range(df.shape[1]):
                value = df.iloc[0].values[i]
                if value != value:
                    st.write('\t- ' + str(df.columns[i]))
                    df.iloc[0,i] = averages[averages.Location == Location].iloc[0,i]
            st.write('Scraped data:')
            st.write(df)

        with st.spinner('Loading model and convert data'):
            time.sleep(2)
            vars_wind = ['WindGustDir', 'WindDir9am', 'WindDir3pm']

            WindMapping = {'E' : 0, 'ENE' : 22.5, 'NE' : 45, 'NNE' : 67.5,
                           'N' : 90, 'NNW' : 112.5, 'NW' : 135, 'WNW' : 157.5,
                           'W' : 180, 'WSW' : 202.5, 'SW' : 225, 'SSW' : 247.5,
                           'S' : 270, 'SSE' : 292.5, 'SE' : 315, 'ESE' : 337.5,
                           }
            for wind in vars_wind:
                    new_col_name_x = 'X_' + wind
                    new_col_name_y = 'Y_' + wind
                    df[new_col_name_x] = df[wind].apply(lambda x : coordinate(WindMapping[x])[0])
                    df[new_col_name_y] = df[wind].apply(lambda x : coordinate(WindMapping[x])[1])
                    df.drop(wind, axis = 1, inplace= True)
            df['month'] = datetime.now().month
            loaded_model = pkl.load(open('data/final_models/' + str(Location) + '.pkl', 'rb'))
            loaded_scaler = pkl.load(open('data/fitted_scalers/' + str(Location) + '.pkl', 'rb'))
            feature_names = loaded_model.feature_names_in_
            scale_feats = loaded_scaler.feature_names_in_
            # Compare model feature names and scraped feature names. Drop in scraped data the differences
            for element in df.columns:
                if element not in feature_names:
                    df.drop(element, axis = 1, inplace = True)
            # If a column is still NaN or if dataframe is completly empty, throw error:
            if df.isna().sum().sum() > 0 or df.empty:
                st.write('There is some data missing in the scraped data! Try again later.')
                sys.exit()
            st.write('Converted data')
            st.write(df)
        with st.spinner('Scaling data'):
            time.sleep(1)
            #loaded_model = pickle.load(open('./Models/' + str(Location) + '.pkl', 'rb'))
            #loaded_scaler = pickle.load(open('./Models/' + str(Location) + '_scaler.pkl', 'rb'))
            df[scale_feats] = loaded_scaler.transform(df[scale_feats])
            st.write('Scaled data')
            st.write(df)
        with st.spinner('Prediction'):

            y_pred = loaded_model.predict(df)
            y_pred_proba = loaded_model.predict_proba(df)
            if y_pred == 0: 
                st.write('Most likely it will stay dry tomorrow according to the model.')
                st.write('Predicted probability for this predication according to the model is: ' + str(round(y_pred_proba[0][0] * 100, 2)) + '%')
            else: 
                st.write('Most likely it will rain tomorrow according to the model.')
                st.write('Predicted probability for this predication according to the model is: ' + str(round(y_pred_proba[0][1] * 100, 2)) + '%')
        with st.spinner('Interpretibility'):
            time.sleep(1)
            st.write(loaded_model.estimator_)
            explainer = shap.TreeExplainer(loaded_model)
            shap_values = explainer.shap_values(df)
            shap.initjs()
            df1 = df.round(2)
            shap.force_plot(explainer.expected_value[int(y_pred)], shap_values[int(y_pred)], df1, show = False, matplotlib = True)
            plt.savefig('data/images/Forceplot.png')
            st.write('Feature interpretation by SHAP:')
            st.image('data/images/Forceplot.png', width = 1000)


