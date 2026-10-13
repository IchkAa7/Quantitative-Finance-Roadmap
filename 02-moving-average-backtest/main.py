from src.data_loader import load_stock_data
from src.strategy import calculate_moving_averages, generate_signals, generate_trades
from src.backtest import run_backtest

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

    print("\nBACKTEST RESULTS")

    print(f"Initial capital: €{10000:,.2f}")
    print(f"Strategy final value: €{final_strategy_value:,.2f}")
    print(f"Buy & Hold final value: €{final_buy_hold_value:,.2f}")


if __name__ == "__main__":
    main()