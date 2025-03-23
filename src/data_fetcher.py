# src/data_fetcher.py
import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, start_date: str, end_date: str, interval: str = "1d") -> pd.DataFrame:
    """
    Fetch historical stock data for a given ticker.
    :param ticker: Stock ticker symbol (e.g., "AAPL")
    :param start_date: Start date in YYYY-MM-DD format
    :param end_date: End date in YYYY-MM-DD format
    :param interval: Data interval (e.g., "1d", "1wk")
    :return: DataFrame with stock data (with 'Close' renamed to 'price')
    """
    data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    if data.empty:
        raise ValueError("No data found. Check your ticker or date range.")
    df = data[['Close']].copy()
    df.rename(columns={'Close': 'price'}, inplace=True)
    return df