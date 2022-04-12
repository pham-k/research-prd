import pandas as pd

import path
import label
import util

FORM3 = pd.read_csv(path.FORM3, dtype={
    'V1': str,
})

def F3E1A():
    """
    Get variable UNG THU DA DAY

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3E1A
    """
    cols = ['NguoiThanKDD1', 'NguoiThanKDD2', 'NguoiThanKDD3', 'NguoiThanKDD4', 'NguoiThanKDD5', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.NGUOITHAN))
    
    df['F3E1A'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3E1B():
    """
    Get variable VIEM DA DAY

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3E1B
    """
    cols = ['NguoiThanVDD1', 'NguoiThanVDD2', 'NguoiThanVDD3', 'NguoiThanVDD4', 'NguoiThanVDD5', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.NGUOITHAN))
    
    df['F3E1B'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3E1C():
    """
    Get variable VIEM TA TRANG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3E1C
    """
    cols = ['NguoiThanVTT1', 'NguoiThanVTT2', 'NguoiThanVTT3', 'NguoiThanVTT4', 'NguoiThanVTT5', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.NGUOITHAN))
    
    df['F3E1C'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3E1D():
    """
    Get variable LOET DA DAY

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3E1D
    """
    cols = ['NguoiThanLDD1', 'NguoiThanLDD2', 'NguoiThanLDD3', 'NguoiThanLDD4', 'NguoiThanLDD5', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.NGUOITHAN))
    
    df['F3E1D'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3E1E():
    """
    Get variable LOET TA TRANG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3E1E
    """
    cols = ['NguoiThanLTT1', 'NguoiThanLTT2', 'NguoiThanLTT3', 'NguoiThanLTT4', 'NguoiThanLTT5', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.NGUOITHAN))
    
    df['F3E1E'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3E2A():
    """
    Get variable NGUOI NHIEM HP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3E2A
    """
    cols = ['NguoiThanHP1', 'NguoiThanHP2', 'NguoiThanHP3', 'NguoiThanHP4', 'NguoiThanHP5', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.NGUOITHAN))
    
    df['F3E2A'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3E2B():
    """
    Get variable NGUOI THAN HP SONG CHUNG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3E2B
    """
    cols = ['SongChungHP1', 'SongChungHP2', 'SongChungHP3', 'SongChungHP4', 'SongChungHP5', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.NGUOITHAN))
    
    df['F3E2B'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3E3():
    """
    Get variable TIEN CAN GD

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3E3
    """
    df = (FORM3[['V1', 'TienCanGD']]
        .rename(columns={
            'V1': 'MANC',
            'TienCanGD': 'F3E3'
        })
        .fillna('KHONG RO')
        .replace(label.NHIGIA)
        )
    
    return df
