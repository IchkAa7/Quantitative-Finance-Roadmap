from src.data_loader import load_stock_data
from src.strategy import calculate_moving_averages, generate_signals, generate_trades
from src.backtest import run_backtest
from src.metrics import (
    calculate_total_return,
    calculate_annualized_return,
    calculate_annualized_volatility,
    calculate_sharpe_ratio,
    calculate_max_drawdown,
    calculate_trade_statistics
)
from src.visualization import (
    plot_equity_curves,
    plot_trading_signals
)
def main():
    ticker = "AAPL"

    data = load_stock_data(
        ticker=ticker,
        start_date="2020-01-01",
        end_date="2026-01-01"
    )

    data = calculate_moving_averages(
        data,
        short_window=20,
        long_window=50
    )

    data = generate_signals(data)

    data = generate_trades(data)

    data = run_backtest(
    data,
    initial_capital=10000
    )

    strategy_total_return = calculate_total_return(
        data["Strategy Equity"]
    )

    buy_hold_total_return = calculate_total_return(
        data["Buy Hold Equity"]
    )

    strategy_annualized_return = calculate_annualized_return(
        data["Strategy Equity"]
    )

    buy_hold_annualized_return = calculate_annualized_return(
        data["Buy Hold Equity"]
    )

    strategy_volatility = calculate_annualized_volatility(
        data["Strategy Return"]
    )

    buy_hold_volatility = calculate_annualized_volatility(
        data["Market Return"]
    )

    strategy_sharpe = calculate_sharpe_ratio(
        data["Strategy Return"]
    )

    buy_hold_sharpe = calculate_sharpe_ratio(
        data["Market Return"]
    )

    strategy_max_drawdown = calculate_max_drawdown(
        data["Strategy Equity"]
    )

    buy_hold_max_drawdown = calculate_max_drawdown(
        data["Buy Hold Equity"]
    )

    trade_stats = calculate_trade_statistics(data)

    print(
    data[
        [
            "Close",
            "Signal",
            "Position",
            "Market Return",
            "Strategy Return",
            "Strategy Equity",
            "Buy Hold Equity"
        ]
    ].tail(20)
    )
    final_strategy_value = data["Strategy Equity"].iloc[-1]
    final_buy_hold_value = data["Buy Hold Equity"].iloc[-1]
    print("\nPERFORMANCE COMPARISON")

    print("\nStrategy")
    print(f"Total return: {strategy_total_return:.2%}")
    print(f"Annualized return: {strategy_annualized_return:.2%}")
    print(f"Annualized volatility: {strategy_volatility:.2%}")
    print(f"Sharpe ratio: {strategy_sharpe:.2f}")
    print(f"Max drawdown: {strategy_max_drawdown:.2%}")

    print("\nBuy & Hold")
    print(f"Total return: {buy_hold_total_return:.2%}")
    print(f"Annualized return: {buy_hold_annualized_return:.2%}")
    print(f"Annualized volatility: {buy_hold_volatility:.2%}")
    print(f"Sharpe ratio: {buy_hold_sharpe:.2f}")
    print(f"Max drawdown: {buy_hold_max_drawdown:.2%}")

    print("\nTRADE STATISTICS")
    print(f"Completed trades: {trade_stats['number_of_trades']}")
    print(f"Winning trades: {trade_stats['winning_trades']}")
    print(f"Losing trades: {trade_stats['losing_trades']}")
    print(f"Win rate: {trade_stats['win_rate']:.2%}")

    print(f"Average win: {trade_stats['average_win']:.2%}")
    print(f"Average loss: {trade_stats['average_loss']:.2%}")

    print(f"Profit factor: {trade_stats['profit_factor']:.2f}")
    print(f"Expectancy: {trade_stats['expectancy']:.2%}")

    print("\nBACKTEST RESULTS")

    print(f"Initial capital: €{10000:,.2f}")
    print(f"Strategy final value: €{final_strategy_value:,.2f}")
    print(f"Buy & Hold final value: €{final_buy_hold_value:,.2f}")

    plot_equity_curves(data)
    plot_trading_signals(data, ticker)


if __name__ == "__main__":
    main()