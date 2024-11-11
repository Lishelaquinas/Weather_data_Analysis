import sqlite3
import pandas as pd


def analyse_data():
    conn = sqlite3.connect('weather_data.db')
    df = pd.read_sql_query("SELECT * FROM weather_data", conn)
    averageTemperature = df['temperature'].mean()
    avgerageHumidity = df['humidity'].mean()
    print(f"Average Temperature: {averageTemperature:.2f}°C")
    print(f"Average Humidity: {avgerageHumidity:.2f}%")
    conn.close()

if __name__ == "__main__":
    analyse_data()