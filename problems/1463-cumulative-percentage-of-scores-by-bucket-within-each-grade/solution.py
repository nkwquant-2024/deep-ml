import pandas as pd


def solution(df):
    # TODO: bucket scores, count per (grade, bucket), cumulative percentage within grade
    pass
    df["bucket"] = (df["score"] // 10) * 10
    df = (
    df.groupby(["grade", "bucket"])
        .size()
        .reset_index(name="count")
        .sort_values(["grade", "bucket"])
        .reset_index(drop=True)
        )

    df["cum_pct"] = (df.groupby("grade")["count"].cumsum() / df.groupby("grade")["count"].transform("sum") * 100).round(2)

    return df
