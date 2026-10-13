from yfinance import data

from src.data_loader import load_stock_data
from src.metrics import (
    calculate_daily_returns,
    calculate_return_statistics,
    calculate_cumulative_return,
    calculate_annualized_return,
    calculate_annualized_volatility,
    calculate_max_drawdown,
    calculate_sharpe_ratio,
    calculate_skewness,
    calculate_kurtosis
)

from src.visualization import (
    plot_price,
    plot_daily_returns,
    plot_return_distribution,
    plot_drawdown
)


def main():
    data = load_stock_data(
        ticker="AAPL",
        start_date="2020-01-01",
        end_date="2026-01-01"
    )

    data = calculate_daily_returns(data)

    stats = calculate_return_statistics(data)

    cumulative_return = calculate_cumulative_return(data)
    annualized_return = calculate_annualized_return(data)
    annualized_volatility = calculate_annualized_volatility(data)
    max_drawdown = calculate_max_drawdown(data)
    sharpe_ratio = calculate_sharpe_ratio(data)
    skewness = calculate_skewness(data)
    kurtosis = calculate_kurtosis(data)

    print("\nRETURN STATISTICS")
    print(f"Mean daily return: {stats['mean_daily_return']:.4%}")
    print(f"Daily volatility: {stats['daily_volatility']:.4%}")
    print(f"Best day: {stats['best_day']:.4%}")
    print(f"Worst day: {stats['worst_day']:.4%}")

    print("\nLONG-TERM METRICS")
    print(f"Cumulative return: {cumulative_return:.2%}")
    print(f"Annualized return: {annualized_return:.2%}")
    print(f"Annualized volatility: {annualized_volatility:.2%}")
    print(f"Max drawdown: {max_drawdown:.2%}")

    print("\nRISK METRICS")
    print(f"Sharpe ratio: {sharpe_ratio:.2f}")
    print(f"Skewness: {skewness:.2f}")
    print(f"Kurtosis: {kurtosis:.2f}")
    
    plot_price(data, "AAPL")
    plot_daily_returns(data, "AAPL")
    plot_return_distribution(data, "AAPL")
    plot_drawdown(data, "AAPL")


if __name__ == "__main__":
    main()