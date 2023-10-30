import numpy as np
import pandas as pd


def simpson_multipliers(y):
    N = len(y)
    assert len(y) >= 3, "At least three points must exist for simsons integration"
    assert (
        N % 2 == 1
    ), "There must be an uneven number of stations for this simple rule to hold"
    n = int(np.floor(N / 2))
    multipliers = 0.5 * np.ones(N)
    multipliers[0 : 2 * n] = np.tile([1.0, 2.0], n)
    multipliers[0] = 0.5
    multipliers[-1] = 0.5

    return multipliers


def simpson_table(y):
    df = pd.DataFrame()
    df["y"] = y

    df["S/M"] = simpson_multipliers(y=y)
    df["product"] = df["y"] * df["S/M"]

    return df


def simpson(y, d: float):
    df = simpson_table(y)
    integral = 2 / 3 * d * df["product"].sum()
    return integral
