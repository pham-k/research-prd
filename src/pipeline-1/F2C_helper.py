import pandas as pd

import path
import label
import util

FORM2 = pd.read_csv(path.FORM2, dtype={
    'V1': str,
})

def F2C1_F2C52():
    """
    Get variables SUA to MAT ONG

    Args:
        None

    Returns:
        DataFrame contains 53 columns MANC, F2C1, ..., F2C52
    """
    s = 'TASua	TASuaChua	TAKem	TAPhoMai	TABo	TATrung	TAThitTrang	TAThitDo	TACa	TATom	TANgheu	TACom	TAXoi	TAHuTiu	TAMi	TABanhMi	TABap	TAMiGoi	TAXucXich	TAThitNguoi	TALapXuong	TAGioThu	TAChaBong	TAKhoBo	TADongHop	TADongLanh	TASocola	TABanh	TAChe	TAKeo	TATraiCayKho	TAKhoaiTayChien	TASnack	TAPizza	TAHamburger	TARauCuSong	TARauCuChin	TATraiCay	TAHat	TANuocCoGa	TATraSua	TACaPhe	TATraDongChai	TANuocDua	TASuaDauNanh	TANuocEp	TaSamBiDao	TANuocTangLuc	TANuocYen	TACaCao	TANguCoc	TAMatOng'
    old_cols = s.split('	')
    new_cols = ['F2C' + str(x) for x in range(1, 53)]
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

def F2C53():
    """
    Get variable THAY DOI THOI QUEN

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2C53
    """
    df = (FORM2[['V1', 'ThayDoiThoiQuen']]
        .rename(columns={
            'V1': 'MANC',
            'ThayDoiThoiQuen': 'F2C53'
        })
        .fillna('KHONG RO')
        .replace(label.NHIGIA))
    return df


