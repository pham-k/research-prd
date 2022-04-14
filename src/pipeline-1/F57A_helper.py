import pandas as pd

import path
import label
import util

TK = pd.read_csv(path.TK, dtype={
    'V1': str,
})

def F57_NGAY():
    """
    Get variable NGAY THAM GIA (yyyy-mm-dd)

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, NGAY 
    """
    df = (TK
        .query('LanTK == 7.0')
        [['V1', 'NgayTK']]
        .rename(columns={
            'V1': 'MANC',
            'NgayTK': 'F57_NGAY'
        }))
    df.drop_duplicates(subset=['MANC'], inplace=True)
    df['F57_NGAY'] = pd.to_datetime(df['F57_NGAY']).dt.strftime('%Y-%m-%d')
    return df


def F57A1():
    """
    Get variable DAU BUNG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57A1
    """
    df = (TK
        .query('LanTK == 7.0')
        [['V1', 'DauBungTS']]
        .rename(columns={
            'V1': 'MANC',
            'DauBungTS': 'F57A1'
        })
        .fillna('')
        .replace(label.TANSUATTUAN))
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57A1A():
    """
    Get variable DAU BUNG - ANH HUONG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57A1A
    """
    cols = ['DauBungAH1', 'DauBungAH2', 'DauBungAH3', 'DauBungAH4', 'DauBungAH5', ]
    df = (TK.query('LanTK == 7.0')
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.DAUBUNGANHHUONG))
    
    df['F57A1A'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57A2():
    """
    Get variable OI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57A2
    """
    df = (TK
        .query('LanTK == 7.0')
        [['V1', 'OiTS']]
        .rename(columns={
            'V1': 'MANC',
            'OiTS': 'F57A2'
        })
        .fillna('')
        .replace(label.TANSUATTUAN))
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57A2A():
    """
    Get variable OI - TINH CHAT DICH

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57A2A
    """
    cols = ['OiTCDich1', 'OiTCDich2', 'OiTCDich3', 'OiTCDich4', 'OiTCDich5', ]
    df = (TK
        .query('LanTK == 7.0')
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.TINHCHATDICH))
    
    df['F57A2A'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57A3A():
    """
    Get variable TAO BON

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57A3A
    """
    df = (TK.query('LanTK == 7.0')
        [['V1', 'TaoBon']]
        .rename(columns={
            'V1': 'MANC',
            'TaoBon': 'F57A3A'
        })
        .replace(label.NHIGIA)
        .fillna('KHONG RO')
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57A3B():
    """
    Get variable BRISTOL

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57A3B
    """
    df = (TK.query('LanTK == 7.0')
        [['V1', 'Bristol']]
        .rename(columns={
            'V1': 'MANC',
            'Bristol': 'F57A3B'
        })
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57A4():
    """
    Get variable THAY DOI CAN NANG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57A4
    """
    df = (TK.query('LanTK == 7.0')
        [['V1', 'TDCanNang']]
        .rename(columns={
            'V1': 'MANC',
            'TDCanNang': 'F57A4'
        })
        .fillna('KHONG RO')
        .replace(label.THAYDOICANNANG)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57A5():
    """
    Get variable TRIEU CHUNG KHAC

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57A5
    """
    cols = ['TCKhac1', 'TCKhac2', 'TCKhac3', 'TCKhac4', 'TCKhac5', 'TCKhac6', 'TCKhac7', 
            'TCKhac8', 'TCKhac9', 'TCKhac10', 'TCKhac11', 'TCKhac12', 'TCKhac13', ]
    df = (TK.query('LanTK == 7.0')
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.TRIEUCHUNG))
    
    df['F57A5'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57A8():
    """
    Get variable CHIEU CAO

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57A8
    """
    df = (TK.query('LanTK == 7.0')
        [['V1', 'ChieuCao']]
        .rename(columns={
            'V1': 'MANC',
            'ChieuCao': 'F57A8'
        })
        .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57A9():
    """
    Get variable CAN NANG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57A9
    """
    df = (TK.query('LanTK == 7.0')
        [['V1', 'CanNang']]
        .rename(columns={
            'V1': 'MANC',
            'CanNang': 'F57A9'
        })
        .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df


