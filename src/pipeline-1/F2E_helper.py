import pandas as pd

import path
import label
import util

FORM2 = pd.read_csv(path.FORM2, dtype={
    'V1': str,
})

def F2E1():
    """
    Get variable NGU CHUNG VOI BA ME

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2E1
    """
    df = (FORM2[['V1', 'NguVoiBaMe']]
        .rename(columns={
            'V1': 'MANC',
            'NguVoiBaMe': 'F2E1'
        })
        .fillna('KHONG RO')
        .replace(label.NHIGIA))
    return df

def F2E2():
    """
    Get variable NGU CHUNG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2E2
    """
    cols = ['NguVoi1', 'NguVoi2', 'NguVoi3', 'NguVoi4', 'NguVoi5',]
    df = (FORM2[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.NGUVOI))
    
    df['F2E2'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F2E3():
    """
    Get variable NGU RIENG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2E3
    """
    df = (FORM2[['V1', 'NguRieng', 'NguRiengTuoi']]
        .rename(columns={
            'V1': 'MANC',
        }))
    
    df['NguRieng'] = df['NguRieng'].replace(label.NHIGIA)
    
    def f(row):
        if pd.notna(row[2]):
            return str(row[2])
        elif row[1] == label.NHIGIA[1] and pd.isna(row[2]):
            return 'CO NHUNG KHONG RO TUOI'
        elif row[1] == label.NHIGIA[0] and pd.isna(row[2]):
            return 'KHONG'
        else:
            return 'PENDING'
    
    df['F2E3'] = df.apply(f, axis=1)
    df.drop(columns=['NguRieng', 'NguRiengTuoi'], inplace=True)
    return df

def F2E4():
    """
    Get variable NGU CHUNG VOI VAT NUOI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2E4
    """
    df = (FORM2[['V1', 'NguVoiPet']]
        .rename(columns={
            'V1': 'MANC',
            'NguVoiPet': 'F2E4'
        })
        .fillna('KHONG RO')
        .replace(label.TANSUAT))
    return df

