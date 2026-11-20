import pandas as pd


def select_orders(df, countries, low, high):
    """Return order_id, country, amount for the orders that pass the rule."""
    pass
    mask_country = df["country"].isin(countries)
    mask_amount = (df["amount"].between(low,high , inclusive ="both")) | df["vip"]==True
    result = df.loc[mask_country&mask_amount,:].drop("vip", axis=1)
    return result
