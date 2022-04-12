import pandas as pd

import path
import label
import util

CAY = pd.read_csv(path.CAY, dtype={
    'V1': str,
})

PCR = pd.read_csv(path.PCR, dtype={
    'V1': str,
})

GPB = pd.read_csv(path.GPB, dtype={
    'V1': str,
})

NS = pd.read_csv(path.NS, dtype={
    'V1': str,
})

def F4C1():
    """
    Get variable CAY

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F4C1
    """
    df = (CAY
        [['V1', 'Cay']]
        .rename(columns={
            'V1': 'MANC',
            'Cay': 'F4C1'
        })
        .fillna('KHONG RO')
        .replace(label.NHIGIA))
    
    return df

def F4C2():
    """
    Get variable PCR

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F4C2
    """
    df = (PCR
        [['V1', 'PCR']]
        .rename(columns={
            'V1': 'MANC',
            'PCR': 'F4C2'
        })
        .fillna('KHONG RO')
        .replace(label.NHIGIA))
    # print(df[df.duplicated(subset=['MANC'])])
    df.drop_duplicates(['MANC'], inplace=True)
    return df

def F4C3():
    """
    Get variable UREASE

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F4C3
    """
    df = (NS
        .query('GhiChu == 2.0')
        [['V1', 'Clo']]
        .rename(columns={
            'V1': 'MANC',
            'Clo': 'F4C3'
        })
        .fillna('KHONG RO')
        .replace(label.NHIGIA))
    df.drop_duplicates(['MANC'], inplace=True)
    return df

def F4C4():
    """
    Get variable VI TRI GPB

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F4C4
    """
    df = (GPB
        [['V1', 'ViTri']]
        .rename(columns={
            'V1': 'MANC',
            'ViTri': 'F4C4'
        })
        .fillna('KHONG RO')
        .replace(label.GPBVITRI)
        )
    
    return df

def F4C4_HV():
    """
    Get variable HANG VI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F4C4_HVA, ..., F4C4_HVE
    """
    prefix = 'HV'
    suffixes = ['Neu', 'Lym', 'Teo', 'CSR', 'HP']
    cols = [prefix + e for e in suffixes]
    df = (GPB
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
            cols[0]: 'F4C4_HVA',
            cols[1]: 'F4C4_HVB',
            cols[2]: 'F4C4_HVC',
            cols[3]: 'F4C4_HVD',
            cols[4]: 'F4C4_HVE',
        })
        .fillna('KHONG RO')
        .replace(label.GPBMUCDO)
        )
    
    return df

def F4C4_HVTT():
    """
    Get variable HANG VI - TON THUONG KHAC

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F4C4_HVTT
    """
    cols = ['HVTonThuong1', 'HVTonThuong2', 'HVTonThuong3', 'HVTonThuong4', 'HVTonThuong5', ]
    df = (GPB[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .replace(label.TONTHUONGGPB)
        .fillna(''))
    
    df['F4C4_HVTT'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F4C4_TV():
    """
    Get variable THAN VI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F4C4_TVA, ..., F4C4_TVE
    """
    prefix = 'TV'
    suffixes = ['Neu', 'Lym', 'Teo', 'CSR', 'HP']
    cols = [prefix + e for e in suffixes]
    df = (GPB
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
            cols[0]: 'F4C4_TVA',
            cols[1]: 'F4C4_TVB',
            cols[2]: 'F4C4_TVC',
            cols[3]: 'F4C4_TVD',
            cols[4]: 'F4C4_TVE',
        })
        .fillna('KHONG RO')
        .replace(label.GPBMUCDO)
        )
    
    return df

def F4C4_TVTT():
    """
    Get variable THAN VI - TON THUONG KHAC

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F4C4_TVTT
    """
    cols = ['TVTonThuong1', 'TVTonThuong2', 'TVTonThuong3', 'TVTonThuong4', 'TVTonThuong5', ]
    df = (GPB[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .replace(label.TONTHUONGGPB)
        .fillna('')
    )
    
    df['F4C4_TVTT'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F4C4_HTV():
    """
    Get variable HANG THAN VI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F4C4_HTVA, ..., F4C4_HTVE
    """
    prefix = 'HTV'
    suffixes = ['Neu', 'Lym', 'Teo', 'CSR', 'HP']
    cols = [prefix + e for e in suffixes]
    df = (GPB
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
            cols[0]: 'F4C4_HTVA',
            cols[1]: 'F4C4_HTVB',
            cols[2]: 'F4C4_HTVC',
            cols[3]: 'F4C4_HTVD',
            cols[4]: 'F4C4_HTVE',
        })
        .fillna('KHONG RO')
        .replace(label.GPBMUCDO)
        )
    
    return df

def F4C4_HTVTT():
    """
    Get variable HANG THAN VI - TON THUONG KHAC

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F4C4_HTVTT
    """
    cols = ['HTVTonThuong1', 'HTVTonThuong2', 'HTVTonThuong3', 'HTVTonThuong4', 'HTVTonThuong5', ]
    df = (GPB[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .replace(label.TONTHUONGGPB)
        .fillna('')
    )
    
    df['F4C4_HTVTT'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

