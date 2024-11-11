from flask import Flask, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)

DATABASE = 'weather_data.db'

def get_data():
    conn = sqlite3.connect(DATABASE)
    df = pd.read_sql_query("SELECT * FROM weather_data", conn)
    conn.close()
    return df.to_dict(orient='records')

@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', weather_data=data)

if __name__ == "__main__":
    app.run(debug=True)
