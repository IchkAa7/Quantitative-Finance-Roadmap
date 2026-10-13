def run_backtest(data, initial_capital=10000):
    data = data.copy()

    # Rendement quotidien de l'action
    data["Market Return"] = data["Close"].pct_change()

    # Position détenue pendant la journée
    data["Position"] = data["Signal"].shift(1)

    # Rendement obtenu par la stratégie
    data["Strategy Return"] = (
        data["Position"] * data["Market Return"]
    )

    # Evolution du capital de la stratégie
    data["Strategy Equity"] = (
        initial_capital
        * (1 + data["Strategy Return"].fillna(0)).cumprod()
    )

    # Buy & Hold pour comparaison
    data["Buy Hold Equity"] = (
        initial_capital
        * (1 + data["Market Return"].fillna(0)).cumprod()
    )

    return data