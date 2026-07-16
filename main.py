import requests

url = "https://api.weatherapi.com/v1/current.json"

city = input("Enter the city name: ")


params = {
    "q": city,
    "key": "<Your Key>"
}
response = requests.get(url,params=params)

data = response.json()

print(response.status_code)

print("\n=====================================================")
print("                  Weather Dashboard")
print("=====================================================")
print("\n📍 city:",data["location"]["name"])
print("🌐 region:", data["location"]["region"])
print("🌎 country:", data["location"]["country"])
print("🌡  temp:",data["current"]["temp_c"])
print("💨 wind speed(in KM):",data["current"]["wind_kph"])
print("💨 Wind Speed(in MPH):",data["current"]["wind_mph"])
print("💨 wind direction:",data["current"]["wind_dir"])
print("🍃 pressure:",data["current"]["pressure_mb"])
print("💧 humidity:",data["current"]["humidity"])
print("🌧️ Chance of rain:",data["current"]["chance_of_rain"])
print("⌛ Last Updated:",data["current"]["last_updated"])
print("🕝 Current Time:",data["location"]["localtime"])

print("\n=====================================================")

print(response.url)