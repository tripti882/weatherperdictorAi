
import pandas as pd
import requests  # Don't forget to import the requests library
from datetime import datetime

# Your WeatherStack API key
api_key = '60c231831ab060390b179ea241ff79d1'  # Replace with your WeatherStack API key
city = 'dharwad'  # Example city
url =  f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


# Fetch data from the API
response = requests.get(url)

# Check if the request was successfulbase_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Print the entire response to check its structure
    print(data)
    
    # Check if 'wind_speed' exists in the response
    if 'current' in data and 'wind_speed' in data['current']:
        weather_data = {
            'city': city,
            'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'temperature': data['current']['temperature'],
            'humidity': data['current']['humidity'],
            'pressure': data['current']['pressure'],
            'weather_description': data['current']['weather_descriptions'][0],
            'windspeed': data['current']['wind_speed'],  # Correct key for wind speed
            'precipitation': data['current']['precip']   # Correct key for precipitation
        }
    else:
        # Handle case where wind_speed or precip is missing
        weather_data = {
            'city': city,
            'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'temperature': data['current']['temperature'],
            'humidity': data['current']['humidity'],
            'pressure': data['current']['pressure'],
            'weather_description': data['current']['weather_descriptions'][0],
            'windspeed': 'N/A',  # Handle missing wind speed
            'precipitation': 'N/A'  # Handle missing precipitation
        }

    # Convert to DataFrame for further processing
    df = pd.DataFrame([weather_data])

    # Show the DataFrame
    print(df)

else:
    print(f"Error fetching data: {response.status_code}")
