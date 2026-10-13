import numpy as np


def calculate_total_return(equity_curve):
    return equity_curve.iloc[-1] / equity_curve.iloc[0] - 1


def calculate_annualized_return(equity_curve):
    total_return = calculate_total_return(equity_curve)

    number_of_days = len(equity_curve)

    annualized_return = (1 + total_return) ** (252 / number_of_days) - 1

    return annualized_return


def calculate_annualized_volatility(returns):
    returns = returns.dropna()

    return returns.std() * np.sqrt(252)


def calculate_sharpe_ratio(returns, risk_free_rate=0.0):
    returns = returns.dropna()

    daily_risk_free_rate = risk_free_rate / 252

    excess_returns = returns - daily_risk_free_rate

    return (
        excess_returns.mean()
        / excess_returns.std()
    ) * np.sqrt(252)


def calculate_max_drawdown(equity_curve):
    running_max = equity_curve.cummax()

    drawdown = (
        equity_curve - running_max
    ) / running_max

    return drawdown.min()
def calculate_trade_statistics(data):
    trades = []

    in_position = False
    entry_price = None

    for _, row in data.iterrows():

        if row["Trade"] == 1 and not in_position:
            entry_price = row["Close"]
            in_position = True

        elif row["Trade"] == -1 and in_position:
            exit_price = row["Close"]

            trade_return = (
                exit_price / entry_price
            ) - 1

            trades.append(trade_return)

            in_position = False
            entry_price = None

    number_of_trades = len(trades)

    if number_of_trades == 0:
        return {
            "number_of_trades": 0,
            "winning_trades": 0,
            "losing_trades": 0,
            "win_rate": 0
        }

    winning_trades = sum(
        trade_return > 0
        for trade_return in trades
    )

    losing_trades = sum(
        trade_return <= 0
        for trade_return in trades
    )

    win_rate = winning_trades / number_of_trades

    return {
        "number_of_trades": number_of_trades,
        "winning_trades": winning_trades,
        "losing_trades": losing_trades,
        "win_rate": win_rate
    }