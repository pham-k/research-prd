import pandas as pd

import path
import label
import util

FORM3 = pd.read_csv(path.FORM3, dtype={
    'V1': str,
})

def F3B1():
    """
    Get variable TUNG XET NGHIEM HP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3B1
    """
    df = (FORM3[['V1', 'TungXNHP']]
        .rename(columns={
            'V1': 'MANC',
            'TungXNHP': 'F3B1'
        })
        .replace(label.NHIGIA)
        .fillna('KHONG RO')
        )
    
    return df

def F3B1A():
    """
    Get variable LOAI XET NGHIEM

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3B1A
    """
    cols = ['XNHP1', 'XNHP2', 'XNHP3', 'XNHP4', 'XNHP5', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('KHONG RO')
        .replace(label.XETNGHIEM))
    
    df['F3B1A'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3B1B():
    """
    Get variable KET QUA XET NGHIEM HP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3B1B
    """
    df = (FORM3[['V1', 'KQXN']]
        .rename(columns={
            'V1': 'MANC',
            'KQXN': 'F3B1B'
        })
        .replace(label.NHIGIA)
        .fillna('KHONG RO')
        )
    
    return df

def F3B2():
    """
    Get variable TUNG DIEU TRI HP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3B2
    """
    df = (FORM3[['V1', 'TungDTHP']]
        .rename(columns={
            'V1': 'MANC',
            'TungDTHP': 'F3B2'
        })
        .replace(label.NHIGIA)
        .fillna('KHONG RO')
        )
    
    return df

def F3B2A():
    """
    Get variable SO LAN DIEU TRI HP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3B2A
    """
    df = (FORM3[['V1', 'SoLanDT']]
        .rename(columns={
            'V1': 'MANC',
            'SoLanDT': 'F3B2A'
        })
        )
    
    return df

def F3B2A():
    """
    Get variable SO LAN DIEU TRI HP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3B2A
    """
    df = (FORM3[['V1', 'SoLanDT']]
        .rename(columns={
            'V1': 'MANC',
            'SoLanDT': 'F3B2A'
        })
        )
    
    return df

def F3B2B():
    """
    Get variable NGAY DIEU TRI GAN NHAT

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3B2B
    """
    df = (FORM3[['V1', 'NgayDTGanNhat']]
        .rename(columns={
            'V1': 'MANC',
            'NgayDTGanNhat': 'F3B2B'
        })
        )
    df['F3B2B'] = (
        pd.to_datetime(df['F3B2B'], errors='coerce', format="%m-%d-%Y")
        .dt.strftime('%Y-%m-%d')
        .fillna('KHONG RO')
    )

    return df

def F3B2C():
    """
    Get variable THUOC DIEU TRI GAN NHAT

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3B2C
    """
    cols = ['DTThuoc1', 'DTThuoc2', 'DTThuoc3', 'DTThuoc4', 
            'DTThuoc5', 'DTThuoc6', 'DTThuoc7', 'DTThuoc8', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.THUOC))
    
    df['F3B2C'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3B2D():
    """
    Get variable THOI GIAN DIEU TRI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A5D
    """
    df = (FORM3[['V1', 'DTTGNgay', 'DTTGThang', 'DTTGNam']]
        .rename(columns={
            'V1': 'MANC',
        }))
    
    def f(row):
        d, m, y = row[1], row[2], row[3]
        if pd.isna(d) and pd.isna(m) and pd.isna(y):
            return 'KHONG RO'
        elif pd.notna(d):
            return d
        elif pd.isna(d) and pd.notna(m):
            return m*30
        elif pd.isna(d) and pd.isna(m) and pd.notna(y):
            return y*365
        else:
            return 'PENDING'
    
    df['F3B2D'] = df.apply(f, axis=1)
    df.drop(columns=['DTTGNgay', 'DTTGThang', 'DTTGNam'], inplace=True)
    return df

def F3B2E():
    """
    Get variable XET NGHIEM SAU DIEU TRI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3B2E
    """
    cols = ['XNSauDT1', 'XNSauDT2', 'XNSauDT3', 'XNSauDT4', 'XNSauDT5', 'XNSauDT6', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('KHONG RO')
        .replace(label.XETNGHIEM))
    
    df['F3B2E'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3B2F():
    """
    Get variable KET QUA XET NGHIEM SAU DIEU TRI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3B2F
    """
    df = (FORM3[['V1', 'KQXNSauDT']]
        .rename(columns={
            'V1': 'MANC',
            'KQXNSauDT': 'F3B2F'
        })
        .replace(label.NHIGIA)
        .fillna('KHONG RO')
        )
    
    return df

def F3B3():
    """
    Get variable SO LAN NOI SOI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3B3
    """
    df = (FORM3[['V1', 'SoLanNS']]
        .rename(columns={
            'V1': 'MANC',
            'SoLanNS': 'F3B3'
        })
        )
    
    return df



