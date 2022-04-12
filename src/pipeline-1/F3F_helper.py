import pandas as pd

import path
import label
import util

FORM3 = pd.read_csv(path.FORM3, dtype={
    'V1': str,
})

def F3F1():
    """
    Get variable CAN NANG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3F1
    """
    df = (FORM3[['V1', 'CanNang']]
        .rename(columns={
            'V1': 'MANC',
            'CanNang': 'F3F1'
        })
        .fillna(0)
        )
    
    return df

def F3F2():
    """
    Get variable CHIEU CAO

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3F2
    """
    df = (FORM3[['V1', 'ChieuCao']]
        .rename(columns={
            'V1': 'MANC',
            'ChieuCao': 'F3F2'
        })
        .fillna(0)
        )
    
    return df


