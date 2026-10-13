from src.data_loader import load_stock_data
from src.strategy import calculate_moving_averages


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

    print(
        data[
            ["Close", "SMA_short", "SMA_long"]
        ].head(60)
    )


if __name__ == "__main__":
    main()