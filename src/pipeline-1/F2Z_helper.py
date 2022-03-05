import pandas as pd

import path
import label

ENTRY = pd.read_csv(path.ENTRY, dtype={
    'V1': str,
    'NgayTG': str,
})

HANHCHINH = pd.read_csv(path.HANHCHINH, dtype={
    'V1': str,
    'MaHS': str,
    'HoTen': str,
    'NgaySinh': str,
})

FORM2 = pd.read_csv(path.FORM2, dtype={
    'V1': str,
})

# print(HANHCHINH.info())

def NGAY():
    """
    Get variable NGAY THAM GIA (yyyy-mm-dd)

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, NGAY 
    """
    df = (ENTRY[['V1', 'NgayTG']]
        .rename(columns={
            'V1': 'MANC',
            'NgayTG': 'NGAY'
        }))
    df['NGAY'] = pd.to_datetime(df['NGAY'])
    return df

def MAHS():
    """
    Get variable MA HO SO

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, MAHS 
    """
    df = (HANHCHINH[['V1', 'MaHS']]
        .rename(columns={
            'V1': 'MANC',
            'MaHS': 'MAHS'
        }))
    return df

def F2Z1():
    """
    Get variable HO TEN

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2Z1
    """
    df = (HANHCHINH[['V1', 'HoTen']]
        .rename(columns={
            'V1': 'MANC',
            'HoTen': 'F2Z1'
        }))
    df['F2Z1'] = df['F2Z1'].str.upper()
    return df

def F2Z2():
    """
    Get variable NGAY SINH (yyyy-mm-dd)

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2Z2
    """
    df = (HANHCHINH[['V1', 'NgaySinh']]
        .rename(columns={
            'V1': 'MANC',
            'NgaySinh': 'F2Z2'
        }))
    df['F2Z2'] = pd.to_datetime(df['F2Z2'])
    return df

def F2Z3():
    """
    Get variable GIOI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, GIOI
    """
    df = (HANHCHINH[['V1', 'GioiTinh']]
        .rename(columns={
            'V1': 'MANC',
            'GioiTinh': 'F2Z3'
        }))
    df['F2Z3'] = (df['F2Z3']
        .fillna('KHONG RO')
        .replace(label.GIOI))
    return df

def F2Z4_1():
    """
    Get variable NOI SINH - TINH THANH

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2Z4_1
    """
    df = (HANHCHINH[['V1', 'NSTinh']]
        .rename(columns={
            'V1': 'MANC',
            'NSTinh': 'F2Z4_1'
        }))
    df['F2Z4_1'] = (df['F2Z4_1']
        .fillna('KHONG RO')
        .replace(label.TINHTHANH))
    return df

def F2Z4_2():
    """
    Get variable NOI SINH - QUAN HUYEN

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2Z4_2
    """
    df = (HANHCHINH[['V1', 'NSQuan']]
        .rename(columns={
            'V1': 'MANC',
            'NSQuan': 'F2Z4_2'
        }))
    df['F2Z4_2'] = (df['F2Z4_2']
        .fillna('KHONG RO')
        .replace(label.QUANHUYEN))
    return df

def F2Z5_1():
    """
    Get variable NOI O - TINH THANH

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2Z5_1
    """
    df = (HANHCHINH[['V1', 'NOTinh']]
        .rename(columns={
            'V1': 'MANC',
            'NOTinh': 'F2Z5_1'
        }))
    df['F2Z5_1'] = (df['F2Z5_1']
        .fillna('KHONG RO')
        .replace(label.TINHTHANH))
    return df

def F2Z5_2():
    """
    Get variable NOI O - QUAN HUYEN

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2Z4_2
    """
    df = (HANHCHINH[['V1', 'NOQuan']]
        .rename(columns={
            'V1': 'MANC',
            'NOQuan': 'F2Z5_2'
        }))
    df['F2Z5_2'] = (df['F2Z5_2']
        .fillna('KHONG RO')
        .replace(label.QUANHUYEN))
    return df

