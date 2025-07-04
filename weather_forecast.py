# 📦 Required Libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# 📁 Create directory for graphs if it doesn't exist
os.makedirs("graphs", exist_ok=True)

# 🌐 OpenWeatherMap API Setup
API_KEY = "b6260d8f86466dad47bcf74e75fade2d"  # Replace with your actual API key
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

# 🏙️ Ask for city name
CITY = input("Enter city name: ")

# 🔗 Construct the request URL
params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)

# ❌ Handle errors
if response.status_code != 200:
    print("Failed to retrieve data:", response.status_code)
    print("Response:", response.text)
    exit()

# ✅ Process the data
data = response.json()
timestamps = []
temperatures = []
humidity = []
wind_speeds = []
descriptions = []

for entry in data['list'][:10]:  # About 30 hours of forecast
    dt = datetime.fromtimestamp(entry['dt'])
    formatted_time = dt.strftime("%a %d %b, %I:%M %p")
    timestamps.append(formatted_time)
    temperatures.append(entry['main']['temp'])
    humidity.append(entry['main']['humidity'])
    wind_speeds.append(entry['wind']['speed'])
    descriptions.append(entry['weather'][0]['description'].capitalize())

# 📊 Create DataFrame
df = pd.DataFrame({
    "Datetime": timestamps,
    "Temperature": temperatures,
    "Humidity": humidity,
    "Wind Speed": wind_speeds,
    "Description": descriptions
})

# 🎨 Plot Style
sns.set(style='whitegrid')

# 🌡️ Temperature Line Plot
plt.figure(figsize=(12, 5))
sns.lineplot(x=df["Datetime"], y=df["Temperature"], marker='o', color='tomato')
plt.title(f"🌡️ Temperature Forecast - {CITY}")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("graphs/temperature.png")
plt.close()

# 💧 Humidity Bar Plot
plt.figure(figsize=(12, 5))
sns.barplot(x=df["Datetime"], y=df["Humidity"], color='skyblue')
plt.title(f"💧 Humidity Forecast - {CITY}")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("graphs/humidity.png")
plt.close()

# 🍃 Wind Speed Line Plot
plt.figure(figsize=(12, 5))
sns.lineplot(x=df["Datetime"], y=df["Wind Speed"], marker='o', color='green')
plt.title(f"🍃 Wind Speed Forecast - {CITY}")
plt.ylabel("Wind Speed (m/s)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("graphs/wind_speed.png")
plt.close()

print(f"\n✅ Forecast for {CITY} complete!")
print("📁 Graphs saved in the 'graphs' folder.")
