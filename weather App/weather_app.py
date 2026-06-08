import requests
from datetime import datetime

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            print("\nError:", data.get("message"))
            return

        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"]

        print("\n" + "=" * 40)
        print("WEATHER REPORT")
        print("=" * 40)
        print(f"Location      : {city_name}, {country}")
        print(f"Date & Time   : {datetime.now()}")
        print(f"Temperature   : {temperature} °C")
        print(f"Humidity      : {humidity}%")
        print(f"Pressure      : {pressure} hPa")
        print(f"Wind Speed    : {wind_speed} m/s")
        print(f"Condition     : {description.title()}")
        print("=" * 40)

    except requests.exceptions.RequestException:
        print("Network Error. Please check your internet connection.")


def main():
    print("===== Weather App =====")

    while True:
        city = input("\nEnter City Name: ")

        if city.strip():
            get_weather(city)

        choice = input("\nSearch another city? (y/n): ").lower()

        if choice != "y":
            print("\nThank you for using Weather App!")
            break


if __name__ == "__main__":
    main()