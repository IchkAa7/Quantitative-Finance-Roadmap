import pandas as pd
import yfinance as yf


def load_stock_data(ticker, start_date, end_date):
    data = yf.download(
        ticker,
        start=start_date,
        end=end_date
    )

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    return data