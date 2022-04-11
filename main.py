# MarcWeather v0.1
# Settings
import datetime as dt
import requests
# Don't change the 2 settings
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "4e20147622ae055966c79322f8e77263"
# You can modify the string in the variable to your current city (City, Country. Example: Beirut, Lebanon or simply Beirut.)
CITY = "Beirut, Lebanon"
# For the main menu
MainMenu = input(f"""Marc Weather v0.1
 1) Show weather for {CITY}
 2) About...
 3) Exit
 
 Enter a choice: """)
if MainMenu == '1':
    # Connect to the API
    def kelvin_to_celsius_fahrenheit(kelvin):
        celsuis = kelvin - 273.15
        farenheit = celsuis * (9/5) + 32
        return celsuis, farenheit
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url).json()

    temp_kelvin = response['main']['temp']
    temp_celsuis, temp_farenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)


    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsuis, feels_like_farenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

# In line 40 to 46, you can remove the {(weather object)_farenheit:.2f} F to remove the farenheit and vice versa
    print(f"""The city is {CITY}
Temperature: {temp_celsuis:.2f} C or {temp_farenheit:.2F} F
Temperature feels like: {feels_like_celsuis:.2f} C or {feels_like_farenheit:.2F} F
Humidity: {humidity}%
Wind Speed: {wind_speed}km/h
Main Weather: {description}
Sun rises at {sunrise_time} local time.
Sun sets at {sunset_time} local time.""")
elif MainMenu == '2':
    print("""Marc Weather v0.1
    Version 0.1 Initial Release
    Uses weather data from OpenWeather""")
elif MainMenu == '3':
    exit()
# end of MarcWeather
# Info:
# MarcWeather v0.1 Initial Release
