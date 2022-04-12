import pandas as pd

import path
import label
import util

FORM2 = pd.read_csv(path.FORM2, dtype={
    'V1': str,
})

def F2F2():
    """
    Get variable SI SO LOP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2F2
    """
    df = (FORM2[['V1', 'SiSoLop']]
        .rename(columns={
            'V1': 'MANC',
            'SiSoLop': 'F2F2'
        })
        .fillna('KHONG RO')
        )
    return df

def F2F3_F2F7():
    """
    Get variables DUNG SUAT AN TRUA to NGU TRUA

    Args:
        None

    Returns:
        DataFrame contains 6 columns MANC, F2F3, ..., F2F7
    """
    s = 'TruongAnTrua	TruongUong	TruongTieuTien	TruongDaiTien	TruongNgu'
    old_cols = s.split('	')
    new_cols = ['F2F' + str(x) for x in range(3, 8)]
    columns = dict(zip(old_cols, new_cols))
    
    df = (FORM2[['V1'] + old_cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .rename(columns=columns)
        .fillna('KHONG RO')
        .replace(label.NHIGIA))
    return df


