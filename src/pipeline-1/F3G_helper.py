import pandas as pd

import path
import label
import util

CTM = pd.read_csv(path.CTM, dtype={
    'V1': str,
})

NS = pd.read_csv(path.NS, dtype={
    'V1': str,
})

def F3G1_F3G4():
    """
    Get variable WBC to PLT

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3G1, ..., F3G4
    """
    df = (CTM[['V1', 'WBC', 'Neu', 'Eos', 'Baso', 'Lym', 'Mono',
               'Hct', 'Hb', 'Plt']]
        .rename(columns={
            'V1': 'MANC',
            'WBC': 'F3G1',
            'Neu': 'F3G1A',
            'Eos': 'F3G1B',
            'Baso': 'F3G1C',
            'Lym': 'F3G1D',
            'Mono': 'F3G1E',
            'Hct': 'F3G2',
            'Hb': 'F3G3',
            'Plt': 'F3G4',
        })
        )
    
    return df

def F3G5():
    """
    Get variable UREASE

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3G5
    """
    df = (NS[['V1', 'Clo']]
        .rename(columns={
            'V1': 'MANC',
            'Clo': 'F3G5'
        })
        .replace(label.NHIGIA)
        .fillna('KHONG RO')
        )
    
    return df

def F3G6():
    """
    Get variable NOI SOI THUC QUAN

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3G6
    """
    prefix='ThucQuan'
    suffixes = ['1', '2', '3', '4', '5']
    cols = [prefix + e for e in suffixes]
    df = (
        NS.query('GhiChu == 2.0')
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC'
        })
        .fillna('')
        .replace(label.TONTHUONG)
        )
    df['F3G6'] = df.apply(util.concatenate_columns, axis=1).replace({'': 'BINH THUONG'})
    df.drop(columns=cols, inplace=True)
    df.drop_duplicates(subset=['MANC'], inplace=True)
    # df.to_excel(path.INTERMEDIATE + 'F3G6.xlsx')
    return df

def F3G7_PV():
    """
    Get variable TON THUONG PHINH VI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3G7_PV
    """
    prefix='PhinhVi'
    suffixes = ['1', '2', '3', '4', '5']
    cols = [prefix + e for e in suffixes]
    df = (
        NS.query('GhiChu == 2.0')
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC'
        })
        .fillna('')
        .replace(label.TONTHUONG)
        )
    df['F3G7_PV'] = df.apply(util.concatenate_columns, axis=1).replace({'': 'BINH THUONG'})
    df.drop(columns=cols, inplace=True)
    df.drop_duplicates(subset=['MANC'], inplace=True)
    # df.to_excel(path.INTERMEDIATE + 'F3G7_PV.xlsx')
    return df

def F3G7_TV():
    """
    Get variable TON THUONG THAN VI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3G7_TV
    """
    prefix='ThanVi'
    suffixes = ['1', '2', '3', '4', '5']
    cols = [prefix + e for e in suffixes]
    df = (
        NS.query('GhiChu == 2.0')
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC'
        })
        .fillna('')
        .replace(label.TONTHUONG)
        )
    df['F3G7_TV'] = df.apply(util.concatenate_columns, axis=1).replace({'': 'BINH THUONG'})
    df.drop(columns=cols, inplace=True)
    df.drop_duplicates(subset=['MANC'], inplace=True)

    return df

def F3G7_HV():
    """
    Get variable TON THUONG HANG VI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3G7_HV
    """
    prefix='HangVi'
    suffixes = ['1', '2', '3', '4', '5']
    cols = [prefix + e for e in suffixes]
    df = (
        NS.query('GhiChu == 2.0')
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC'
        })
        .fillna('')
        .replace(label.TONTHUONG)
        )
    df['F3G7_HV'] = df.apply(util.concatenate_columns, axis=1).replace({'': 'BINH THUONG'})
    df.drop(columns=cols, inplace=True)
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F3G7_MV():
    """
    Get variable TON THUONG MON VI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3G7_MV
    """
    prefix='MonVi'
    suffixes = ['1', '2', '3', '4', '5']
    cols = [prefix + e for e in suffixes]
    df = (
        NS.query('GhiChu == 2.0')
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC'
        })
        .fillna('')
        .replace(label.TONTHUONG)
        )
    df['F3G7_MV'] = df.apply(util.concatenate_columns, axis=1).replace({'': 'BINH THUONG'})
    df.drop(columns=cols, inplace=True)
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F3G7_HTT():
    """
    Get variable TON THUONG HANH TA TRANG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3G7_HTT
    """
    prefix='HTT'
    suffixes = ['1', '2', '3', '4', '5']
    cols = [prefix + e for e in suffixes]
    df = (
        NS.query('GhiChu == 2.0')
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC'
        })
        .fillna('')
        .replace(label.TONTHUONG)
        )
    df['F3G7_HTT'] = df.apply(util.concatenate_columns, axis=1).replace({'': 'BINH THUONG'})
    df.drop(columns=cols, inplace=True)
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F3G7_D2():
    """
    Get variable TON THUONG D2

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F3G7_D2
    """
    prefix='D2'
    suffixes = ['1', '2', '3', '4', '5']
    cols = [prefix + e for e in suffixes]
    df = (
        NS.query('GhiChu == 2.0')
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC'
        })
        .fillna('')
        .replace(label.TONTHUONG)
        )
    df['F3G7_D2'] = df.apply(util.concatenate_columns, axis=1).replace({'': 'BINH THUONG'})
    df.drop(columns=cols, inplace=True)
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F3G8_PV():
    """
    Get variable LOET PHINH VI

    Args:
        None

    Returns:
        DataFrame contains 5 columns MANC, F3G8_PVA, F3G8_PVB, F3G8_PVC, F3G8_PVD
    """
    prefix='PhinhVi'
    suffixes = ['OLoet', 'KTOLoet', 'Forest', 'Seo']
    cols = [prefix + e for e in suffixes]
    df = (
        NS.query('GhiChu == 2.0')
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        )
    df[cols[0]] = df[cols[0]].fillna(0)
    df[cols[1]] = df[cols[1]].fillna(0)
    df[cols[2]] = df[cols[2]].fillna('KHONG RO').replace(label.FOREST)
    df[cols[3]] = df[cols[3]].fillna(0).replace(label.NHIGIA)
    df.rename(columns={
        cols[0]: 'F3G8_PVA',
        cols[1]: 'F3G8_PVB',
        cols[2]: 'F3G8_PVC',
        cols[3]: 'F3G8_PVD',
    }, inplace=True)
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F3G8_TV():
    """
    Get variable LOET THAN VI

    Args:
        None

    Returns:
        DataFrame contains 5 columns MANC, F3G8_TVA, F3G8_TVB, F3G8_TVC, F3G8_TVD
    """
    prefix='ThanVi'
    suffixes = ['OLoet', 'KTOLoet', 'Forest', 'Seo']
    cols = [prefix + e for e in suffixes]
    df = (
        NS.query('GhiChu == 2.0')
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        )
    df[cols[0]] = df[cols[0]].fillna(0)
    df[cols[1]] = df[cols[1]].fillna(0)
    df[cols[2]] = df[cols[2]].fillna('KHONG RO').replace(label.FOREST)
    df[cols[3]] = df[cols[3]].fillna(0).replace(label.NHIGIA)
    df.rename(columns={
        cols[0]: 'F3G8_TVA',
        cols[1]: 'F3G8_TVB',
        cols[2]: 'F3G8_TVC',
        cols[3]: 'F3G8_TVD',
    }, inplace=True)
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F3G8_HV():
    """
    Get variable LOET HANG VI

    Args:
        None

    Returns:
        DataFrame contains 5 columns MANC, F3G8_HVA, F3G8_HVB, F3G8_HVC, F3G8_HVD
    """
    prefix='HangVi'
    suffixes = ['OLoet', 'KTOLoet', 'Forest', 'Seo']
    cols = [prefix + e for e in suffixes]
    df = (
        NS.query('GhiChu == 2.0')
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        )
    df[cols[0]] = df[cols[0]].fillna(0)
    df[cols[1]] = df[cols[1]].fillna(0)
    df[cols[2]] = df[cols[2]].fillna('KHONG RO').replace(label.FOREST)
    df[cols[3]] = df[cols[3]].fillna(0).replace(label.NHIGIA)
    df.rename(columns={
        cols[0]: 'F3G8_HVA',
        cols[1]: 'F3G8_HVB',
        cols[2]: 'F3G8_HVC',
        cols[3]: 'F3G8_HVD',
    }, inplace=True)
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F3G8_MV():
    """
    Get variable LOET MON VI

    Args:
        None

    Returns:
        DataFrame contains 5 columns MANC, F3G8_MVA, F3G8_MVB, F3G8_MVC, F3G8_MVD
    """
    prefix='MonVi'
    suffixes = ['OLoet', 'KTOLoet', 'Forest', 'Seo']
    cols = [prefix + e for e in suffixes]
    df = (
        NS.query('GhiChu == 2.0')
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        )
    df[cols[0]] = df[cols[0]].fillna(0)
    df[cols[1]] = df[cols[1]].fillna(0)
    df[cols[2]] = df[cols[2]].fillna('KHONG RO').replace(label.FOREST)
    df[cols[3]] = df[cols[3]].fillna(0).replace(label.NHIGIA)
    df.rename(columns={
        cols[0]: 'F3G8_MVA',
        cols[1]: 'F3G8_MVB',
        cols[2]: 'F3G8_MVC',
        cols[3]: 'F3G8_MVD',
    }, inplace=True)
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F3G8_HTT():
    """
    Get variable LOET HANH TA TRANG

    Args:
        None

    Returns:
        DataFrame contains 5 columns MANC, F3G8_HTTA, F3G8_HTTB, F3G8_HTTC, F3G8_HTTD
    """
    prefix='HTT'
    suffixes = ['OLoet', 'KTOLoet', 'Forest', 'Seo']
    cols = [prefix + e for e in suffixes]
    df = (
        NS.query('GhiChu == 2.0')
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        )
    df[cols[0]] = df[cols[0]].fillna(0)
    df[cols[1]] = df[cols[1]].fillna(0)
    df[cols[2]] = df[cols[2]].fillna('KHONG RO').replace(label.FOREST)
    df[cols[3]] = df[cols[3]].fillna(0).replace(label.NHIGIA)
    df.rename(columns={
        cols[0]: 'F3G8_HTTA',
        cols[1]: 'F3G8_HTTB',
        cols[2]: 'F3G8_HTTC',
        cols[3]: 'F3G8_HTTD',
    }, inplace=True)
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F3G8_D2():
    """
    Get variable LOET D2

    Args:
        None

    Returns:
        DataFrame contains 5 columns MANC, F3G8_D2A, F3G8_D2B, F3G8_D2C, F3G8_D2D
    """
    prefix='D2'
    suffixes = ['OLoet', 'KTOLoet', 'Forest', 'Seo']
    cols = [prefix + e for e in suffixes]
    df = (
        NS.query('GhiChu == 2.0')
        [['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        )
    df[cols[0]] = df[cols[0]].fillna(0)
    df[cols[1]] = df[cols[1]].fillna(0)
    df[cols[2]] = df[cols[2]].fillna('KHONG RO').replace(label.FOREST)
    df[cols[3]] = df[cols[3]].fillna(0).replace(label.NHIGIA)
    df.rename(columns={
        cols[0]: 'F3G8_D2A',
        cols[1]: 'F3G8_D2B',
        cols[2]: 'F3G8_D2C',
        cols[3]: 'F3G8_D2D',
    }, inplace=True)
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

