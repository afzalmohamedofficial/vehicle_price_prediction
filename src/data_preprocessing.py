import pandas as pd
import os

inputpath = os.path.join("data, "Australian_Vehicle_Price_X_data.csv")
outputpath = os.path.join("data, "Australian_Vehicle_Price_list_cleaned.csv")                         

# function here

def preprocess_data(inputpath, outputpath):
    df = pd.read_csv(inputpath)

    df_clean = df.dropna()

    #save cleaned data 
    return df_clean.to_csv(outputpath, index=False)


if __name__ == "__main__":
    preprocess_data(inputpath, outputpath)
