# 📊 Advanced Stock Forecasting with SARIMAX

This project provides an end-to-end solution for stock price forecasting using the SARIMAX (Seasonal Autoregressive Integrated Moving Average with Exogenous Regressors) model. It covers data fetching, feature engineering, model training, forecasting, and evaluation.

## 🚀 Features
- **Data Fetching:** Retrieve historical stock data using APIs.
- **Feature Engineering:** Add technical indicators like Moving Averages and RSI.
- **Modeling:** Train SARIMAX models with optional exogenous variables.
- **Evaluation:** Calculate performance metrics including RMSE, MAE, and MAPE.
- **Visualization:** Plot actual vs. predicted prices.

## 🛠 Project Structure
```bash
├── main.py
├── src
│   ├── data_fetcher.py        # Fetches stock data using APIs
│   ├── feature_engineering.py # Adds technical indicators for feature enhancement
│   ├── model.py               # Trains and forecasts using SARIMAX
│   ├── evaluate.py            # Computes error metrics for model evaluation
│   └── utils.py               # Plots actual vs predicted prices
└── requirements.txt           # Lists all dependencies
```

## 🧑‍💻 Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/JaiGoswamii/stock_forecasting.git
    cd stock_forecasting
    ```
2. Install dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

## 📈 Usage
1. Open `main.py` and adjust the parameters such as:
    - **ticker**: Stock ticker symbol (e.g., "AAPL" for Apple)
    - **start_date** and **end_date**: Date range for fetching data
2. Run the project:
    ```bash
    python main.py
    ```
3. View the evaluation metrics and graphical visualizations.

## ⚙️ Functions Overview
- **fetch_stock_data(ticker, start_date, end_date)**: Fetches historical stock price data.
- **add_technical_indicators(df)**: Adds technical indicators like Moving Averages, RSI, etc.
- **fit_sarimax(train_data)**: Fits a SARIMAX model on training data.
- **forecast_model(model_fit, steps)**: Generates forecasts for the specified number of steps.
- **compute_metrics(actual, predicted)**: Calculates RMSE, MAE, and MAPE.
- **plot_forecast(train, test, forecast_df, ticker)**: Visualizes the actual vs. predicted results.

## 📊 Example Output
- Forecasted vs. Actual Prices Plot
- Evaluation Metrics such as:
  - RMSE: Root Mean Square Error
  - MAE: Mean Absolute Error
  - MAPE: Mean Absolute Percentage Error

## 📌 Future Enhancements
- Support for forecasting multiple tickers simultaneously.
- Incorporate additional exogenous variables.
- Implement hyperparameter tuning for model optimization.

## 🤝 Contributing
Contributions are welcome! If you'd like to improve this project, feel free to fork the repository and submit a pull request.

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
**Author:** Jai Goswami

[GitHub Repository](https://github.com/JaiGoswamii/stock_forecasting.git)

