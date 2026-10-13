import matplotlib.pyplot as plt


def plot_equity_curves(data):
    plt.figure(figsize=(12, 6))

    plt.plot(
        data.index,
        data["Strategy Equity"],
        label="Strategy"
    )

    plt.plot(
        data.index,
        data["Buy Hold Equity"],
        label="Buy & Hold"
    )

    plt.title("Strategy vs Buy & Hold")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")

    plt.legend()
    plt.grid(True)

    plt.show()


def plot_trading_signals(data, ticker):
    plt.figure(figsize=(14, 7))

    plt.plot(
        data.index,
        data["Close"],
        label="Close"
    )

    plt.plot(
        data.index,
        data["SMA_short"],
        label="SMA Short"
    )

    plt.plot(
        data.index,
        data["SMA_long"],
        label="SMA Long"
    )

    buy_signals = data[data["Trade"] == 1]
    sell_signals = data[data["Trade"] == -1]

    plt.scatter(
        buy_signals.index,
        buy_signals["Close"],
        marker="^",
        s=100,
        label="BUY"
    )

    plt.scatter(
        sell_signals.index,
        sell_signals["Close"],
        marker="v",
        s=100,
        label="SELL"
    )

    plt.title(f"{ticker} - Moving Average Strategy")
    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.legend()
    plt.grid(True)

    plt.show()