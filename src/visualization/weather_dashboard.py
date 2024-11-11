import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



def create_dashboard():
    # Connect to the database
    conn = sqlite3.connect('weather_data.db')
    df = pd.read_sql_query('SELECT * FROM weather_data', conn)
    
    # Convert the 'date' column to datetime format if it's not already
    df['date'] = pd.to_datetime(df['date'])
    
    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['temperature'], marker='o', color='b', linestyle='-', linewidth=1)
    plt.title('Temperature Over Time')
    plt.xlabel('Datetime')
    plt.ylabel('Temperature')
    
    # Format the x-axis to show labels only on Mondays with the desired format
    ax = plt.gca()  # Get the current axis
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MONDAY))  # Show labels only on Mondays
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Format as 'Year-Month-Day'
    
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.tight_layout()
    
    # Save the plot as an image
    plt.savefig('weather_dashboard.png')
    
    # Close the database connection
    conn.close()


if __name__ == "__main__":
    create_dashboard()



