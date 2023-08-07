import requests
import datetime

def get_weather_forecast(city, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt={days}&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8"
    response = requests.get(url)
    data = response.json()

    weather_forecast = []
    for day_data in data['list']:
        date = datetime.datetime.fromtimestamp(day_data['dt']).strftime("%d-%m-%Y")
        temp_day = day_data['temp']['day']
        temp_night = day_data['temp']['night']
        weather_forecast.append((date, temp_day, temp_night))

    return weather_forecast

def save_weather_to_file(city, days, forecast_data):
    filename = f"{datetime.datetime.now().strftime('%d-%m-%Y')}-{city}-{days}-days-weather-forecast.txt"
    with open(filename, 'w') as file:
        file.write("Дата Температура вдень Температура вночі\n")
        for date, temp_day, temp_night in forecast_data:
            file.write(f"{date} {temp_day:.2f} {temp_night:.2f}\n")

def main():
    city = input("Введіть місто: ")
    days = int(input("Введіть кількість днів прогнозу: "))

    forecast_data = get_weather_forecast(city, days)
    save_weather_to_file(city, days, forecast_data)

    print("Прогноз погоди збережено у файлі.")

if __name__ == "__main__":
    main()