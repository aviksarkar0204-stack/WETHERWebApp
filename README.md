# Weather WebApp

A real-time weather web application built with Python (Flask) and OpenWeatherMap API.  
Simply **enter any city name** — Weather WebApp will show live temperature, humidity, AQI, sunrise/sunset, and much more!

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0.0-black?style=flat-square&logo=flask)
![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap-API-orange?style=flat-square)

[![Live Demo](https://img.shields.io/badge/🌤️%20Live%20Demo-HuggingFace-FFD21E?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/Avik128/WETHERWebApp)

---

## 📸 Demo

> Type any city name → Weather WebApp fetches and displays live weather data instantly.

---

## ✨ Features

- 🔍 **City Search** — Search weather for any city in the world
- 🌡️ **Temperature & Feels Like** — Current temp and perceived temperature in °C
- 🌧️ **Chance of Rain** — Precipitation probability from forecast data
- 💧 **Humidity** — Real-time humidity percentage
- 🌫️ **Air Quality Index (AQI)** — Color-coded AQI with levels (Good to Very Poor)
- 🌅 **Sunrise & Sunset** — Local sunrise and sunset time
- 🕐 **Local Time** — Displays the current local time of the searched city
- 😊 **Weather Emojis** — Dynamic emojis based on weather conditions
- 📱 **Responsive Design** — Works on mobile, tablet, and desktop

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Flask | Web framework (backend) |
| HTML/CSS | Frontend UI |
| JavaScript | Async API calls & dynamic rendering |
| OpenWeatherMap API | Live weather, forecast & AQI data |
| Gunicorn | Production WSGI server |
| Docker | Containerization |
| Hugging Face Spaces | Cloud deployment platform |

---

## 📁 Project Structure
```
WETHERWebApp/
│
├── app.py                  # Flask backend — routes & API logic
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── README.md               # Project documentation
│
├── templates/
│   └── index.html          # Frontend HTML + JavaScript
│
└── static/
    └── css/
        └── style.css       # Styling & responsive design
```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/aviksarkar0204-stack/WETHERWebApp.git
cd WETHERWebApp
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your API Key
In `app.py`, replace the API key with your own from [OpenWeatherMap](https://openweathermap.org/api):
```python
API_KEY = "your_api_key_here"
```

---

## ▶️ How to Run
```bash
python app.py
```

Then open your browser and go to:
```
http://127.0.0.1:7860
```

---

## 🕹️ How to Use

1. Run the app and open it in your browser
2. **Type a city name** in the search box (e.g., London, Tokyo, New York)
3. Click **"Get Weather"** or press **Enter**
4. Weather WebApp will display:
   - Temperature & weather description
   - Humidity, Feels Like, Chance of Rain
   - AQI with color coding
   - Sunrise, Sunset & Local Time

---

## 🌈 AQI Color Guide

| Level | Label | Color |
|-------|-------|-------|
| 1 | Good | 🟢 Green |
| 2 | Fair | 🟡 Yellow |
| 3 | Moderate | 🟠 Orange |
| 4 | Poor | 🔴 Red |
| 5 | Very Poor | 🟣 Purple |

---

## ☁️ Weather Emoji Guide

| Condition | Emoji |
|-----------|-------|
| Thunderstorm | ⛈️ |
| Drizzle | 🌦️ |
| Rain | 🌧️ |
| Snow | ☃️ |
| Fog/Mist | 🌫️ |
| Clear Sky | ☀️ |
| Cloudy | ⛅ |
| Tornado | 🌪️ |

---

## 📋 Requirements
```
flask
requests
gunicorn
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Avik Sarkar**  
GitHub: [@aviksarkar0204-stack](https://github.com/aviksarkar0204-stack)
