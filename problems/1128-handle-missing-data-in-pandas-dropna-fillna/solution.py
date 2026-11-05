import pandas as pd

def solution(df):
    complete_fraction_col = df.isna().mean() <= 0.5
    df = df.loc[:, complete_fraction_col]
    complete_fraction_row = df.isna().mean(axis=1) <= 0.5
    df = df.loc[complete_fraction_row,:]
    result = df.apply(lambda x: x.fillna(x.mean()) if x.dtypes=="float" else x.fillna(x.mode().iloc[0]))
    return result.reset_index(drop=True)