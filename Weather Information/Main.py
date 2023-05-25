import requests

def get_weather(city):
    api_key = "1cf7847e2378fab42d6778a04c7ba380"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main_data = data["main"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        pressure = main_data["pressure"]
        weather_info = data["weather"][0]
        description = weather_info["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Description: {description}")
    else:
        print("City not found.")


city_name = input("Enter city name: ")
get_weather(city_name)
