import pandas as pd
from io import BytesIO
import openpyxl

def test_load_data():
    # Create a simple DataFrame
    df = pd.DataFrame({"col1": [1, 3], "col2": [2, 4]})

    # Save the DataFrame to an in-memory Excel file
    with BytesIO() as output:
        # Writing DataFrame to the Excel file
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
        # Get the binary content of the Excel file
        excel_data = output.getvalue()

    # Now read the Excel file from the binary data
    with BytesIO(excel_data) as input_data:
        # Reading the Excel file
        df_read = pd.read_excel(input_data, engine='openpyxl')

    # Check that the data is loaded correctly into a DataFrame
    assert isinstance(df_read, pd.DataFrame)
    assert df_read.shape == (2, 2)  # 2 rows and 2 columns
    assert list(df_read.columns) == ['col1', 'col2']  # Column names are correct

    # Optional: check the actual values
    assert df_read.iloc[0, 0] == 1
    assert df_read.iloc[0, 1] == 2
    assert df_read.iloc[1, 0] == 3
    assert df_read.iloc[1, 1] == 4
