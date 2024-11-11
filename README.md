## Weather Data Analysis
This project collects, processes, stores, and visualizes weather data from a weather API, enabling users to monitor temperature, humidity, and other metrics over time. The data is stored in a SQLite database, and a web dashboard displays the information, updated regularly through scheduled tasks.

### Prerequisites
Python 3.7+ - Ensure you have Python installed.
Virtual Environment (recommended) - Set up a virtual environment to manage dependencies.

### Setup
#### 1.Clone the repository:

git clone https://github.com/Lishelaquinas/Weather-Data-Analysis.git
cd Weather-Data-Analysis

#### 2.Create a virtual environment and activate it:

python -m venv venv
.\venv\Scripts\activate

#### 3. Install dependencies:

pip install -r requirements.txt

#### 4.Add your API Key

#### Run the project.
**Run Data Collection**:
    ```bash
    python data_collection/fetch_weather_data.py
    ```

**Run Data Cleaning**:
    ```bash
    python data_processing/clean_data.py
    ```

**Run Data Analysis**:
    ```bash
    python data_processing/analyze_data.py
    ```

**Generate Visualization**:
    ```bash
    python visualization/weather_dashboard.py
    ```

**Start Flask Web Application**:
    ```bash
    cd web_app
    python app.py
    ```

## Scheduling

To automate the pipeline, use the provided `scheduling/cron_jobs.sh` script to schedule the tasks using cron.
