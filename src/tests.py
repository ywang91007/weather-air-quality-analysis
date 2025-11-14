# Test file to check if API is working

import os
import sys
from data_collection import get_weather

sys.path.insert(0, 'src')

# Test with Los Angeles
print("Testing API with Los Angeles...")
print()

# Set API key (need to create a .env file first)
os.environ['OPENWEATHER_API_KEY'] = os.getenv('OPENWEATHER_API_KEY', '')

try:
    result = get_weather('Los Angeles')
    
    print("Success! Here's the data:")
    print(f"City: {result['city']}")
    print(f"Temperature: {result['temperature']}°F")
    print(f"Humidity: {result['humidity']}%")
    print(f"Wind Speed: {result['wind_speed']} mph")
    print(f"Weather: {result['weather']}")
    print()
    print("Test passed! API is working.")
    
except Exception as e:
    print(f"Test failed: {e}")
