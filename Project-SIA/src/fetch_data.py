import requests
import pandas as pd

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Save the file locally or read directly into pandas
        with open('data.xlsx', 'wb') as f:
            f.write(response.content)
        # Load data into pandas DataFrame
        df = pd.read_excel('data.xlsx', engine='openpyxl')
        return df
    else:
        print("Failed to fetch data")
        return None