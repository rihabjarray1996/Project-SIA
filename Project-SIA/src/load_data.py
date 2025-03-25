import pandas as pd

def load_data(file_path):
    # Load Excel file into pandas DataFrame
    df = pd.read_excel(file_path, engine='openpyxl')
    return df