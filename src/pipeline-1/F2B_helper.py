import pandas as pd

import path
import label
import util

FORM2 = pd.read_csv(path.FORM2, dtype={
    'V1': str,
})

def F2B1_F2B11():
    """
    Get variables THUC AN NONG to AN VAT

    Args:
        None

    Returns:
        DataFrame contains 12 columns MANC, F2B1, ..., F2B11
    """
    s = 'TANong	TAChua	TACay	TASong	TANuong	TAHanhToi	TADuongPho	TAHangQuan	TANhanh	AnBoc	AnVat'
    old_cols = s.split('	')
    new_cols = ['F2B' + str(x) for x in range(1, 12)]
    columns = dict(zip(old_cols, new_cols))
    
    df = (FORM2[['V1'] + old_cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .rename(columns=columns)
        .fillna('KHONG RO')
        .replace(label.TANSUATTUAN))
    # print(df.info())
    return df

def F2B12_F2B15():
    """
    Get variables DUNG CHUNG to GAP/ MUC THUC AN CHUNG

    Args:
        None

    Returns:
        DataFrame contains 5 columns MANC, F2B12, ..., F2B15
    """
    s = 'AnChung	UongChung	ChamChung	GapChung'
    old_cols = s.split('	')
    new_cols = ['F2B' + str(x) for x in range(12, 16)]
    columns = dict(zip(old_cols, new_cols))
    
    df = (FORM2[['V1'] + old_cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .rename(columns=columns)
        .fillna('KHONG RO')
        .replace(label.NHIGIA))
    # print(df.info())
    return df


