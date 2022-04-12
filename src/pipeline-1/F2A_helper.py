import pandas as pd

import path
import label
import util

FORM2 = pd.read_csv(path.FORM2, dtype={
    'V1': str,
})

def F2A1():
    """
    Get variable CON THU MAY

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2A1
    """
    df = (FORM2[['V1', 'ConThu']]
        .rename(columns={
            'V1': 'MANC',
            'ConThu': 'F2A1'
        }))
    return df

def F2A2():
    """
    Get variable TUOI THAI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2A2
    """
    df = (FORM2[['V1', 'TuoiThai', 'TuoiThaiTT']]
        .rename(columns={
            'V1': 'MANC',
            'TuoiThai': 'F2A2',
        }))
    
    df['F2A2'] = (df['F2A2']
        .fillna('KHONG RO')
        .replace(label.TUOITHAI))
    
    def f(row):
        if row[1] == label.TUOITHAI[2] and pd.notna(row[2]):
            return row[1] + ' ' + str(row[2])[0:2] + ' TUAN'
        else:
            return row[1]
    
    df['F2A2'] = df.apply(f, axis=1)
    df.drop(columns='TuoiThaiTT', inplace=True)
    return df

def F2A3():
    """
    Get variable PHUONG PHAP SANH

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2A3
    """
    df = (FORM2[['V1', 'PPSanh']]
        .rename(columns={
            'V1': 'MANC',
            'PPSanh': 'F2A3'
        })
        .fillna('KHONG RO')
        .replace(label.PPSINH))
    return df

def F2A4():
    """
    Get variable CAN NANG LUC SANH

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2A4
    """
    df = (FORM2[['V1', 'CNLS']]
        .rename(columns={
            'V1': 'MANC',
            'CNLS': 'F2A4'
        }))
    return df

def F2A5():
    """
    Get variable DI TAT BAM SINH

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2A5
    """
    cols = ['DTBS1', 'DTBS2', 'DTBS3', 'DTBS4', 'DTBS5',]
    df = (FORM2[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.DTBS))
    
    df['F2A5'] = df.apply(util.concatenate_columns, axis=1)
    # print(df.columns)
    df.drop(columns=cols, inplace=True)
    return df

def F2A6():
    """
    Get variable NUOI DUONG 6 THANG DAU

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2A6
    """
    cols = ['NuoiDuong6T1', 'NuoiDuong6T2', 'NuoiDuong6T3', 'NuoiDuong6T4', 'NuoiDuong6T5',]
    df = (FORM2[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.NUOIDUONG6T))
    
    df['F2A6'] = df.apply(util.concatenate_columns, axis=1)
    # print(df.columns)
    df.drop(columns=cols, inplace=True)
    return df

def F2A7():
    """
    Get variable BU ME DEN MAY THANG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2A7
    """
    df = (FORM2[['V1', 'BuMe']]
        .rename(columns={
            'V1': 'MANC',
            'BuMe': 'F2A7'
        }))
    return df

def F2A8():
    """
    Get variable BAT DAU AN DAM LUC MAY THANG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2A8
    """
    df = (FORM2[['V1', 'AnDam']]
        .rename(columns={
            'V1': 'MANC',
            'AnDam': 'F2A8'
        }))
    return df

def F2A9():
    """
    Get variable NHAI MOM

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2A9
    """
    df = (FORM2[['V1', 'NhaiMom']]
        .rename(columns={
            'V1': 'MANC',
            'NhaiMom': 'F2A9'
        })
        .fillna('KHONG RO')
        .replace(label.NHAIMOM))
    return df

def F2A10():
    """
    Get variable TIEM CHUNG MO RONG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2A10
    """
    df = (FORM2[['V1', 'TCMR']]
        .rename(columns={
            'V1': 'MANC',
            'TCMR': 'F2A10'
        })
        .fillna('KHONG RO')
        .replace(label.TCMR))
    return df

def F2A11():
    """
    Get variable BAT DAU DI HOC

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2A11
    """
    df = (FORM2[['V1', 'DiHocThang', 'DiHocTuoi']]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna(0))
    
    def f(row):
        if row[1] == 0 and row[2] == 0:
            return 'KHONG RO'
        elif row[1] == 0 and row[2] != 0:
            return row[2] * 12
        else:
            return row[1]
    
    df['F2A11'] = df.apply(f, axis=1)
    df.drop(columns=['DiHocThang', 'DiHocTuoi'], inplace=True)
    return df

