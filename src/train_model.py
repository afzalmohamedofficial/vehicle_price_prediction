import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

def train_and_save_model(X_data_csv, y_data_csv, model_path):
    # Load data
    X = pd.read_csv(X_data_csv)
    y = pd.read_csv(y_data_csv)

    model = LinearRegression()
    model.fit(X, y)

    os.makedirs(os.path.dirname(model_path), exist_ok=True)

    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")


if __name__ == "__main__":
    X_data_input_path = r"data\Australian_Vehicle_Price_X_data.csv"
    y_data_input_path = r"data\Australian_Vehicle_Price_y_data.csv"
    model_path = r"models\linear_model.pkl"
    train_and_save_model(X_data_input_path, y_data_input_path, model_path)

