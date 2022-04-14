import pandas as pd

import path
import label
import util

TK = pd.read_csv(path.TK, dtype={
    'V1': str,
})

def F55D1_F55D7():
    """
    Get variables QUEN THUOC, ..., PHIEN HA

    Args:
        None

    Returns:
        DataFrame contains 53 columns MANC, F55D1, ..., F55D7
    """
    s = 'QuenThuoc	KhongUong	GiamLieu	DLQuenThuoc	UongHomQua	BotTCNgung	PhienHa'
    old_cols = s.split('	')
    new_cols = ['F55D' + str(x) for x in range(1, 8)]
    columns = dict(zip(old_cols, new_cols))
    
    df = (TK.query('LanTK == 5.0')
        [['V1'] + old_cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .rename(columns=columns)
        .fillna('KHONG RO')
        .replace(label.NHIGIA))
    df.drop_duplicates(subset=['MANC'], inplace=True)
    # print(df.info())
    return df

def F55D8():
    """
    Get variable KHO KHAN GHI NHO LICH

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F55D8
    """
    df = (TK
        .query('LanTK == 5.0')
        [['V1', 'NhoLich_KhoKhan']]
        .rename(columns={
            'V1': 'MANC',
            'NhoLich_KhoKhan': 'F55D8'
        })
        .fillna('')
        .replace(label.TANSUAT))
    df.drop_duplicates(subset=['MANC'], inplace=True)
    return df


