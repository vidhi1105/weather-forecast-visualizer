# === Import Libraries ===
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# === Configuration ===
API_KEY = "b6260d8f86466dad47bcf74e75fade2d"  # Replace with your OpenWeatherMap API key

# Ask user to input city
CITY = input("Enter the city name: ").strip()
UNITS = "metric"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&units={UNITS}&appid={API_KEY}"

# === Create Folder for Graphs ===
os.makedirs("real_graphs", exist_ok=True)

# === Fetch Weather Data ===
response = requests.get(URL)

# === Handle Common Errors ===
if response.status_code == 401:
    print("❌ ERROR 401: Unauthorized – Invalid API key.")
    exit()
elif response.status_code == 404:
    print("❌ ERROR 404: City not found. Please check the city name.")
    exit()
elif response.status_code != 200:
    print(f"❌ ERROR {response.status_code}: Failed to retrieve data.")
    exit()

# === Parse Weather Data ===
data = response.json()
timestamps = []
temperatures = []
humidity = []
wind_speeds = []
descriptions = []

for entry in data['list'][:10]:  # ~Next 30 hours (10 readings)
    dt = datetime.fromtimestamp(entry['dt'])
    temp = entry['main']['temp']
    hum = entry['main']['humidity']
    wind = entry['wind']['speed']
    desc = entry['weather'][0]['description'].capitalize()

    timestamps.append(dt)
    temperatures.append(temp)
    humidity.append(hum)
    wind_speeds.append(wind)
    descriptions.append(desc)

# === Create DataFrame ===
df = pd.DataFrame({
    "Datetime": timestamps,
    "Temperature": temperatures,
    "Humidity": humidity,
    "Wind Speed": wind_speeds,
    "Description": descriptions
})

# === Set Seaborn Style ===
sns.set(style='whitegrid', font_scale=1.1)

# 🌡️ Temperature Plot with Condition Labels
plt.figure(figsize=(12, 5))
sns.lineplot(x="Datetime", y="Temperature", data=df, marker='o', color='tomato')
for i, txt in enumerate(df["Description"]):
    plt.text(df["Datetime"][i], df["Temperature"][i] + 0.5, txt, fontsize=9, ha='center', rotation=30)
plt.title(f"🌡️ Temperature Forecast with Conditions - {CITY}")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("real_graphs/temperature_conditions.png")
plt.close()

# 💧 Humidity Bar Plot
plt.figure(figsize=(12, 5))
sns.barplot(x=df["Datetime"].dt.strftime("%a %H:%M"), y=df["Humidity"], color='skyblue')
plt.title(f"💧 Humidity Forecast - {CITY}")
plt.xlabel("Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("real_graphs/humidity.png")
plt.close()

# 🍃 Wind Speed Plot
plt.figure(figsize=(12, 5))
sns.lineplot(x="Datetime", y="Wind Speed", data=df, marker='s', color='seagreen')
plt.title(f"🍃 Wind Speed Forecast - {CITY}")
plt.xlabel("Time")
plt.ylabel("Wind Speed (m/s)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("real_graphs/wind_speed.png")
plt.close()

print("✅ Forecast complete! Graphs saved in the 'real_graphs/' folder.")
