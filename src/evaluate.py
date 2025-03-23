# src/evaluate.py
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error

def compute_metrics(actual: pd.Series, predicted: pd.Series) -> dict:
    """
    Compute RMSE, MAE, and MAPE between actual and predicted series.
    :param actual: Actual observed values
    :param predicted: Predicted values
    :return: Dictionary with evaluation metrics
    """
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    mae = mean_absolute_error(actual, predicted)
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100
    return {"RMSE": rmse, "MAE": mae, "MAPE": mape}
