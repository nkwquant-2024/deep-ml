import pandas as pd

def solution(df1, df2, df3):
    df1_2 = df1.merge(df2, on="emp_id", how="inner")
    result_df = df1_2.merge(df3, on="emp_id", how="left")
    return result_df