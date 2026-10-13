def calculate_moving_averages(data, short_window=20, long_window=50):
    data = data.copy()

    data["SMA_short"] = data["Close"].rolling(
        window=short_window
    ).mean()

    data["SMA_long"] = data["Close"].rolling(
        window=long_window
    ).mean()

    return data