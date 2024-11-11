#!/bin/bash

# Run data collection every hour
0 * * * * /usr/bin/python3 /path/to/your/project/data_collection/fetch_weather_data.py
# Run data cleaning daily
0 1 * * * /usr/bin/python3 /path/to/your/project/data_processing/clean_data.py
# Run data analysis weekly
0 0 * * 0 /usr/bin/python3 /path/to/your/project/data_processing/analyze_data.py
