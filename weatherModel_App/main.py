import requests
from flask import Flask, render_template, request
import speech_recognition as sr
import pyttsx3
import threading
import time

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

location_info = {"city": "YourCity", "country": "YourCountry", "latitude": "0.0", "longitude": "0.0"}

def get_weather():
    global location_info
    while True:
        try:
            complete_api_link = BASE_URL + "q=" + location_info["city"] + "&appid=" + API_KEY
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()

            if api_data["cod"] == "404":
                print("Invalid city: {}, please enter a valid city.".format(location_info["city"]))
            else:
                main = api_data["main"]
                wind = api_data["wind"]
                weather_desc = api_data["weather"][0]["description"]

                temp = round(main["temp"] - 273.15, 2)
                humidity = main["humidity"]
                wind_speed = wind["speed"]

                weather_info = {
                    "temperature": temp,
                    "humidity": humidity,
                    "wind_speed": wind_speed,
                    "weather_desc": weather_desc,
                }

                print("Weather updated:")
                print("Temperature: {}°C".format(weather_info["temperature"]))
                print("Humidity: {}%".format(weather_info["humidity"]))
                print("Wind Speed: {} m/s".format(weather_info["wind_speed"]))
                print("Description: {}".format(weather_info["weather_desc"]))

                # Wait for 1 hour before updating again
                time.sleep(3600)

        except Exception as e:
            print("An error occurred while fetching weather data:", e)

# Start a separate thread for weather updates
weather_thread = threading.Thread(target=get_weather)
weather_thread.start()

# Voice Assistant
def voice_assistant():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for voice commands...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5)

                command = recognizer.recognize_google(audio).lower()

                if "change location" in command:
                    print("Please enter a new city:")
                    new_city = input()
                    location_info["city"] = new_city
                    print("Location changed to:", new_city)

                elif "exit" in command:
                    print("Exiting the voice assistant.")
                    break

        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print("An error occurred while processing the voice command:", e)

# Start a separate thread for the voice assistant
voice_thread = threading.Thread(target=voice_assistant)
voice_thread.start()

# Flask Web App
@app.route("/")
def home():
    global location_info
    return render_template("index.html", location=location_info)

if __name__ == "__main__":
    app.run(debug=True)
