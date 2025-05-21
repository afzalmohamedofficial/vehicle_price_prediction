import os
from src.train_model import train_and_save_model



def test_train_model_saves_file():
    X_path = r"data\Australian_Vehicle_Price_X_data.csv"
    y_path = r"data\Australian_Vehicle_Price_y_data.csv"
    model_path = r"models\linear_model.pkl"

    train_and_save_model(X_path, y_path, model_path)

    assert os.path.exists(model_path)
    assert os.path.getsize(model_path)>0

    os.remove(model_path)