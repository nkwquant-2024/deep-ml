import pandas as pd
import numpy as np


def solution(df, window):
    # TODO: complete the daily calendar, keep NaN for missing days, trailing calendar-window mean
    # sort and keep NaN for missing days
    df = df.sort_values("date").set_index("date").asfreq("D") 
    #calculate the rolling mean
    df["rolling_mean"] = df["value"].rolling(window, min_periods=1).mean()
    df = df.reset_index()
    return df
