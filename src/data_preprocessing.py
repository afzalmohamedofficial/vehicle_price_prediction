import pandas as pd

inputpath = r"data\Australian_Vehicle_Price_list.csv"
outputpath = r"data\Australian_Vehicle_Price_list_v02.csv"

# function here

def preprocess_data(inputpath, outputpath):
    df = pd.read_csv(inputpath)

    df_clean = df.dropna()

    #save cleaned data 
    return df_clean.to_csv(outputpath, index=False)


if __name__ == "__main__":
    preprocess_data(inputpath, outputpath)
    
