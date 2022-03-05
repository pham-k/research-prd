import pandas as pd

def get_col(df1, df2):
    pass

def concatenate_columns(row):
    """
    Concatenate columns

    Args:
        cols: list of columns
    
    Returns:
        A string, separated by ', ', ignore None or empty string
    """
    return ', '.join(list(filter(None, row[1:].tolist())))