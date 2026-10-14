def calculate_daily_returns(data):
    data = data.copy()

    data["Daily Return"] = data["Close"].pct_change()

    return data


def estimate_parameters(data):
    returns = data["Daily Return"].dropna()

    mean_return = returns.mean()
    volatility = returns.std()

    return mean_return, volatility