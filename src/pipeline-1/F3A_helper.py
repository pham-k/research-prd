import pandas as pd

import path
import label
import util

FORM3 = pd.read_csv(path.FORM3, dtype={
    'V1': str,
})

def F3A1():
    """
    Get variable LY DO KHAM

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A1
    """
    cols = ['LyDoKham1', 'LyDoKham2', 'LyDoKham3', 'LyDoKham4', 'LyDoKham5', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.TRIEUCHUNG))
    
    df['F3A1'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3A2():
    """
    Get variable LY DO NOI SOI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A2
    """
    cols = ['LyDoNS1', 'LyDoNS2', 'LyDoNS3', 'LyDoNS4', 'LyDoNS5', 
            'LyDoNS6', 'LyDoNS7', 'LyDoNS8', 'LyDoNS9', 'LyDoNS10', 'LyDoNS11',]

    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.TRIEUCHUNG))
    
    df['F3A2'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3A3():
    """
    Get variable THOI GIAN BAT DAU TRIEU CHUNG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A3
    """
    df = (FORM3[['V1', 'TGBatDauTCNgay', 'TGBatDauTCThang', 'TGBatDauTCNam']]
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
    
    df['F3A3'] = df.apply(f, axis=1)
    df.drop(columns=['TGBatDauTCNgay', 'TGBatDauTCThang', 'TGBatDauTCNam'], inplace=True)
    return df

def F3A4():
    """
    Get variable DAU BUNG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A4
    """
    df = (FORM3[['V1', 'DauBungTS']]
        .rename(columns={
            'V1': 'MANC',
            'DauBungTS': 'F3A4'
        })
        .fillna('')
        .replace(label.TANSUATTUAN))
    
    return df

def F3A4A():
    """
    Get variable THOI GIAN DAU BUNG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A4A
    """
    df = (FORM3[['V1', 'DauBungTGNgay', 'DauBungTGThang', 'DauBungTGNam']]
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
    
    df['F3A4A'] = df.apply(f, axis=1)
    df.drop(columns=['DauBungTGNgay', 'DauBungTGThang', 'DauBungTGNam'], inplace=True)
    return df

def F3A4B():
    """
    Get variable DAU BUNG - KHOI PHAT

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A4B
    """
    cols = ['DauBungKP1', 'DauBungKP2', 'DauBungKP3', 'DauBungKP4', 'DauBungKP5', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.THOIDIEMKHOIPHAT))
    
    df['F3A4B'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3A4C():
    """
    Get variable DAU BUNG - LIEN QUAN BUA AN

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A4C
    """
    cols = ['DauBungBuaAn1', 'DauBungBuaAn2', 'DauBungBuaAn3', 'DauBungBuaAn4', 'DauBungBuaAn5', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.LIENQUANBUAAN))
    
    df['F3A4C'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3A4D():
    """
    Get variable DAU BUNG - VI TRI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A4D
    """
    cols = ['DauBungVT1', 'DauBungVT2', 'DauBungVT3', 'DauBungVT4', 'DauBungVT5', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.DAUBUNGVITRI))
    
    df['F3A4D'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3A4E():
    """
    Get variable DAU BUNG - KIEU

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A4E
    """
    cols = ['DauBungKieu1', 'DauBungKieu2', 'DauBungKieu3', 'DauBungKieu4', 'DauBungKieu5', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.DAUBUNGKIEU))
    
    df['F3A4E'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3A4F():
    """
    Get variable DAU BUNG - CACH GIAM

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A4F
    """
    cols = ['DauBungGiam1', 'DauBungGiam2', 'DauBungGiam3', 'DauBungGiam4', 
            'DauBungGiam5', 'DauBungGiam6', 'DauBungGiam7', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.DAUBUNGGIAM))
    
    df['F3A4F'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3A4G():
    """
    Get variable DAU BUNG - ANH HUONG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A4G
    """
    cols = ['DauBungAH1', 'DauBungAH2', 'DauBungAH3', 'DauBungAH4', 'DauBungAH5', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.DAUBUNGANHHUONG))
    
    df['F3A4G'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3A5():
    """
    Get variable OI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A5
    """
    df = (FORM3[['V1', 'OiTS']]
        .rename(columns={
            'V1': 'MANC',
            'OiTS': 'F3A5'
        })
        .fillna('')
        .replace(label.TANSUATTUAN))
    
    return df

def F3A5A():
    """
    Get variable OI - KHOI PHAT

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A5A
    """
    cols = ['OiKP1', 'OiKP2', 'OiKP3', 'OiKP4', 'OiKP5', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.THOIDIEMKHOIPHAT))
    
    df['F3A5A'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3A5B():
    """
    Get variable THOI GIAN OI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A5B
    """
    df = (FORM3[['V1', 'OiTGNgay', 'OiTGThang', 'OiTGNam']]
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
    
    df['F3A5B'] = df.apply(f, axis=1)
    df.drop(columns=['OiTGNgay', 'OiTGThang', 'OiTGNam'], inplace=True)
    return df

def F3A5C():
    """
    Get variable OI - LIEN QUAN BUA AN

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A5C
    """
    cols = ['OiBuaAn1', 'OiBuaAn2', 'OiBuaAn3', 'OiBuaAn4', 'OiBuaAn5', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.LIENQUANBUAAN))
    
    df['F3A5C'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3A5D():
    """
    Get variable OI - KIEU

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A5D
    """
    cols = ['OiKieu1', 'OiKieu2', 'OiKieu3', 'OiKieu4', 'OiKieu5', 'OiKieu6', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.OIKIEU))
    
    df['F3A5D'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3A5E():
    """
    Get variable OI - CAM GIAC

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A5E
    """
    cols = ['OiCamGiac1', 'OiCamGiac2', 'OiCamGiac3',] 
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.OICAMGIAC))
    
    df['F3A5E'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3A6A():
    """
    Get variable TAO BON

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A6A
    """
    df = (FORM3[['V1', 'TaoBon']]
        .rename(columns={
            'V1': 'MANC',
            'TaoBon': 'F3A6A'
        })
        .replace(label.NHIGIA)
        .fillna('KHONG RO')
        )
    
    return df

def F3A6B():
    """
    Get variable BRISTOL

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A6B
    """
    df = (FORM3[['V1', 'Bristol']]
        .rename(columns={
            'V1': 'MANC',
            'Bristol': 'F3A6B'
        })
        )
    
    return df

def F3A7():
    """
    Get variable THAY DOI CAN NANG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A7
    """
    df = (FORM3[['V1', 'ThayDoiCN']]
        .rename(columns={
            'V1': 'MANC',
            'ThayDoiCN': 'F3A7'
        })
        .fillna('KHONG RO')
        .replace(label.THAYDOICANNANG)
        )
    
    return df

def F3A8():
    """
    Get variable TRIEU CHUNG KHAC

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A8
    """
    cols = ['TCKhac1', 'TCKhac2', 'TCKhac3', 'TCKhac4', 'TCKhac5', 'TCKhac6', 'TCKhac7', 
            'TCKhac8', 'TCKhac9', 'TCKhac10', 'TCKhac11', 'TCKhac12', 'TCKhac13', ]
    df = (FORM3[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.TRIEUCHUNG))
    
    df['F3A8'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F3A9():
    """
    Get variable THIEU MAU

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A9
    """
    df = (FORM3[['V1', 'ThieuMau']]
        .rename(columns={
            'V1': 'MANC',
            'ThieuMau': 'F3A9'
        })
        .replace(label.NHIGIA)
        .fillna('KHONG RO')
        )
    
    return df

def F3A9A():
    """
    Get variable TRUYEN MAU

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A9A
    """
    df = (FORM3[['V1', 'TruyenMau']]
        .rename(columns={
            'V1': 'MANC',
            'TruyenMau': 'F3A9A'
        })
        .replace(label.NHIGIA)
        .fillna('KHONG')
        )
    
    return df

def F3A10():
    """
    Get variable NHOM MAU

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3A10
    """
    df = (FORM3[['V1', 'NhomMau']]
        .rename(columns={
            'V1': 'MANC',
            'NhomMau': 'F3A10'
        })
        .fillna('KHONG RO')
        .replace(label.NHOMMAU)
        )
    
    return df



