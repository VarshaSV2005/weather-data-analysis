import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Generate dates for one month
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 1, 31)
dates = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]

# Cities to include in the dataset
cities = ["New York", "Chicago"]

# List to store generated data
weather_data = []

# Generate random weather data
for date in dates:
    for city in cities:
        temperature = round(random.uniform(10, 30), 1)  # Temperature between 10°C and 30°C
        humidity = random.randint(50, 90)  # Humidity between 50% and 90%
        wind_speed = round(random.uniform(5, 25), 1)  # Wind speed between 5 and 25 km/h
        
        weather_data.append([date.strftime('%Y-%m-%d'), city, temperature, humidity, wind_speed])

# Create a DataFrame
df = pd.DataFrame(weather_data, columns=["Date", "City", "Temperature", "Humidity", "WindSpeed"])

# Save to CSV file
df.to_csv("weather_data.csv", index=False)

print("Dataset 'weather_data.csv' has been created successfully!")
print(df.head())  # Show the first few rows
