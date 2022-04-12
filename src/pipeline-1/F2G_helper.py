import pandas as pd

import path
import label
import util

FORM2 = pd.read_csv(path.FORM2, dtype={
    'V1': str,
})

def F2G1():
    """
    Get variable SO ANH CHI EM RUOT

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2G1
    """
    df = (FORM2[['V1', 'SoACE']]
        .rename(columns={
            'V1': 'MANC',
            'SoACE': 'F2G1'
        })
        .fillna('KHONG RO')
        )
    return df

def F2G2_F2G4():
    """
    Get variables DAN TOC BE to DAN TOC BA

    Args:
        None

    Returns:
        DataFrame contains 4 columns MANC, F2G2, ..., F2G4
    """
    s = 'DanTocBe	DanTocMe	DanTocBa'
    old_cols = s.split('	')
    new_cols = ['F2G' + str(x) for x in range(2, 5)]
    columns = dict(zip(old_cols, new_cols))
    
    df = (FORM2[['V1'] + old_cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .rename(columns=columns)
        .fillna('KHONG RO')
        .replace(label.DANTOC))
    
    return df

def F2G5_F2G7():
    """
    Get variables TON GIAO BE to TON GIAO ME BA

    Args:
        None

    Returns:
        DataFrame contains 4 columns MANC, F2G5, ..., F2G7
    """
    s = 'TonGiaoBe	TonGiaoMe	TonGiaoBa'
    old_cols = s.split('	')
    new_cols = ['F2G' + str(x) for x in range(5, 8)]
    columns = dict(zip(old_cols, new_cols))
    
    df = (FORM2[['V1'] + old_cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .rename(columns=columns)
        .fillna('KHONG RO')
        .replace(label.TONGIAO))
    
    return df

def F2G8_F2G9():
    """
    Get variables NGAY SINH ME to NGAY SINH BA

    Args:
        None

    Returns:
        DataFrame contains 3 columns MANC, F2G8, F2G9
    """
    
    df = (FORM2[['V1', 'NgaySinhMe', 'NgaySinhBa']]
        .rename(columns={
            'V1': 'MANC',
            'NgaySinhMe': 'F2G8',
            'NgaySinhBa': 'F2G9',
        })
        .fillna('KHONG RO')
        )
    df['F2G8'] = (
        pd.to_datetime(df['F2G8'], errors='coerce', format="%m-%d-%Y")
        .dt.strftime('%Y-%m-%d')
        .fillna('KHONG RO')
    )
    df['F2G9'] = (
        pd.to_datetime(df['F2G9'], errors='coerce', format="%m-%d-%Y")
        .dt.strftime('%Y-%m-%d')
        .fillna('KHONG RO')
    )
    
    return df

def F2G10_F2G11():
    """
    Get variable NOI SINH ME, NOI SINH BA

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2G10, F2G11
    """
    df = (FORM2[['V1', 'NSTinhMe', 'NSTinhBa']]
        .rename(columns={
            'V1': 'MANC',
            'NSTinhMe': 'F2G10',
            'NSTinhBa': 'F2G11',
        }))
    df['F2G10'] = (df['F2G10']
        .fillna('KHONG RO')
        .replace(label.TINHTHANH))
    df['F2G11'] = (df['F2G11']
        .fillna('KHONG RO')
        .replace(label.TINHTHANH))
    return df

def F2G12_F2G13():
    """
    Get variable NGHE NGHIEP ME, NGHE NGHIEP BA

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2G12, F2G13
    """
    df = (FORM2[['V1', 'NNMe', 'NNBa']]
        .rename(columns={
            'V1': 'MANC',
            'NNMe': 'F2G12',
            'NNBa': 'F2G13',
        }))
    df['F2G12'] = (df['F2G12']
        .fillna('KHONG RO')
        .replace(label.NGHENGHIEP))
    df['F2G13'] = (df['F2G13']
        .fillna('KHONG RO')
        .replace(label.NGHENGHIEP))
    return df

def F2G14_F2G15():
    """
    Get variable TRINH DO HOC VAN ME, BA

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2G14, F2G15
    """
    df = (FORM2[['V1', 'TDHVMe', 'TDHVBa']]
        .rename(columns={
            'V1': 'MANC',
            'TDHVMe': 'F2G14',
            'TDHVBa': 'F2G15',
        }))
    df['F2G14'] = (df['F2G14']
        .fillna('KHONG RO')
        .replace(label.TRINHDOHOCVAN))
    df['F2G15'] = (df['F2G15']
        .fillna('KHONG RO')
        .replace(label.TRINHDOHOCVAN))
    return df

def F2G16A_F2G16B():
    """
    Get variable SO NGUOI SONG CHUNG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2G16A, F2G16B
    """
    df = (FORM2[['V1', 'SongChungNL', 'SongChungTE']]
        .rename(columns={
            'V1': 'MANC',
            'SongChungNL': 'F2G16A',
            'SongChungTE': 'F2G16B',
        }))
    df['F2G16A'] = (df['F2G16A']
        .fillna('KHONG RO'))
    df['F2G16B'] = (df['F2G16B']
        .fillna('KHONG RO'))
    return df

def F2G17():
    """
    Get variable SONG CHUNG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2G17
    """
    cols = ['SongChung1', 'SongChung2', 'SongChung3', 'SongChung4', 'SongChung5',
            'SongChung6', 'SongChung7', 'SongChung8', 'SongChung9', ]
    df = (FORM2[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.SONGCHUNG))
    
    df['F2G17'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

