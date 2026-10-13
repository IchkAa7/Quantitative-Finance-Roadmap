def calculate_moving_averages(data, short_window=20, long_window=50):
    data = data.copy()

    data["SMA_short"] = data["Close"].rolling(
        window=short_window
    ).mean()

    data["SMA_long"] = data["Close"].rolling(
        window=long_window
    ).mean()

    return data

def generate_signals(data):
    data = data.copy()

    data["Signal"] = 0

    data.loc[
        data["SMA_short"] > data["SMA_long"],
        "Signal"
    ] = 1

    return data

def generate_trades(data):
    data = data.copy()

    data["Trade"] = data["Signal"].diff()

    return data