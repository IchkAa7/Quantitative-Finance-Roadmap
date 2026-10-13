def run_backtest(
    data,
    initial_capital=10000,
    transaction_cost=0.001
):
    data = data.copy()

    data["Market Return"] = (
        data["Close"]
        .pct_change()
        .fillna(0)
    )

    data["Position"] = (
        data["Signal"]
        .shift(1)
        .fillna(0)
    )

    data["Gross Strategy Return"] = (
        data["Position"] * data["Market Return"]
    )

    data["Executed Trade"] = (
        data["Position"]
        .diff()
        .abs()
        .fillna(0)
    )

    data["Transaction Cost"] = (
        data["Executed Trade"] * transaction_cost
    )

    data["Strategy Return"] = (
        data["Gross Strategy Return"]
        - data["Transaction Cost"]
    )

    data["Strategy Equity"] = (
        initial_capital
        * (1 + data["Strategy Return"]).cumprod()
    )

    data["Buy Hold Equity"] = (
        initial_capital
        * (1 + data["Market Return"]).cumprod()
    )

    return data