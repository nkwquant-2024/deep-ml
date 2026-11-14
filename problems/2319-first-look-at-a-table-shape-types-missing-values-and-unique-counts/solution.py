import pandas as pd


def first_look(df):
    """Return (shape, summary) where summary has one row per column of df."""




    shape = [len(df.index), len(df.columns) ]
    summary = pd.DataFrame(
        {
        'column': df.columns, 
        'dtype': df.dtypes.astype(str), 
        'missing': df.isnull().sum(), 
        'unique': df.nunique()
        }
    )

    return shape, summary
