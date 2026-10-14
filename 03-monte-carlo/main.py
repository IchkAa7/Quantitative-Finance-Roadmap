from src.data_loader import load_stock_data
from src.metrics import (
    calculate_daily_returns,
    estimate_parameters
)


def main():
    ticker = "AAPL"

    data = load_stock_data(
        ticker=ticker,
        start_date="2020-01-01",
        end_date="2026-01-01"
    )

    data = calculate_daily_returns(data)

    mean_return, volatility = estimate_parameters(data)

    print("\nMONTE CARLO PARAMETERS")
    print(f"Mean daily return: {mean_return:.4%}")
    print(f"Daily volatility: {volatility:.4%}")
    print(f"Last price: ${data['Close'].iloc[-1]:.2f}")


if __name__ == "__main__":
    main()