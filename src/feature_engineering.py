# src/feature_engineering.py
import pandas as pd

def add_technical_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add technical indicators and lag features to the stock data.
    Calculates:
      - SMA_20: 20-day Simple Moving Average
      - SMA_50: 50-day Simple Moving Average
      - lag1: Price lagged by one day
    :param df: DataFrame with at least the 'price' column
    :return: DataFrame with new features
    """
    df['SMA_20'] = df['price'].rolling(window=20).mean()
    df['SMA_50'] = df['price'].rolling(window=50).mean()
    df['lag1'] = df['price'].shift(1)
    
    # Drop rows with NaN values generated by rolling or shifting
    df = df.dropna()
    return df
