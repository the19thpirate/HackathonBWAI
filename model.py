### DEscription : Creating a FrontEnd GUI for the Supply Chain Model

## importing Libraries

from google.protobuf.symbol_database import Default
import pandas as pd
import streamlit as st
from statsmodels.tsa.arima.model import ARIMA

### Creating Title

st.title('Forecasts for Product Storage Management')
st.subheader('The following forecasts are done for 5 days in the future')

st.write("")

## Creating a Select Box for Choosing Partner 

def arima(df,order):
    ARIMA_model = ARIMA(df['Quantity'].values, order = order).fit()
    ARIMA_predict = ARIMA_model.forecast(5)
    return ARIMA_predict

def arima_request(df,order):
    ARIMA_model = ARIMA(df['OrderTotal'].values, order = order).fit()
    ARIMA_predict = ARIMA_model.forecast(5)
    return ARIMA_predict

st.sidebar.write("For Partner Donations Forecast click on the appropriate button")

if st.sidebar.button('FoodieLand'):
    url_1 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/main/Refrigerated_FoodieLand.csv'
    url_2 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/main/Frozen_FoodieLand.csv'
    url_3 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/main/Shelf_FoodieLand.csv'
    url_4 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/main/Thawed_FoodieLand.csv'
    fl_ref = pd.read_csv(url_1)
    fl_fr = pd.read_csv(url_2)
    fl_sh = pd.read_csv(url_3)
    fl_th = pd.read_csv(url_4)

    list_ = [fl_ref, fl_fr, fl_sh, fl_th]
    order = [(1,1,1), (2,1,0), (0,1,0), (0,1,1)]
    forecasts = {}
    for i in range(len(list_)):
        forecasts[i] = (arima(list_[i], order[i]))

    forecasts = pd.DataFrame(forecasts)
    forecasts.columns = ['Refrigerated', 'Frozen', 'Shelf', 'Thawed']

    st.write('FoodieLand Partner Forecast: ')
    st.dataframe(forecasts)

if st.sidebar.button('GrocerTown'):
    url_1 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/main/gt_ref_110.csv'
    url_2 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/main/gt_fr_210.csv'
    url_3 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/main/gt_sh_010.csv'
    url_4 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/main/gt_th_110.csv'
    gt_ref = pd.read_csv(url_1)
    gt_fr = pd.read_csv(url_2)
    gt_sh = pd.read_csv(url_3)
    gt_th = pd.read_csv(url_4)

    list_ = [gt_ref, gt_fr, gt_sh, gt_th]
    order = [(1,1,0), (2,1,0), (0,1,0), (1,1,0)]
    forecasts = {}
    for i in range(len(list_)):
        forecasts[i] = (arima(list_[i], order[i]))

    forecasts = pd.DataFrame(forecasts)
    forecasts.columns = ['Refrigerated', 'Frozen', 'Shelf', 'Thawed']

    st.write('GrocerTown Partner Forecast: ')
    st.dataframe(forecasts)

if st.sidebar.button('LoMarket'):
    url_1 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/main/lm_ref_111.csv'
    url_2 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/main/lm_fr_110.csv'
    url_3 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/main/lm_sh_010.csv'
    url_4 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/main/lm_th_111.csv'
    lm_ref = pd.read_csv(url_1)
    lm_fr = pd.read_csv(url_2)
    lm_sh = pd.read_csv(url_3)
    lm_th = pd.read_csv(url_4)

    list_ = [lm_ref, lm_fr, lm_sh, lm_th]
    order = [(1,1,1), (1,1,0), (0,1,0), (1,1,1)]
    forecasts = {}
    for i in range(len(list_)):
        forecasts[i] = (arima(list_[i], order[i]))

    forecasts = pd.DataFrame(forecasts)
    forecasts.columns = ['Refrigerated', 'Frozen', 'Shelf', 'Thawed']

    st.write('LoMarket Partner Forecast: ')
    st.dataframe(forecasts)


st.sidebar.write('For Location Based Requests Forecast click on the appropriate button')

if st.sidebar.button('HQ'):
    url_1 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/hq_ref_011.csv'
    url_2 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/hq_fr_011.csv'
    url_3 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/hq_sh_011.csv'
    url_4 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/hq_th_011.csv'
    hq_ref = pd.read_csv(url_1)
    hq_fr = pd.read_csv(url_2)
    hq_sh = pd.read_csv(url_3)
    hq_th = pd.read_csv(url_4)

    list_ = [hq_ref, hq_fr, hq_sh, hq_th]
    order = [(0,1,1), (0,1,1), (0,1,1), (0,1,1)]
    forecasts = {}
    for i in range(len(list_)):
        forecasts[i] = (arima_request(list_[i], order[i]))

    forecasts = pd.DataFrame(forecasts)
    forecasts.columns = ['Refrigerated', 'Frozen', 'Shelf', 'Thawed']

    st.write('HQ Location Requests Forecast: ')
    st.dataframe(forecasts)

if st.sidebar.button('North'):
    url_1 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/nr_ref_012.csv'
    url_2 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/nr_fr_011.csv'
    url_3 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/nr_sh_012.csv'
    url_4 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/nr_th_012.csv'
    nr_ref = pd.read_csv(url_1)
    nr_fr = pd.read_csv(url_2)
    nr_sh = pd.read_csv(url_3)
    nr_th = pd.read_csv(url_4)

    list_ = [nr_ref, nr_fr, nr_sh, nr_th]
    order = [(0,1,2), (0,1,1), (0,1,2), (0,1,2)]
    forecasts = {}
    for i in range(len(list_)):
        forecasts[i] = (arima_request(list_[i], order[i]))

    forecasts = pd.DataFrame(forecasts)
    forecasts.columns = ['Refrigerated', 'Frozen', 'Shelf', 'Thawed']

    st.write('North Location Requests Forecast: ')
    st.dataframe(forecasts)

if st.sidebar.button('South'):
    url_1 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/st_ref_011.csv'
    url_2 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/st_fr_011.csv'
    url_3 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/st_sh_013.csv'
    url_4 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/st_th_110.csv'
    so_ref = pd.read_csv(url_1)
    so_fr = pd.read_csv(url_2)
    so_sh = pd.read_csv(url_3)
    so_th = pd.read_csv(url_4)

    list_ = [so_ref, so_fr, so_sh, so_th]
    order = [(1,1,1), (1,1,0), (0,1,0), (1,1,1)]
    forecasts = {}
    for i in range(len(list_)):
        forecasts[i] = (arima_request(list_[i], order[i]))

    forecasts = pd.DataFrame(forecasts)
    forecasts.columns = ['Refrigerated', 'Frozen', 'Shelf', 'Thawed']

    st.write('South Location Requests Forecast: ')
    st.dataframe(forecasts)

if st.sidebar.button('East'):
    url_1 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/ea_ref_011.csv'
    url_2 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/ea_fr_011.csv'
    url_3 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/ea_sh_011.csv'
    url_4 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/ea_th_110.csv'
    ea_ref = pd.read_csv(url_1)
    ea_fr = pd.read_csv(url_2)
    ea_sh = pd.read_csv(url_3)
    ea_th = pd.read_csv(url_4)

    list_ = [ea_ref, ea_fr, ea_sh, ea_th]
    order = [(0,1,1), (0,1,1), (0,1,1), (1,1,0)]
    forecasts = {}
    for i in range(len(list_)):
        forecasts[i] = (arima_request(list_[i], order[i]))

    forecasts = pd.DataFrame(forecasts)
    forecasts.columns = ['Refrigerated', 'Frozen', 'Shelf', 'Thawed']

    st.write('East Location Requests Forecast: ')
    st.dataframe(forecasts)

if st.sidebar.button('West'):
    url_1 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/we_ref_011.csv'
    url_2 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/we_fr_011.csv'
    url_3 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/we_sh_013.csv'
    url_4 = 'https://raw.githubusercontent.com/the19thpirate/HackathonBWAI/Location/we_th_110.csv'
    we_ref = pd.read_csv(url_1)
    we_fr = pd.read_csv(url_2)
    we_sh = pd.read_csv(url_3)
    we_th = pd.read_csv(url_4)

    list_ = [we_ref, we_fr, we_sh, we_th]
    order = [(1,1,1), (1,1,0), (0,1,0), (1,1,1)]
    forecasts = {}
    for i in range(len(list_)):
        forecasts[i] = (arima_request(list_[i], order[i]))

    forecasts = pd.DataFrame(forecasts)
    forecasts.columns = ['Refrigerated', 'Frozen', 'Shelf', 'Thawed']

    st.write('West Location Requests Forecast: ')
    st.dataframe(forecasts)