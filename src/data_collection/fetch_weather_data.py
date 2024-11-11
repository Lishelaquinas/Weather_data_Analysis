import requests # type: ignore
from datetime import datetime, timedelta
import time
import sqlite3


API_KEY = "YOUR API KEY"
lat, lon = 43.0481, -76.1474




def get_current_weather_data (date):
        timestamp = int(datetime.strptime(date, '%Y-%m-%d').timestamp())
        #print(timestamp)
        url  = f'https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={timestamp}&appid={API_KEY}'
        
        res = requests.get(url)
        return res.json()


def get_weather_data():
    weather_data = []
    start_date = datetime.strptime('2024-01-01', '%Y-%m-%d')
   
    end_date = datetime.now()
    #loop over each date and get the data 
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime('%Y-%m-%d')
        data = get_current_weather_data(date_str)
        try:
            daily_weather = {
            'date': date_str,
            'temperature': data['data'][0]['temp'],
            'humidity': data['data'][0]['humidity'],
            'pressure': data['data'][0]['pressure'],
            'weather': data['data'][0]['weather'][0]['description']
        }
            weather_data.append(daily_weather)
            #print(daily_weather)

            time.sleep(1)
            current_date += timedelta(days=1)
        except:
            print(str(date_str) + " Data Error")
    return weather_data

def save_to_db(data):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_data
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        temperature REAL,
        humidity INTEGER,
        pressure INTEGER,
        weather TEXT ) ''')
    for weather_data in data:
        cursor.execute("""
        INSERT INTO weather_data (date, temperature, humidity, pressure, weather)
        VALUES (?, ?, ?, ?, ?)
    """, (weather_data['date'], weather_data['temperature'], weather_data['humidity'], weather_data['pressure'], weather_data['weather']))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    data = get_weather_data()
    save_to_db(data)
     



