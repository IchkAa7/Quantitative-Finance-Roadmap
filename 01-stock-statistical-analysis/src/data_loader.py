"""
Functions used to load stock market data.
"""
import yfinance as yf


def load_stock_data(ticker, start_date, end_date):
    data = yf.download(
        ticker,
        start=start_date,
        end=end_date
    )

    return data