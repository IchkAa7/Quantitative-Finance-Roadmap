from src.data_loader import load_stock_data
from src.metrics import (
    calculate_daily_returns,
    estimate_parameters
)
from src.simulation import simulate_price_paths

def main():
    ticker = "AAPL"

    data = load_stock_data(
        ticker=ticker,
        start_date="2020-01-01",
        end_date="2026-01-01"
    )

    data = calculate_daily_returns(data)

    mean_return, volatility = estimate_parameters(data)
    last_price = data["Close"].iloc[-1]

    price_paths = simulate_price_paths(
        last_price=last_price,
        mean_return=mean_return,
        volatility=volatility,
        days=252,
        simulations=1000
    )

    print("\nSIMULATION")
    print(f"Shape: {price_paths.shape}")
    print(f"First simulated final price: ${price_paths[-1, 0]:.2f}")

    print("\nMONTE CARLO PARAMETERS")
    print(f"Mean daily return: {mean_return:.4%}")
    print(f"Daily volatility: {volatility:.4%}")
    print(f"Last price: ${data['Close'].iloc[-1]:.2f}")


if __name__ == "__main__":
    main()