import pandas as pd

def solution(df):
    df["name"] = df["name"].str.strip().str.capitalize()
    df["date"] = df["date"].str.strip()
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    df = df.drop_duplicates()
    df["value"] = df["value"].fillna(df["value"].mean())
    return df.reset_index(drop=True)