# Weather and Air Quality Analysis Project

## What This Project Does
This project collects weather data from different U.S. cities and will analyze how weather affects air quality.

## Files in This Project
- `src/data_collection.py` - Gets weather data from OpenWeatherMap API
- `tests.py` - Tests if the API is working
- `requirements.txt` - List of Python packages needed
- `.gitignore` - Tells git what files to ignore
- `README.md` - This file

## How to Set Up

### Step 1: Get an API Key
1. Go to https://openweathermap.org/api
2. Click "Sign Up" and create a free account
3. After signing in, go to "API keys"
4. Copy your API key

### Step 2: Create .env File
Create a new file called `.env` in the project folder and put this in it:
```
OPENWEATHER_API_KEY=your_api_key
```
(Replace `your_api_key` with your actual API key)

### Step 3: Install Required Packages
Open terminal/command prompt and type:
```
pip install -r requirements.txt
```

## How to Run

### Test if it works:
```
python tests.py
```

### Collect weather data:
```
python src/data_collection.py
```

This will create a file `data/weather_data.json` with weather information.

## What I've Done So Far
- ✅ Set up project structure
- ✅ Connected to OpenWeatherMap API
- ✅ Can get weather data for multiple cities
- ⏳ Still need to get air quality data
- ⏳ Still need to analyze the data

## Data Sources
1. **OpenWeatherMap API** - Current weather data
2. **EPA Air Quality Data** - Air quality information (coming next)

## Important Notes
- The `data/` folder is not uploaded to GitHub (it's in .gitignore)
