# Moving Average Backtest

Second project in my quantitative finance roadmap.

## Objective

Build and evaluate a simple moving average crossover strategy using historical market data.

The strategy is based on two moving averages:

- Short moving average: 20 days
- Long moving average: 50 days

When the short moving average is above the long moving average, the strategy stays invested.

When the short moving average is below the long moving average, the strategy stays out of the market.

## Strategy Logic

```text
SMA20 > SMA50
→ Long position

SMA20 <= SMA50
→ Cash