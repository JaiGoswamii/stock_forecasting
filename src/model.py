# src/model.py
import pmdarima as pm
import numpy as np
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

def select_model_order(train_series: pd.Series, exog_train: pd.DataFrame = None, seasonal: bool = True, m: int = 252):
    """
    Automatically select SARIMAX order using auto_arima.
    :param train_series: Training time series (prices)
    :param exog_train: Optional exogenous variables DataFrame
    :param seasonal: Whether to consider seasonality
    :param m: Seasonal period (e.g., 252 for trading days in a year)
    :return: (order, seasonal_order)
    """
    auto_model = pm.auto_arima(
        train_series,
        exogenous=exog_train,
        seasonal=seasonal,
        m=m,
        trace=True,
        error_action='ignore',
        suppress_warnings=True
    )
    return auto_model.order, auto_model.seasonal_order

def fit_sarimax(train_series: pd.Series, exog_train: pd.DataFrame = None, order=None, seasonal_order=None):
    """
    Fit a SARIMAX model with optional exogenous variables.
    :param train_series: Training data (price series)
    :param exog_train: Exogenous variables for training
    :param order: ARIMA order tuple (p, d, q)
    :param seasonal_order: Seasonal order tuple (P, D, Q, m)
    :return: Fitted SARIMAX model
    """
    if order is None or seasonal_order is None:
        order, seasonal_order = select_model_order(train_series, exog_train)
    
    model = SARIMAX(train_series, exog=exog_train, order=order, seasonal_order=seasonal_order, enforce_stationarity=False, enforce_invertibility=False)
    model_fit = model.fit(disp=False)
    return model_fit

def forecast_model(model_fit, steps: int, exog_test: pd.DataFrame = None) -> pd.DataFrame:
    """
    Forecast future values using the fitted SARIMAX model.
    :param model_fit: Fitted SARIMAX model
    :param steps: Number of forecast steps
    :param exog_test: Exogenous variables for the forecast period
    :return: DataFrame containing the forecasted mean and confidence intervals
    """
    forecast_obj = model_fit.get_forecast(steps=steps, exog=exog_test)
    forecast_df = forecast_obj.summary_frame()
    return forecast_df
