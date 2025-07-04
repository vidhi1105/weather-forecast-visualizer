# 🌦️ Weather Forecast Visualizer - Python (VS Code Project)

A Python-based real-time **Weather Forecast Visualizer** that fetches 5-day weather forecast data using the OpenWeatherMap API and creates clean, visually appealing graphs using **Matplotlib** and **Seaborn**. Designed for students, interns, data learners, and those looking to practice API integration, data handling, and visualization using Python.

---

## 🧠 Project Objective

The main goal of this project is to demonstrate the ability to:
- Connect and retrieve real-time data from an external API.
- Analyze and clean the data using **Pandas**.
- Create understandable graphs using **Matplotlib** and **Seaborn**.
- Organize the output clearly and professionally.
- Present a local weather forecasting system (like a mini weather app).

---

## 📌 Key Features

✔️ Real-time city input  
✔️ 30-hour weather forecast using OpenWeatherMap API  
✔️ Clean timestamp formatting: `"Thu 04 Jul, 03:00 PM"`  
✔️ Graphs generated:
- 🌡️ Temperature (°C)
- 💧 Humidity (%)
- 🍃 Wind Speed (m/s)

✔️ Graphs saved as `.png` inside a `graphs/` folder  
✔️ Beginner-friendly and well-commented code  
✔️ Ready to run inside **VS Code** or any Python IDE

---

## 📁 Folder Structure

```

weather-forecast-vscode/
├── weather\_forecast.py       # Main Python script
├── requirements.txt          # Required libraries
├── README.md                 # This file
└── graphs/                   # Auto-generated plots
├── temperature.png
├── humidity.png
└── wind\_speed.png

````

---

## ⚙️ How It Works

1. The user is prompted to enter a city name (e.g., `Mumbai`, `London`).
2. The script sends a request to the OpenWeatherMap API.
3. Data for the next ~30 hours is parsed and processed.
4. Using Pandas, the data is structured and cleaned.
5. Three visual graphs are generated and saved:
   - Temperature vs. Time
   - Humidity vs. Time
   - Wind Speed vs. Time

---

## 🛠️ Installation and Setup

### 🧩 1. Clone the Repository

```bash
git clone https://github.com/vidhi1105/weather-forecast-vscode.git
cd weather-forecast-vscode
````

### 📦 2. Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

Then install the libraries:

```bash
pip install -r requirements.txt
```

---

### 🔑 3. Get an API Key

* Visit: [https://openweathermap.org/api](https://openweathermap.org/api)
* Sign up for free
* Copy your API key
* Open `weather_forecast.py` and replace:

```python
API_KEY = "your_openweathermap_api_key"
```

---

## ▶️ Usage

Run the script using Python:

```bash
python weather_forecast.py
```

When prompted:

```
Enter city name: mumbai
```

📊 After execution:

* Graphs will be saved to `graphs/temperature.png`, `humidity.png`, and `wind_speed.png`
* You can open them from VS Code or your file explorer

---

## 📸 Sample Output

![image](https://github.com/user-attachments/assets/84cd3ba0-2ded-48ae-b7a2-9fd8667b17fc)

![image](https://github.com/user-attachments/assets/02ea55a1-ec67-41a9-8e5f-3701c5427844)

![image](https://github.com/user-attachments/assets/873b8a91-9d93-4110-8626-0596288eaabb)




---

## 📜 requirements.txt

```txt
requests
pandas
matplotlib
seaborn
```

Install using:

```bash
pip install -r requirements.txt
```

---

## 🧪 Example Data Structure

The code fetches this structure from the API:

```json
{
  "list": [
    {
      "dt": 1720029600,
      "main": {
        "temp": 30.5,
        "humidity": 65
      },
      "wind": {
        "speed": 3.5
      },
      "weather": [
        {"description": "clear sky"}
      ]
    },
    ...
  ]
}
```

---

## 🎯 Use Case

* 🧑‍💻 Python learners & interns
* 📊 Data analysis practice
* 🌍 Real-time API integration
* 📋 Mini project for portfolio

---

## 💡 Ideas for Improvement

* Add weather icons (☁️ 🌧️ 🌞)
* Generate automatic PDF report
* Add GUI using Tkinter or Streamlit
* Deploy it as a web app

---

## 👨‍💻 Author

**Vidhi Krishna Mandhana**
Internship Project — Elite Intern, July 2025
Created using Python, VS Code, OpenWeatherMap API

---

## ⚖️ License

This project is licensed under the [MIT License](LICENSE).
Feel free to fork, clone, and improve it.

---

## 🔗 Related Projects

* [Student Marks Report PDF Generator](https://github.com/vidhi1105/student-marks-report-pdf)
* [Spam Detection ML Model (Coming Soon)]()

````

---

## ✅ What You Should Do Next

1. Save this text as `README.md` inside your project folder.
2. Commit it:

```bash
git add README.md
git commit -m "📝 Add detailed README"
git push origin main
````



