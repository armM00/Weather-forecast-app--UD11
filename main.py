import streamlit as st
from plotly import express as px


st.title('Weather forecast for the Next days')

place = st.text_input(label="Place", key='user_input')
DAYS = st.slider(label='Forecast Days', min_value=1,
                 max_value=5, help='Select the number of forecasted days.')

option = st.selectbox(label='Select the data to view',
                      options=("Weather", "Sky"))

str_ = ""
str_ = 'day' if DAYS == 1 else "days"

if len(place) != 0:
    st.subheader(f"{option} for the next {DAYS} {str_} in {place}:")


    def get_data(days=DAYS):
        dates = ['2022-25-10', '2022-26-10', '2022-27-10']
        temperatures = [10, 11, 15]
        if days == 1:
            return dates, temperatures
        else:
            return dates[0:days], temperatures[0:days]


    d, t, = get_data()
    figure = px.line(x=d, y=t, labels={'x': 'Date', 'y': 'Temperature (C)'})

    st.plotly_chart(figure)
