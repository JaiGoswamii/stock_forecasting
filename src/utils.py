# src/utils.py
import matplotlib.pyplot as plt

def plot_forecast(train, test, forecast_df, ticker: str):
    """
    Plot the historical training data, test data, and forecast results.
    :param train: Training data (DataFrame with 'price')
    :param test: Test data (DataFrame with 'price')
    :param forecast_df: Forecast DataFrame with 'mean', 'mean_ci_lower', 'mean_ci_upper'
    :param ticker: Stock ticker symbol for title
    """
    plt.figure(figsize=(12, 6))
    plt.plot(train.index, train['price'], label='Train')
    plt.plot(test.index, test['price'], label='Test', color='green')
    plt.plot(forecast_df.index, forecast_df['mean'], label='Forecast', color='red')
    plt.fill_between(forecast_df.index, forecast_df['mean_ci_lower'], forecast_df['mean_ci_upper'], color='pink', alpha=0.3)
    plt.title(f"{ticker} Stock Price Forecast")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()
