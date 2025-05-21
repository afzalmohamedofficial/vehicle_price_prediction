import os
import pandas as pd
from src.data_preprocessing import preprocess_data

def test_preprocess_data_creates_output():
    input_path = r"data\Australian_Vehicle_Price_X_data.csv"
    output_path = r"data\Australian_Vehicle_Price_X_data_cleaned.csv"

    preprocess_data(input_path,output_path)

    assert os.path.exists(output_path)

    df = pd.read_csv(output_path)
    assert not df.empty

    os.remove(output_path) # Clean up after test


