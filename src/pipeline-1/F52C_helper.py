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

def F52C1():
    """
    Get variable UONG PPI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52C1
    """
    df = (TK
        .query('LanTK == 2.0')
        [['V1', 'UongPPI']]
        .rename(columns={
            'V1': 'MANC',
            'UongPPI': 'F52C1'
        })
        .fillna('')
        .replace(label.UONGTHUOC))
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52C1A_LAN1_GIO():
    """
    Get variable PPI LAN 1 GIO

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52C1A_LAN1_GIO
    """
    df = (TK.query('LanTK == 2.0')
        [['V1', 'UongPPIL1Gio']]
        .rename(columns={
            'V1': 'MANC',
            'UongPPIL1Gio': 'F52C1A_LAN1_GIO'
        })
        # .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52C1A_LAN1_PHUT():
    """
    Get variable PPI LAN 1 PHUT

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52C1A_LAN1_PHUT
    """
    df = (TK.query('LanTK == 2.0')
        [['V1', 'UongPPIL1Phut']]
        .rename(columns={
            'V1': 'MANC',
            'UongPPIL1Phut': 'F52C1A_LAN1_PHUT'
        })
        # .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52C1A_LAN2_GIO():
    """
    Get variable PPI LAN 2 GIO

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52C1A_LAN2_GIO
    """
    df = (TK.query('LanTK == 2.0')
        [['V1', 'UongPPIL2Gio']]
        .rename(columns={
            'V1': 'MANC',
            'UongPPIL2Gio': 'F52C1A_LAN2_GIO'
        })
        # .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52C1A_LAN2_PHUT():
    """
    Get variable PPI LAN 2 PHUT

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52C1A_LAN2_PHUT
    """
    df = (TK.query('LanTK == 2.0')
        [['V1', 'UongPPIL2Phut']]
        .rename(columns={
            'V1': 'MANC',
            'UongPPIL2Phut': 'F52C1A_LAN2_PHUT'
        })
        # .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52C2():
    """
    Get variable UONG KS

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52C2
    """
    df = (TK
        .query('LanTK == 2.0')
        [['V1', 'UongKS']]
        .rename(columns={
            'V1': 'MANC',
            'UongKS': 'F52C2'
        })
        .fillna('')
        .replace(label.UONGTHUOC))
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52C2A_LAN1_GIO():
    """
    Get variable KS LAN 1 GIO

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52C2A_LAN1_GIO
    """
    df = (TK.query('LanTK == 2.0')
        [['V1', 'UongKSL1Gio']]
        .rename(columns={
            'V1': 'MANC',
            'UongKSL1Gio': 'F52C2A_LAN1_GIO'
        })
        # .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52C2A_LAN1_PHUT():
    """
    Get variable KS LAN 1 PHUT

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52C2A_LAN1_PHUT
    """
    df = (TK.query('LanTK == 2.0')
        [['V1', 'UongKSL1Phut']]
        .rename(columns={
            'V1': 'MANC',
            'UongKSL1Phut': 'F52C2A_LAN1_PHUT'
        })
        # .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52C2A_LAN2_GIO():
    """
    Get variable KS LAN 2 GIO

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52C2A_LAN2_GIO
    """
    df = (TK.query('LanTK == 2.0')
        [['V1', 'UongKSL2Gio']]
        .rename(columns={
            'V1': 'MANC',
            'UongKSL2Gio': 'F52C2A_LAN2_GIO'
        })
        # .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52C2A_LAN2_PHUT():
    """
    Get variable KS LAN 2 PHUT

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52C2A_LAN2_PHUT
    """
    df = (TK.query('LanTK == 2.0')
        [['V1', 'UongKSL2Phut']]
        .rename(columns={
            'V1': 'MANC',
            'UongKSL2Phut': 'F52C2A_LAN2_PHUT'
        })
        # .fillna(0)
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52C4_F52C5():
    """
    Get variable UONG DU CU, DUNG LIEU

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52C4, F52C5
    """
    df = (TK.query('LanTK == 2.0')
        [['V1', 'DuCu' , 'DuLieu']]
        .rename(columns={
            'V1': 'MANC',
            'DuCu': 'F52C4',
            'DuLieu': 'F52C5',
        })
        .replace(label.NHIGIA)
        .fillna('KHONG RO')
        )
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df

def F52C3A_THUOC_F52C3A_TDP():
    """
    Get variable THUOC VA TDP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52C3A_THUOC, F52C3A_TDP
    """
    tdp = (
        TDP.query('STT == 1.0')
    )
    tdp.loc[:, 'Thuoc'] = tdp['Thuoc'].replace(label.THUOC)
    tdp.loc[:, 'TDP'] = tdp['TDP'].replace(label.TRIEUCHUNG)
    df = (TK
        .query('LanTK == 2.0')
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
        'Thuoc': 'F52C3A_THUOC',
        'TDP': 'F52C3A_TDP',
    }, inplace=True)
    return df

def F52C3B_THUOC_F52C3B_TDP():
    """
    Get variable THUOC VA TDP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52C3B_THUOC, F52C3B_TDP
    """
    tdp = (
        TDP.query('STT == 2.0')
    )
    tdp.loc[:, 'Thuoc'] = tdp['Thuoc'].replace(label.THUOC)
    tdp.loc[:, 'TDP'] = tdp['TDP'].replace(label.TRIEUCHUNG)
    df = (TK
        .query('LanTK == 2.0')
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
        'Thuoc': 'F52C3B_THUOC',
        'TDP': 'F52C3B_TDP',
    }, inplace=True)
    return df

def F52C3C_THUOC_F52C3C_TDP():
    """
    Get variable THUOC VA TDP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52C3C_THUOC, F52C3C_TDP
    """
    tdp = (
        TDP.query('STT == 3.0')
    )
    tdp.loc[:, 'Thuoc'] = tdp['Thuoc'].replace(label.THUOC)
    tdp.loc[:, 'TDP'] = tdp['TDP'].replace(label.TRIEUCHUNG)
    df = (TK
        .query('LanTK == 2.0')
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
        'Thuoc': 'F52C3C_THUOC',
        'TDP': 'F52C3C_TDP',
    }, inplace=True)
    return df

def F52C3D_THUOC_F52C3D_TDP():
    """
    Get variable THUOC VA TDP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52C3D_THUOC, F52C3D_TDP
    """
    tdp = (
        TDP.query('STT == 4.0')
    )
    tdp.loc[:, 'Thuoc'] = tdp['Thuoc'].replace(label.THUOC)
    tdp.loc[:, 'TDP'] = tdp['TDP'].replace(label.TRIEUCHUNG)
    df = (TK
        .query('LanTK == 2.0')
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
        'Thuoc': 'F52C3D_THUOC',
        'TDP': 'F52C3D_TDP',
    }, inplace=True)
    return df

def F52C3E_THUOC_F52C3E_TDP():
    """
    Get variable THUOC VA TDP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F52C3E_THUOC, F52C3E_TDP
    """
    tdp = (
        TDP.query('STT == 5.0')
    )
    tdp.loc[:, 'Thuoc'] = tdp['Thuoc'].replace(label.THUOC)
    tdp.loc[:, 'TDP'] = tdp['TDP'].replace(label.TRIEUCHUNG)
    df = (TK
        .query('LanTK == 2.0')
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
        'Thuoc': 'F52C3E_THUOC',
        'TDP': 'F52C3E_TDP',
    }, inplace=True)
    return df


