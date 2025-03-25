import pandas as pd
import pytest  # Import pytest module
from src.analyze import analyze  # Import the analyze function (replace 'your_module' with the actual module name)

def test_analyze():
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    
    try:
        analyze(df)  # Pass the DataFrame to analyze()
    except Exception as e:
        pytest.fail(f"analyze() raised an exception: {e}")