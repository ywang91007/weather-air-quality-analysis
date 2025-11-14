# Weather Data Collection Script
# This script gets weather data from OpenWeatherMap API

import requests
import json
import os

# Get API key from environment variable
api_key = os.getenv('OPENWEATHER_API_KEY')

def get_weather(city):
    """Get weather data for one city"""
    
    # API endpoint
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        'q': city,
        'appid': api_key,
        'units': 'imperial'
    }
    
    # Make API request
    response = requests.get(url, params=params)
    data = response.json()
    
    # Get the data we need
    weather_info = {
        'city': city,
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'weather': data['weather'][0]['main']
    }
    
    return weather_info


# List of cities to get weather for
cities = ['Los Angeles', 'New York', 'Chicago']

# Get weather data for each city
all_weather = []
for city in cities:
    print(f"Getting weather for {city}...")
    weather = get_weather(city)
    all_weather.append(weather)
    print(f"  Temperature: {weather['temperature']}°F")
    print(f"  Humidity: {weather['humidity']}%")
    print()

# Save to JSON file
with open('data/weather_data.json', 'w') as f:
    json.dump(all_weather, f, indent=2)

print("Data saved to data/weather_data.json")
