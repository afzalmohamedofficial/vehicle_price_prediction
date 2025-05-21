from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np
import joblib
import os


def evaluate_model(X_data_csv, y_data_csv, model_path):
    X = pd.read_csv(X_data_csv)
    y = pd.read_csv(y_data_csv)

    model = joblib.load(model_path)
    y_pred = model.predict(X)
    
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    print("RMSE:", rmse)
    print("R² Score:", r2_score(y, y_pred))


if __name__ =="__main__":
    X_data_input_path = os.path.join("data", "Australian_Vehicle_Price_X_data.csv")
    y_data_input_path = os.path.join("data", "Australian_Vehicle_Price_y_data.csv")
    model_path = os.path.join("models", "linear_model.pkl")
    evaluate_model(X_data_input_path, y_data_input_path, model_path)

