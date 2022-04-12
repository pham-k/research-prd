import pandas as pd

import path
import label
import util

FORM2 = pd.read_csv(path.FORM2, dtype={
    'V1': str,
})

def F2D1_F2D7():
    """
    Get variables RUA TAY XA BONG to DANH RANG

    Args:
        None

    Returns:
        DataFrame contains 9 columns MANC, F2D1, ..., F2D7
    """
    s = 'RuaTayTruocAn	RuaTaySauVS	DiChanDat	DungChungKhan	DungChungBC	CanMongTay	DanhRang'
    old_cols = s.split('	')
    new_cols = ['F2D' + str(x) for x in range(1, 8)]
    columns = dict(zip(old_cols, new_cols))
    
    df = (FORM2[['V1'] + old_cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .rename(columns=columns)
        .fillna('KHONG RO')
        .replace(label.TANSUAT))
    # print(df.info())
    return df

def F2D8():
    """
    Get variable LAU RUA HAU MON

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2D8
    """
    cols = ['LauRuaHM1', 'LauRuaHM2', 'LauRuaHM3', 'LauRuaHM4', 'LauRuaHM5',]
    df = (FORM2[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.LAURUAHAUMON))
    
    df['F2D8'] = df.apply(util.concatenate_columns, axis=1)
    # print(df.columns)
    df.drop(columns=cols, inplace=True)
    return df

