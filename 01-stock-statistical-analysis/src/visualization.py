"""
Functions used to create financial charts.
"""
import matplotlib.pyplot as plt


def plot_price(data, ticker):
    plt.figure(figsize=(12, 6))

    plt.plot(data.index, data["Close"])

    plt.title(f"{ticker} - Price")
    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.grid(True)

    plt.show()


def plot_daily_returns(data, ticker):
    plt.figure(figsize=(12, 6))

    plt.plot(data.index, data["Daily Return"])

    plt.title(f"{ticker} - Daily Returns")
    plt.xlabel("Date")
    plt.ylabel("Daily Return")

    plt.grid(True)

    plt.show()


def plot_return_distribution(data, ticker):
    returns = data["Daily Return"].dropna()

    plt.figure(figsize=(10, 6))

    plt.hist(returns, bins=50)

    plt.title(f"{ticker} - Return Distribution")
    plt.xlabel("Daily Return")
    plt.ylabel("Frequency")

    plt.grid(True)

    plt.show()


def plot_drawdown(data, ticker):
    close = data["Close"]

    running_max = close.cummax()

    drawdown = (close - running_max) / running_max

    plt.figure(figsize=(12, 6))

    plt.plot(data.index, drawdown)

    plt.title(f"{ticker} - Drawdown")
    plt.xlabel("Date")
    plt.ylabel("Drawdown")

    plt.grid(True)

    plt.show()