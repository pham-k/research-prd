import pandas as pd

import path
import label
import util

TK = pd.read_csv(path.TK, dtype={
    'V1': str,
})

def F52A1():
    """
    Get variable DAU BUNG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52A1
    """
    df = (TK
        .query('LanTK == 2.0')
        [['V1', 'DauBungTS']]
        .rename(columns={
            'V1': 'MANC',
            'DauBungTS': 'F52A1'
        })
        .fillna('')
        .replace(label.TANSUATTUAN))
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52A1A():
    """
    Get variable DAU BUNG - ANH HUONG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52A1A
    """
    cols = ['DauBungAH1', 'DauBungAH2', 'DauBungAH3', 'DauBungAH4', 'DauBungAH5', ]
    df = (TK.query('LanTK == 2.0')
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.DAUBUNGANHHUONG))
    
    df['F52A1A'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52A2():
    """
    Get variable OI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52A2
    """
    df = (TK
        .query('LanTK == 2.0')
        [['V1', 'OiTS']]
        .rename(columns={
            'V1': 'MANC',
            'OiTS': 'F52A2'
        })
        .fillna('')
        .replace(label.TANSUATTUAN))
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52A2A():
    """
    Get variable OI - TINH CHAT DICH

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52A2A
    """
    cols = ['OiTCDich1', 'OiTCDich2', 'OiTCDich3', 'OiTCDich4', 'OiTCDich5', ]
    df = (TK
        .query('LanTK == 2.0')
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.TINHCHATDICH))
    
    df['F52A2A'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52A3A():
    """
    Get variable TAO BON

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52A3A
    """
    df = (TK.query('LanTK == 2.0')
        [['V1', 'TaoBon']]
        .rename(columns={
            'V1': 'MANC',
            'TaoBon': 'F52A3A'
        })
        .replace(label.NHIGIA)
        .fillna('KHONG RO')
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52A3B():
    """
    Get variable BRISTOL

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52A3B
    """
    df = (TK.query('LanTK == 2.0')
        [['V1', 'Bristol']]
        .rename(columns={
            'V1': 'MANC',
            'Bristol': 'F52A3B'
        })
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52A4():
    """
    Get variable THAY DOI CAN NANG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52A4
    """
    df = (TK.query('LanTK == 2.0')
        [['V1', 'TDCanNang']]
        .rename(columns={
            'V1': 'MANC',
            'TDCanNang': 'F52A4'
        })
        .fillna('KHONG RO')
        .replace(label.THAYDOICANNANG)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52A5():
    """
    Get variable TRIEU CHUNG KHAC

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52A5
    """
    cols = ['TCKhac1', 'TCKhac2', 'TCKhac3', 'TCKhac4', 'TCKhac5', 'TCKhac6', 'TCKhac7', 
            'TCKhac8', 'TCKhac9', 'TCKhac10', 'TCKhac11', 'TCKhac12', 'TCKhac13', ]
    df = (TK.query('LanTK == 2.0')
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.TRIEUCHUNG))
    
    df['F52A5'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52A8():
    """
    Get variable CHIEU CAO

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52A8
    """
    df = (TK.query('LanTK == 2.0')
        [['V1', 'ChieuCao']]
        .rename(columns={
            'V1': 'MANC',
            'ChieuCao': 'F52A8'
        })
        .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52A9():
    """
    Get variable CAN NANG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52A9
    """
    df = (TK.query('LanTK == 2.0')
        [['V1', 'CanNang']]
        .rename(columns={
            'V1': 'MANC',
            'CanNang': 'F52A9'
        })
        .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df


