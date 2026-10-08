import requests

API_KEY = "----"

GEO_URL = "https://api.openweathermap.org/geo/1.0/direct"
CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


def get_coordinates(city):
    params = {
        "q": city,
        "limit": 1,
        "appid": API_KEY
    }

    response = requests.get(GEO_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if not data:
        return None

    return {
        "name": data[0]["name"],
        "country": data[0].get("country", ""),
        "lat": data[0]["lat"],
        "lon": data[0]["lon"]
    }


def get_current_weather(lat, lon):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(CURRENT_URL, params=params, timeout=10)
    response.raise_for_status()

    return response.json()


def get_forecast(lat, lon):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(FORECAST_URL, params=params, timeout=10)
    response.raise_for_status()

    return response.json()


def display_current_weather(location, weather):
    print("\n" + "=" * 45)
    print("          CURRENT WEATHER")
    print("=" * 45)

    temperature = weather["main"]["temp"]
    feels_like = weather["main"]["feels_like"]
    humidity = weather["main"]["humidity"]
    pressure = weather["main"]["pressure"]
    description = weather["weather"][0]["description"].title()
    wind_speed = weather["wind"]["speed"]

    print(f"City        : {location['name']}")
    print(f"Country     : {location['country']}")
    print(f"Weather     : {description}")
    print(f"Temperature : {temperature:.1f} °C")
    print(f"Feels Like  : {feels_like:.1f} °C")
    print(f"Humidity    : {humidity}%")
    print(f"Pressure    : {pressure} hPa")
    print(f"Wind Speed  : {wind_speed} m/s")


def display_forecast(forecast):
    print("\n" + "=" * 45)
    print("            WEATHER FORECAST")
    print("=" * 45)

    # Show next 8 forecast entries
    # 8 entries × 3 hours = next 24 hours

    for item in forecast["list"][:8]:
        date_time = item["dt_txt"]

        temperature = item["main"]["temp"]
        humidity = item["main"]["humidity"]
        description = item["weather"][0]["description"].title()

        print(f"\nDate & Time : {date_time}")
        print(f"Temperature : {temperature:.1f} °C")
        print(f"Humidity    : {humidity}%")
        print(f"Weather     : {description}")
        print("-" * 45)


def weather_app():
    print("=" * 45)
    print("        LIVE OPENWEATHER APP")
    print("=" * 45)

    if API_KEY == "YOUR_API_KEY_HERE":
        print("\nERROR: Add your OpenWeather API key first.")
        print('Replace: API_KEY = "YOUR_API_KEY_HERE"')
        return

    while True:

        city = input(
            "\nEnter city name or type 'exit': "
        ).strip()

        if city.lower() == "exit":
            print("\nThank you for using Weather App!")
            break

        if not city:
            print("Please enter a city name.")
            continue

        try:
            print("\nFetching live weather data...")

            location = get_coordinates(city)

            if location is None:
                print("City not found. Try again.")
                continue

            weather = get_current_weather(
                location["lat"],
                location["lon"]
            )

            forecast = get_forecast(
                location["lat"],
                location["lon"]
            )

            display_current_weather(
                location,
                weather
            )

            display_forecast(forecast)

        except requests.exceptions.ConnectionError:
            print("No internet connection.")

        except requests.exceptions.Timeout:
            print("Request timed out. Try again.")

        except requests.exceptions.HTTPError as error:

            if error.response.status_code == 401:
                print("Invalid API key.")

            else:
                print(
                    "HTTP Error:",
                    error.response.status_code
                )

        except requests.exceptions.RequestException as error:
            print("API Request Error:", error)

        except Exception as error:
            print("Unexpected Error:", error)


if __name__ == "__main__":
    weather_app()