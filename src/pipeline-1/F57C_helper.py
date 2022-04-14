import pandas as pd

import path
import label
import util

TK = pd.read_csv(path.TK, dtype={
    'V1': str,
})

TDP = pd.read_csv(path.TDP, dtype={
    'V1': str,
    'MaTK': str,
})

def F57C1():
    """
    Get variable UONG PPI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57C1
    """
    df = (TK
        .query('LanTK == 7.0')
        [['V1', 'UongPPI']]
        .rename(columns={
            'V1': 'MANC',
            'UongPPI': 'F57C1'
        })
        .fillna('')
        .replace(label.UONGTHUOC))
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57C1A_LAN1_GIO():
    """
    Get variable PPI LAN 1 GIO

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57C1A_LAN1_GIO
    """
    df = (TK.query('LanTK == 7.0')
        [['V1', 'UongPPIL1Gio']]
        .rename(columns={
            'V1': 'MANC',
            'UongPPIL1Gio': 'F57C1A_LAN1_GIO'
        })
        # .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57C1A_LAN1_PHUT():
    """
    Get variable PPI LAN 1 PHUT

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57C1A_LAN1_PHUT
    """
    df = (TK.query('LanTK == 7.0')
        [['V1', 'UongPPIL1Phut']]
        .rename(columns={
            'V1': 'MANC',
            'UongPPIL1Phut': 'F57C1A_LAN1_PHUT'
        })
        # .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57C1A_LAN2_GIO():
    """
    Get variable PPI LAN 2 GIO

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57C1A_LAN2_GIO
    """
    df = (TK.query('LanTK == 7.0')
        [['V1', 'UongPPIL2Gio']]
        .rename(columns={
            'V1': 'MANC',
            'UongPPIL2Gio': 'F57C1A_LAN2_GIO'
        })
        # .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57C1A_LAN2_PHUT():
    """
    Get variable PPI LAN 2 PHUT

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57C1A_LAN2_PHUT
    """
    df = (TK.query('LanTK == 7.0')
        [['V1', 'UongPPIL2Phut']]
        .rename(columns={
            'V1': 'MANC',
            'UongPPIL2Phut': 'F57C1A_LAN2_PHUT'
        })
        # .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57C2():
    """
    Get variable UONG KS

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57C2
    """
    df = (TK
        .query('LanTK == 7.0')
        [['V1', 'UongKS']]
        .rename(columns={
            'V1': 'MANC',
            'UongKS': 'F57C2'
        })
        .fillna('')
        .replace(label.UONGTHUOC))
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57C2A_LAN1_GIO():
    """
    Get variable KS LAN 1 GIO

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57C2A_LAN1_GIO
    """
    df = (TK.query('LanTK == 7.0')
        [['V1', 'UongKSL1Gio']]
        .rename(columns={
            'V1': 'MANC',
            'UongKSL1Gio': 'F57C2A_LAN1_GIO'
        })
        # .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57C2A_LAN1_PHUT():
    """
    Get variable KS LAN 1 PHUT

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57C2A_LAN1_PHUT
    """
    df = (TK.query('LanTK == 7.0')
        [['V1', 'UongKSL1Phut']]
        .rename(columns={
            'V1': 'MANC',
            'UongKSL1Phut': 'F57C2A_LAN1_PHUT'
        })
        # .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57C2A_LAN2_GIO():
    """
    Get variable KS LAN 2 GIO

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57C2A_LAN2_GIO
    """
    df = (TK.query('LanTK == 7.0')
        [['V1', 'UongKSL2Gio']]
        .rename(columns={
            'V1': 'MANC',
            'UongKSL2Gio': 'F57C2A_LAN2_GIO'
        })
        # .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57C2A_LAN2_PHUT():
    """
    Get variable KS LAN 2 PHUT

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57C2A_LAN2_PHUT
    """
    df = (TK.query('LanTK == 7.0')
        [['V1', 'UongKSL2Phut']]
        .rename(columns={
            'V1': 'MANC',
            'UongKSL2Phut': 'F57C2A_LAN2_PHUT'
        })
        # .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57C4_F57C5():
    """
    Get variable UONG DU CU, DUNG LIEU

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57C4, F57C5
    """
    df = (TK.query('LanTK == 7.0')
        [['V1', 'DuCu' , 'DuLieu']]
        .rename(columns={
            'V1': 'MANC',
            'DuCu': 'F57C4',
            'DuLieu': 'F57C5',
        })
        .replace(label.NHIGIA)
        .fillna('KHONG RO')
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F57C3A_THUOC_F57C3A_TDP():
    """
    Get variable THUOC VA TDP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57C3A_THUOC, F57C3A_TDP
    """
    tdp = (
        TDP.query('STT == 1.0')
    )
    tdp.loc[:, 'Thuoc'] = tdp['Thuoc'].replace(label.THUOC)
    tdp.loc[:, 'TDP'] = tdp['TDP'].replace(label.TRIEUCHUNG)
    df = (TK
        .query('LanTK == 7.0')
        [['V1', 'MaTK']]
        .rename(columns={
            'V1': 'MANC',
        })
        .merge(tdp, how='left', left_on='MaTK', right_on='MaTK')
    )
    df.drop(columns=['V1', 'STT', 'MaTK'], inplace=True)
    df.drop_duplicates(subset=['MANC', 'Thuoc', 'TDP'], inplace=True)
    df = df.fillna('KHONG')
    df.rename(columns={
        'Thuoc': 'F57C3A_THUOC',
        'TDP': 'F57C3A_TDP',
    }, inplace=True)
    return df

def F57C3B_THUOC_F57C3B_TDP():
    """
    Get variable THUOC VA TDP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57C3B_THUOC, F57C3B_TDP
    """
    tdp = (
        TDP.query('STT == 2.0')
    )
    tdp.loc[:, 'Thuoc'] = tdp['Thuoc'].replace(label.THUOC)
    tdp.loc[:, 'TDP'] = tdp['TDP'].replace(label.TRIEUCHUNG)
    df = (TK
        .query('LanTK == 7.0')
        [['V1', 'MaTK']]
        .rename(columns={
            'V1': 'MANC',
        })
        .merge(tdp, how='left', left_on='MaTK', right_on='MaTK')
    )
    df.drop(columns=['V1', 'STT', 'MaTK'], inplace=True)
    df.drop_duplicates(subset=['MANC', 'Thuoc', 'TDP'], inplace=True)
    df = df.fillna('KHONG')
    df.rename(columns={
        'Thuoc': 'F57C3B_THUOC',
        'TDP': 'F57C3B_TDP',
    }, inplace=True)
    return df

def F57C3C_THUOC_F57C3C_TDP():
    """
    Get variable THUOC VA TDP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57C3C_THUOC, F57C3C_TDP
    """
    tdp = (
        TDP.query('STT == 3.0')
    )
    tdp.loc[:, 'Thuoc'] = tdp['Thuoc'].replace(label.THUOC)
    tdp.loc[:, 'TDP'] = tdp['TDP'].replace(label.TRIEUCHUNG)
    df = (TK
        .query('LanTK == 7.0')
        [['V1', 'MaTK']]
        .rename(columns={
            'V1': 'MANC',
        })
        .merge(tdp, how='left', left_on='MaTK', right_on='MaTK')
    )
    df.drop(columns=['V1', 'STT', 'MaTK'], inplace=True)
    df.drop_duplicates(subset=['MANC', 'Thuoc', 'TDP'], inplace=True)
    df = df.fillna('KHONG')
    df.rename(columns={
        'Thuoc': 'F57C3C_THUOC',
        'TDP': 'F57C3C_TDP',
    }, inplace=True)
    return df

def F57C3D_THUOC_F57C3D_TDP():
    """
    Get variable THUOC VA TDP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57C3D_THUOC, F57C3D_TDP
    """
    tdp = (
        TDP.query('STT == 4.0')
    )
    tdp.loc[:, 'Thuoc'] = tdp['Thuoc'].replace(label.THUOC)
    tdp.loc[:, 'TDP'] = tdp['TDP'].replace(label.TRIEUCHUNG)
    df = (TK
        .query('LanTK == 7.0')
        [['V1', 'MaTK']]
        .rename(columns={
            'V1': 'MANC',
        })
        .merge(tdp, how='left', left_on='MaTK', right_on='MaTK')
    )
    df.drop(columns=['V1', 'STT', 'MaTK'], inplace=True)
    df.drop_duplicates(subset=['MANC', 'Thuoc', 'TDP'], inplace=True)
    df = df.fillna('KHONG')
    df.rename(columns={
        'Thuoc': 'F57C3D_THUOC',
        'TDP': 'F57C3D_TDP',
    }, inplace=True)
    return df

def F57C3E_THUOC_F57C3E_TDP():
    """
    Get variable THUOC VA TDP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F57C3E_THUOC, F57C3E_TDP
    """
    tdp = (
        TDP.query('STT == 5.0')
    )
    tdp.loc[:, 'Thuoc'] = tdp['Thuoc'].replace(label.THUOC)
    tdp.loc[:, 'TDP'] = tdp['TDP'].replace(label.TRIEUCHUNG)
    df = (TK
        .query('LanTK == 7.0')
        [['V1', 'MaTK']]
        .rename(columns={
            'V1': 'MANC',
        })
        .merge(tdp, how='left', left_on='MaTK', right_on='MaTK')
    )
    df.drop(columns=['V1', 'STT', 'MaTK'], inplace=True)
    df.drop_duplicates(subset=['MANC', 'Thuoc', 'TDP'], inplace=True)
    df = df.fillna('KHONG')
    df.rename(columns={
        'Thuoc': 'F57C3E_THUOC',
        'TDP': 'F57C3E_TDP',
    }, inplace=True)
    return df


