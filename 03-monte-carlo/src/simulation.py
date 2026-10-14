import numpy as np


def simulate_price_paths(
    last_price,
    mean_return,
    volatility,
    days=252,
    simulations=1000
):
    price_paths = np.zeros((days, simulations))

    price_paths[0] = last_price

    for day in range(1, days):
        random_shocks = np.random.normal(
            loc=mean_return,
            scale=volatility,
            size=simulations
        )

        price_paths[day] = (
            price_paths[day - 1]
            * (1 + random_shocks)
        )

    return price_paths