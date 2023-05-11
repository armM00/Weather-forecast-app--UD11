# Weather Forecast Web App
[![Project Header](https://i.ibb.co/N9fT7BN/cover.jpg)](#)

This is a web application built with Streamlit that provides weather forecasts for the next few days. It utilizes the OpenWeatherMap API to retrieve weather data and displays it in a user-friendly interface.

## Features

- Input a location to get weather forecasts
- Select the number of forecasted days
- Choose between viewing temperature or sky conditions
- Displays temperature as a line chart and sky conditions as images
- Error handling for invalid or missing locations

## Installation

1. Clone the repository:

```shell
git clone https://github.com/armM00/Weather-forecast-app.git
```

2. Install the dependencies:
```pip install -r requirements.txt```

3. Create an api.json file in the project directory and add your OpenWeatherMap API key in the following format:
`{
  "openweathermap": "YOUR_API_KEY"
}`
 Replace "YOUR_API_KEY" with your actual API key.

## Usage
1. Run the app:

`streamlit run app.py`
2. Access the app in your web browser at http://localhost:8501.

3. Enter a location, select the forecast days, and choose the data to view.

## Contributing
Contributions are welcome! If you find any issues or want to enhance the app, feel free to submit a pull request.

## License
This project is licensed under the MIT License.

## Contributing

Feel free to adjust any specific details in the content to match your project's require



