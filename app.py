from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

API_KEY = "7ed7760b26e4db38e7542eb04eaf2bf4"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    try:
        data = request.get_json()
        city = data.get('city', '').strip()
        
        if not city:
            return jsonify({'error': 'Please enter a city name'}), 400
        
        # Get current weather
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        weather_data = response.json()
        
        if weather_data.get("cod") != 200:
            return jsonify({'error': weather_data.get("message", "Unknown error")}), 400
        
        # Extract weather info
        temperature = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        weather_id = weather_data["weather"][0]["id"]
        weather_description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        
        # Sunrise/Sunset
        timezone_offset = weather_data["timezone"]
        sunrise = datetime.utcfromtimestamp(weather_data["sys"]["sunrise"] + timezone_offset).strftime("%H:%M")
        sunset = datetime.utcfromtimestamp(weather_data["sys"]["sunset"] + timezone_offset).strftime("%H:%M")
        
        # Local time
        local_time = datetime.utcnow() + timedelta(seconds=timezone_offset)
        local_time_str = local_time.strftime('%H:%M')
        
        # Coordinates for additional API calls
        lat = weather_data["coord"]["lat"]
        lon = weather_data["coord"]["lon"]
        
        # Get precipitation probability
        precip_prob = None
        try:
            url_forecast = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
            response_f = requests.get(url_forecast, timeout=8)
            response_f.raise_for_status()
            data_f = response_f.json()
            if str(data_f.get("cod")) == "200" and data_f.get("list"):
                pop = data_f["list"][0].get("pop")
                if isinstance(pop, (int, float)):
                    precip_prob = int(pop * 100)
        except:
            pass
        
        # Get AQI
        aqi_level = None
        aqi_text = None
        try:
            url_aqi = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
            response_a = requests.get(url_aqi, timeout=8)
            response_a.raise_for_status()
            data_a = response_a.json()
            aqi = data_a["list"][0]["main"]["aqi"]
            
            aqi_levels = {1: "Good", 2: "Fair", 3: "Moderate", 4: "Poor", 5: "Very Poor"}
            aqi_level = aqi
            aqi_text = aqi_levels.get(aqi, str(aqi))
        except:
            pass
        
        # Get weather emoji
        emoji = get_weather_emoji(weather_id)
        
        result = {
            'temperature': round(temperature),
            'feels_like': round(feels_like),
            'description': weather_description.capitalize(),
            'humidity': humidity,
            'sunrise': sunrise,
            'sunset': sunset,
            'local_time': local_time_str,
            'precip_prob': precip_prob,
            'aqi_level': aqi_level,
            'aqi_text': aqi_text,
            'emoji': emoji,
            'city': weather_data["name"],
            'country': weather_data["sys"]["country"]
        }
        
        return jsonify(result)
    
    except requests.exceptions.HTTPError as http_error:
        status = http_error.response.status_code if http_error.response is not None else None
        if status == 404:
            return jsonify({'error': 'City not found'}), 404
        elif status == 401:
            return jsonify({'error': 'Invalid API key'}), 401
        else:
            return jsonify({'error': f'HTTP error {status}'}), status
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Connection error. Check your internet connection'}), 500
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Request timed out'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_weather_emoji(weather_id):
    if 200 <= weather_id <= 232:
        return "⛈️"
    elif 300 <= weather_id <= 321:
        return "🌦️"
    elif 500 <= weather_id <= 531:
        return "🌧️"
    elif 600 <= weather_id <= 622:
        return "☃️"
    elif 701 <= weather_id <= 781:
        return "🌫️"
    elif weather_id == 762:
        return "🌋"
    elif weather_id == 771:
        return "💨"
    elif weather_id == 781:
        return "🌪️"
    elif weather_id == 800:
        return "☀️"
    elif 801 <= weather_id <= 804:
        return "⛅"
    else:
        return ""

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7860)
