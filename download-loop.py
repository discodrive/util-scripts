import requests
from datetime import datetime
import sys
import time

url = "https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD"
query_parameters = {"downloadformat": "csv"}
log = open("log.txt", "a")

while True:
    timestamp = str(datetime.now())
    
    try:
        response = requests.get(url, params=query_parameters)
        response.raise_for_status()

        with open("gdp_by_country.zip", mode="wb") as file:
            file.write(response.content)

        log.write(f"File downloaded successfully at {timestamp}\n")
        print("File downloaded successfully")

        time.sleep(5)
    except requests.exceptions.RequestException as e:
        log.write(f"File failed to download at {timestamp}: {str(e)}\n")
        print("Download failed. Please see log.txt for more information.")
        
        time.sleep(10)  
        
