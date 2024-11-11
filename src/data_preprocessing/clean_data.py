import sqlite3
import pandas as pd


def clean_data():
    conn = sqlite3.connect('weather_data.db')
    df = pd.read_sql_query("SELECT * FROM weather_data", conn)
    df['date'] = pd.to_datetime(df['date'])
    df.dropna(inplace=True)
    df.to_sql('weather_data', conn, if_exists='replace', index=False)
    conn.close()

if __name__ == "__main__":
    clean_data()
    