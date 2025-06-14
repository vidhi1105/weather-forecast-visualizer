# 🌦️ Weather Forecast Visualization using OpenWeatherMap API

## 📌 Project Overview

This project visualizes **5-day weather forecasts** for a selected city using the **OpenWeatherMap API**. The forecasts are plotted with **Matplotlib** and **Seaborn** to display:

* 🌡️ Temperature trends
* 💧 Humidity variation
* 🔥 Temperature variation heatmap
* 📅 Real-time timestamps and formatting for better analysis

---

## 🚀 Google Colab Notebook

▶️ **Run the project here:**
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1aTmwLJYhG5s1NLJ9c0Sh0oh790V-3sp-?usp=sharing)

---

## 📂 Features

* ✅ Fetches real-time forecast data using API
* ✅ Line plots for temperature trends
* ✅ Bar plots for humidity
* ✅ Heatmap of temperature variation (hourly)
* ✅ PDF report generation of the graphs
* ✅ Clean and easy-to-understand visualization with legends, grid lines, and axis labels

---

## 🏗️ Technologies Used

| Technology     | Purpose                               |
| -------------- | ------------------------------------- |
| **Python 3.x** | Programming language                  |
| `requests`     | For accessing the OpenWeatherMap API  |
| `matplotlib`   | For data visualization (graphs)       |
| `seaborn`      | For enhanced visual styling of graphs |
| `fpdf`         | For generating PDF reports of graphs  |
| `pandas`       | Data manipulation for analysis        |

---

## 🛠️ Installation Instructions

To run the project locally:

```bash
pip install requests matplotlib seaborn pandas fpdf
```

---

## ⚙️ Configuration

1️⃣ Get your **API key** from [OpenWeatherMap](https://openweathermap.org/api)
2️⃣ In the code, replace:

```python
API_KEY = 'YOUR_API_KEY_HERE'
CITY = 'YourCityName'
```

Example:

```python
API_KEY = 'abcd1234yourapikey'
CITY = 'Mumbai'
```

---

## 📊 Graphs Included

| Graph Type               | Description                                    |
| ------------------------ | ---------------------------------------------- |
| 📈 **Temperature Plot**  | Temperature variation over next 5 days         |
| 📊 **Humidity Bar Plot** | Humidity percentages across forecast intervals |
| 🔥 **Heatmap**           | Hourly temperature variation for easy analysis |

---

## 📄 Output PDF Report

✔️ Generates a **PDF report** containing:

* Graph images
* Summary of forecasts
* Statistics (e.g., average temperature)

---

## 🔑 API Source

* [OpenWeatherMap API Documentation](https://openweathermap.org/forecast5)

---

## 📜 License

MIT License © 2025

---

## 🤝 Contributors

Developed by:Vidhi Krishna Mandhana

My Github url:https://github.com/vidhi1105

My Linkedin url:www.linkedin.com/in/
vidhi-mandhana-64a6a5288







