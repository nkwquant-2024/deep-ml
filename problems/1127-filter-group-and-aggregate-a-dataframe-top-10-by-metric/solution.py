import pandas as pd

def solution(df):
    masks = (df["status"]=="completed")
    result = df[masks].sort_values(['amount'],ascending=False).groupby("region")["amount"].sum().reset_index().head(10)
    return result
