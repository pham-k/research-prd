import pandas as pd

import path
import label
import util

FORM3 = pd.read_csv(path.FORM3, dtype={
    'V1': str,
})

TIENCAN = pd.read_csv(path.TIENCAN, dtype={
    'V1': str,
})

def F3C1A():
    """
    Get variable TIEN CAN BE

    Args:
        None

    Returns:
        DataFrame contains 3 columns MANC, F3C1A_BENH, F3C1A_KP
    """
    df = (TIENCAN
        .query('NguoiBi == 9.0')
        .rename(columns = {
            'V1': 'MANC',
            'KPNgay': 'day',
            'KPThang': 'month',
            'KPNam': 'year',
            'Benh': 'F3C1A_BENH',
        })
    )
    df['rank'] = df.groupby(['MANC'])['F3C1A_BENH'].rank(method='first')
    df.loc[:, 'F3C1A_BENH'] = df['F3C1A_BENH'].replace(label.BENH)
    df.loc[:, 'day'] = df['day'].replace({98.0: 1.0})
    df.loc[:, 'month'] = df['month'].replace({98.0: 1.0})
    df['F3C1A_KP'] = (
        pd.to_datetime(df[['day', 'month', 'year']], errors='coerce')
        .dt.strftime('%Y-%m-%d')
        .fillna('KHONG RO'))
    df = df.query('rank == 1.0').drop(columns=[
        'GhiChu', 'NguoiBi', 'KTThang', 'KTNgay', 'KTNam', 'rank',
        'day', 'month', 'year'])
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F3C1B():
    """
    Get variable TIEN CAN BE

    Args:
        None

    Returns:
        DataFrame contains 3 columns MANC, F3C1B_BENH, F3C1B_KP
    """
    df = (TIENCAN
        .query('NguoiBi == 9.0')
        .rename(columns = {
            'V1': 'MANC',
            'KPNgay': 'day',
            'KPThang': 'month',
            'KPNam': 'year',
            'Benh': 'F3C1B_BENH',
        })
    )
    df['rank'] = df.groupby(['MANC'])['F3C1B_BENH'].rank(method='first')
    df.loc[:, 'F3C1B_BENH'] = df['F3C1B_BENH'].replace(label.BENH)
    df.loc[:, 'day'] = df['day'].replace({98.0: 1.0})
    df.loc[:, 'month'] = df['month'].replace({98.0: 1.0})
    df['F3C1B_KP'] = (
        pd.to_datetime(df[['day', 'month', 'year']], errors='coerce')
        .dt.strftime('%Y-%m-%d')
        .fillna('KHONG RO'))
    df = df.query('rank == 2.0').drop(columns=[
        'GhiChu', 'NguoiBi', 'KTThang', 'KTNgay', 'KTNam', 'rank',
        'day', 'month', 'year'])
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F3C1C():
    """
    Get variable TIEN CAN BE

    Args:
        None

    Returns:
        DataFrame contains 3 columns MANC, F3C1C_BENH, F3C1C_KP
    """
    df = (TIENCAN
        .query('NguoiBi == 9.0')
        .rename(columns = {
            'V1': 'MANC',
            'KPNgay': 'day',
            'KPThang': 'month',
            'KPNam': 'year',
            'Benh': 'F3C1C_BENH',
        })
    )
    df['rank'] = df.groupby(['MANC'])['F3C1C_BENH'].rank(method='first')
    df.loc[:, 'F3C1C_BENH'] = df['F3C1C_BENH'].replace(label.BENH)
    df.loc[:, 'day'] = df['day'].replace({98.0: 1.0})
    df.loc[:, 'month'] = df['month'].replace({98.0: 1.0})
    df['F3C1C_KP'] = (
        pd.to_datetime(df[['day', 'month', 'year']], errors='coerce')
        .dt.strftime('%Y-%m-%d')
        .fillna('KHONG RO'))
    df = df.query('rank == 3.0').drop(columns=[
        'GhiChu', 'NguoiBi', 'KTThang', 'KTNgay', 'KTNam', 'rank',
        'day', 'month', 'year'])
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df


# print(F3C1A().head(10))