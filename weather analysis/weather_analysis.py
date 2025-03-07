import matplotlib
matplotlib.use('Agg')  # Use a backend that does not require Tkinter

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import random
from datetime import datetime, timedelta

# 🔹 Step 1: Generate a dataset if it does not exist
csv_file = "weather_data.csv"

if not os.path.exists(csv_file):
    print(" Generating dataset...")

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

    # Create DataFrame
    df = pd.DataFrame(weather_data, columns=["Date", "City", "Temperature", "Humidity", "WindSpeed"])

    # Save to CSV file
    df.to_csv(csv_file, index=False)
    print(f" Dataset '{csv_file}' created successfully!\n")
else:
    print(f" Using existing dataset: {csv_file}\n")

# 🔹 Step 2: Load the dataset
data = pd.read_csv(csv_file)

# Convert 'Date' to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Set index
data.set_index('Date', inplace=True)

# 🔹 Step 3: Resample and calculate averages
daily_avg_temp = data.groupby(data.index)['Temperature'].mean()
weekly_avg_temp = data['Temperature'].resample('W').mean()
monthly_avg_temp = data['Temperature'].resample('ME').mean()  # FIXED! ('M' → 'ME')

# 🔹 Step 4: Calculate statistical metrics
min_temp = np.min(data['Temperature'])
max_temp = np.max(data['Temperature'])
std_temp = np.std(data['Temperature'])

# Print statistics
print(f" Min Temperature: {min_temp}°C")
print(f" Max Temperature: {max_temp}°C")
print(f" Standard Deviation of Temperature: {std_temp}°C\n")

# 🔹 Step 5: Plot and save instead of showing
output_folder = "plots"
os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist

#  Daily Temperature Trend
plt.figure(figsize=(10, 6))
plt.plot(daily_avg_temp, label='Daily Avg Temp', color='blue')
plt.title('Daily Average Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.savefig(f"{output_folder}/daily_temperature.png")  # Save plot
plt.close()  # Close figure

# Weekly Temperature Trend
plt.figure(figsize=(10, 6))
plt.plot(weekly_avg_temp, label='Weekly Avg Temp', color='green')
plt.title('Weekly Average Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.savefig(f"{output_folder}/weekly_temperature.png")
plt.close()

#  Monthly Temperature Trend
plt.figure(figsize=(10, 6))
plt.plot(monthly_avg_temp, label='Monthly Avg Temp', color='red')
plt.title('Monthly Average Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.savefig(f"{output_folder}/monthly_temperature.png")
plt.close()

# 🔹 Step 6: Compare weather patterns between cities
new_york_data = data[data['City'] == 'New York']
chicago_data = data[data['City'] == 'Chicago']

# Calculate the daily average temperature for each city
new_york_avg_temp = new_york_data['Temperature'].resample('D').mean()
chicago_avg_temp = chicago_data['Temperature'].resample('D').mean()

#  Temperature Comparison Plot
plt.figure(figsize=(10, 6))
plt.plot(new_york_avg_temp, label='New York', color='blue')
plt.plot(chicago_avg_temp, label='Chicago', color='red')
plt.title('Temperature Comparison: New York vs Chicago')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.savefig(f"{output_folder}/city_comparison.png")  # Save comparison plot
plt.close()

print(f" All plots saved successfully in '{output_folder}' folder!")
