# main.py
import pandas as pd
from datetime import datetime

from src.data_fetcher import fetch_stock_data
from src.feature_engineering import add_technical_indicators
from src.model import fit_sarimax, forecast_model
from src.evaluate import compute_metrics
from src.utils import plot_forecast

def main():
    # Define parameters
    ticker = "AAPL"
    start_date = "2015-01-01"
    end_date = "2023-01-01"
    
    # 1. Fetch historical stock data
    print("Fetching data...")
    df = fetch_stock_data(ticker, start_date, end_date)
    
    # 2. Feature Engineering
    print("Engineering features...")
    df = add_technical_indicators(df)
    
    # (Optional) Use additional features as exogenous variables
    # Here, we'll use Volume as a simple exogenous variable if available.
    # For our dataset, we only have 'price', but you can modify fetch_stock_data to include more columns.
    # For now, we'll proceed without exogenous variables.
    exog = None  # Replace with your exogenous DataFrame if needed
    
    # 3. Split Data (80% train, 20% test)
    train_size = int(len(df) * 0.8)
    train = df.iloc[:train_size]
    test = df.iloc[train_size:]
    
    # 4. Fit SARIMAX Model
    print("Fitting SARIMAX model...")
    model_fit = fit_sarimax(train['price'], exog_train=exog if exog is not None else None)
    
    # 5. Forecasting
    print("Forecasting...")
    steps = len(test)
    forecast_df = forecast_model(model_fit, steps, exog_test=exog if exog is not None else None)
    
    # 6. Evaluation
    metrics = compute_metrics(test['price'], forecast_df['mean'])
    print("Evaluation Metrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.2f}")
    
    # 7. Plot the results
    plot_forecast(train, test, forecast_df, ticker)
    
if __name__ == "__main__":
    main()
