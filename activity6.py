from datetime import datetime
import requests
import pytemperature

now = datetime.now()

print("ISQA 3900 Open Weather API")

print()
global choice
choice = "y"

while choice.lower() == "y":
    city = input("Enter city:     ")
    print("Use ISO letter country code like: https://countrycode.org/")
    country = input("Enter country code:     ")

    api_start = 'https://api.openweathermap.org/data/2.5/weather?q='

    api_key = '&appid=6a4228285f3e094d43acbae0eabced54'

    url = api_start + city + ',' + country + api_key

    json_data = requests.get(url).json()

    try:
        # Weather Description
        weather_description = json_data['weather'][0]['description']
        print("Current conditions:  ", weather_description)

        # Temperature converted to F
        temperature = json_data['main']['temp']
        convertTemp = pytemperature.k2f(temperature)
        print("Current Temperature in Fahrenheit:  ", convertTemp)

        # Pressure in hPa
        pressure = json_data['main']['pressure']
        print("Current Pressure in hPA:  ", pressure)

        # Humidity
        humidity = json_data['main']['humidity']
        castHumidity = str(humidity)
        print("Current Humidity:  " + castHumidity + "%")

        # Low Temperature converted to F
        lowTemperature = json_data['main']['temp_min']
        convertLowTemp = pytemperature.k2f(lowTemperature)
        print("Expected Low Temperature in Fahrenheit:  ", convertLowTemp)

        # High Temperature converted to F
        highTemperature = json_data['main']['temp_max']
        convertHighTemp = pytemperature.k2f(highTemperature)
        print("Expected High Temperature in Fahrenheit:  ", convertHighTemp)
    except KeyError:
        castCity = str(city)
        castCountry = str(country)
        print("Unable to access " + castCity + " in " + castCountry)
        print("Verify city name and country code")

    # Exception Handling for continuing
    cont = 1
    while cont == 1:
        try:
            choice = input(str("Continue (y/n)?: "))
            if (choice.lower() != 'y') and (choice.lower() != 'n'):
                raise ValueError()
        except ValueError:
            print()
            print("You must answer 'y' for Yes or 'n' for No. Please try again.")
            print()
            continue
        else:
            print()
            if choice.lower() == 'y':
                cont = 0
            elif choice.lower() == 'n':
                cont = 0

# Program End, now with excitement
print('Bye!')