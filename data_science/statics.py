import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

cities = {
    "New York": "https://weather.com/weather/today/l/USNY0996:1:US",
    "London": "https://weather.com/weather/today/l/UKXX0085:1:UK",
    "Tokyo": "https://weather.com/weather/today/l/JAXX0085:1:JA",
    "Sydney": "https://weather.com/weather/today/l/ASXX0112:1:AS",
    "Paris": "https://weather.com/weather/today/l/FRXX0076:1:FR",
    "Moscow": "https://weather.com/weather/today/l/RUXX0063:1:RU",
    "Beijing": "https://weather.com/weather/today/l/CHXX0008:1:CH",
    "Cairo": "https://weather.com/weather/today/l/EGR000010:1:EG",
    "São Paulo": "https://weather.com/weather/today/l/BRXX0232:1:BR",
    "Mumbai": "https://weather.com/weather/today/l/INXX0096:1:IN"
}

weather_data = []

for city, url in cities.items():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        temp = soup.find("span", class_="CurrentConditions--tempValue--MHmYY").text
        humidity = soup.find("div", class_="WeatherDetailsListItem--wxData--kK35q").text
        weather = soup.find("div", class_="CurrentConditions--phraseValue--mZC_p").text

        weather_data.append([city, temp, humidity, weather])
    
    except AttributeError:
        print(f"Could not retrieve data for {city}. Please check the HTML structure.")

# 데이터프레임 생성
df = pd.DataFrame(weather_data, columns=["City", "Temperature (C)", "Humidity (%)", "Weather Description"])

# CSV 파일로 저장
df.to_csv("world_weather_today.csv", index=False)

print("CSV 파일로 저장이 완료되었습니다.")