import requests
from core.config import OPEN_WEATHER_API_KEY

def get_current_weather(sity):
    sity = sity.lower()
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={sity}&appid={OPEN_WEATHER_API_KEY}&units=metric"
        )
        r = r.json()
        return r
    except Exception as ex :
        print(ex)
        print('check sity name')

def generate_weather_data(data_dict):
    sity_name = data_dict['name']
    temp = data_dict['main']['temp']
    humidity = data_dict['main']['humidity']
    max_temp = data_dict['main']['temp_max']
    min_temp = data_dict['main']['temp_min']
    return f"""
    Sity Name: {sity_name} 
    Temperature: {temp}C°
    Humidity: {humidity} %
    Max Temperature: {max_temp}C°
    Min Temperature: {min_temp}C°
    """
    


if __name__ == "__main__":
    weather = get_current_weather('london')        
    print(generate_weather_data(weather))
    # pprint(weather)