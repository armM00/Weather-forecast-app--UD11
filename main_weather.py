import streamlit as st
from plotly import express as px
from backend import get_data

st.title('Weather forecast for the Next days')

place = st.text_input(label="Place", key='user_input').title()
DAYS = st.slider(label='Forecast Days', min_value=1,
                 max_value=5, help='Select the number of forecasted days.')

option = st.selectbox(label='Select the data to view',
                      options=('Temperature', "Sky"))

str_ = ""
str_ = 'day' if DAYS == 1 else "days"

if place:
    try:
        filtered_data = get_data(place, DAYS)
        dates = [my_dict['dt_txt'] for my_dict in filtered_data]

        st.info(f"{option} for the next {DAYS} {str_} in {place}:")

        if option == 'Temperature':
            #  API default is Kelvin
            temperatures_in_kelvin = [my_dict['main']['temp'] for my_dict in filtered_data]
            temps_to_celsius = [i - 273.15 for i in temperatures_in_kelvin]

            figure = px.line(x=dates, y=temps_to_celsius, labels={'x': 'Date', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)

        if option == 'Sky':
            forecast_sky = [my_dict['weather'][0]['main'] for my_dict in filtered_data]

            images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png',
                      'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}

            # as forecast_sky is [ "Clouds", "Clouds", "Clouds", "Clouds", "Clouds", "Clouds", "Rain", "Clouds"]
            # and that we can provide the images in a list.

            # Define the number of columns you want to display
            num_columns = int(len(forecast_sky) / 8)

            # Calculate the number of blocks per column
            num_blocks_per_column = len(forecast_sky) // num_columns

            # Create a layout with multiple columns
            cols = st.columns(num_columns)

            # Iterate over each forecast sky and its corresponding date
            for i, (sky, date) in enumerate(zip(forecast_sky, dates)):
                # Calculate the column index and block index
                col_idx = i % num_columns
                block_idx = i // num_columns

                # Display the image and date in the respective column and block
                with cols[col_idx]:
                    # as forecast_sky is [ "Clouds", "Clouds", "Clouds", "Clouds", "Clouds", "Clouds", "Rain", "Clouds"]
                    # and that we can provide the images in a list.
                    st.image(images[sky], width=115)
                    date_to_display = date
                    st.write(date_to_display)

    except KeyError:
        st.error('City is not found')
