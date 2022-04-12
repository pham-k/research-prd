import pandas as pd

import path
import label
import util

FORM2 = pd.read_csv(path.FORM2, dtype={
    'V1': str,
})

def F2H1A():
    """
    Get variable NOI CU TRU LAU NHAT - TINH

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H1A
    """
    df = (FORM2[['V1', 'CuTruTinh']]
        .rename(columns={
            'V1': 'MANC',
            'CuTruTinh': 'F2H1A'
        })
        .fillna('KHONG RO')
        .replace(label.TINHTHANH)
        )
    return df

def F2H1B():
    """
    Get variable NOI CU TRU LAU NHAT - QUAN

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H1B
    """
    df = (FORM2[['V1', 'CuTruQuan']]
        .rename(columns={
            'V1': 'MANC',
            'CuTruQuan': 'F2H1B'
        })
        .fillna('KHONG RO')
        .replace(label.QUANHUYEN)
        )
    return df

def F2H2():
    """
    Get variable DIEN TICH

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H2
    """
    df = (FORM2[['V1', 'DienTich']]
        .rename(columns={
            'V1': 'MANC',
            'DienTich': 'F2H2'
        })
        .fillna('KHONG RO')
        )
    return df

def F2H3():
    """
    Get variable LOAI NHA

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H3
    """
    df = (FORM2[['V1', 'LoaiNha']]
        .rename(columns={
            'V1': 'MANC',
            'LoaiNha': 'F2H3'
        })
        .fillna('KHONG RO')
        .replace(label.LOAINHA)
        )
    return df

def F2H4():
    """
    Get variable NHA MAY TANG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H4
    """
    df = (FORM2[['V1', 'SoTang']]
        .rename(columns={
            'V1': 'MANC',
            'SoTang': 'F2H4'
        })
        .fillna('KHONG RO')
        )
    return df

def F2H5():
    """
    Get variable MAT TIEN

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H5
    """
    df = (FORM2[['V1', 'MatTien']]
        .rename(columns={
            'V1': 'MANC',
            'MatTien': 'F2H5'
        })
        .fillna('KHONG RO')
        .replace(label.MATTIEN)
        )
    return df

def F2H6():
    """
    Get variable MAY LANH

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H6
    """
    df = (FORM2[['V1', 'MayLanh']]
        .rename(columns={
            'V1': 'MANC',
            'MayLanh': 'F2H6'
        })
        .fillna('KHONG RO')
        .replace(label.NHIGIA)
        )
    return df

def F2H7():
    """
    Get variable NHA VE SINH RIENG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H7
    """
    df = (FORM2[['V1', 'NhaVSRieng']]
        .rename(columns={
            'V1': 'MANC',
            'NhaVSRieng': 'F2H7'
        })
        .fillna('KHONG RO')
        .replace(label.NHIGIA)
        )
    return df

def F2H8_KHONGPHONG():
    """
    Get variable KHONG PHONG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H8_KHONGPHONG
    """
    df = (FORM2[['V1', 'KhongPhong']]
        .rename(columns={
            'V1': 'MANC',
            'KhongPhong': 'F2H8_KHONGPHONG'
        })
        .fillna(0)
        )
    return df

def F2H8_PHONGKHACH():
    """
    Get variable PHONG KHACH

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H8_PHONGKHACH
    """
    df = (FORM2[['V1', 'PhongKhach']]
        .rename(columns={
            'V1': 'MANC',
            'PhongKhach': 'F2H8_PHONGKHACH'
        })
        .fillna(0)
        )
    return df

def F2H8_PHONGNGU():
    """
    Get variable PHONG NGU

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H8_PHONGNGU
    """
    df = (FORM2[['V1', 'PhongNgu']]
        .rename(columns={
            'V1': 'MANC',
            'PhongNgu': 'F2H8_PHONGNGU'
        })
        .fillna(0)
        )
    return df

def F2H8_NHABEP():
    """
    Get variable NHA BEP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H8_NHABEP
    """
    df = (FORM2[['V1', 'NhaBep']]
        .rename(columns={
            'V1': 'MANC',
            'NhaBep': 'F2H8_NHABEP'
        })
        .fillna(0)
        )
    return df

def F2H8_NHAVSNHATAM():
    """
    Get variable NHA VE SINH NHA TAM CHUNG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H8_NHAVSNHATAM
    """
    df = (FORM2[['V1', 'NhaVSChung']]
        .rename(columns={
            'V1': 'MANC',
            'NhaVSChung': 'F2H8_NHAVSNHATAM'
        })
        .fillna(0)
        )
    return df

def F2H8_NHATAMRIENG():
    """
    Get variable NHA TAM RIENG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H8_NHATAMRIENG
    """
    df = (FORM2[['V1', 'NhaTamRieng']]
        .rename(columns={
            'V1': 'MANC',
            'NhaTamRieng': 'F2H8_NHATAMRIENG'
        })
        .fillna(0)
        )
    return df

def F2H8_NHAVSRIENG():
    """
    Get variable NHA VE SINH RIENG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H8_NHAVSRIENG
    """
    df = (FORM2[['V1', 'NhaVSRieng2']]
        .rename(columns={
            'V1': 'MANC',
            'NhaVSRieng2': 'F2H8_NHAVSRIENG'
        })
        .fillna(0)
        )
    return df

def F2H8_PHONGTHO():
    """
    Get variable PHONG THO

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H8_PHONGTHO
    """
    df = (FORM2[['V1', 'PhongTho']]
        .rename(columns={
            'V1': 'MANC',
            'PhongTho': 'F2H8_PHONGTHO'
        })
        .fillna(0)
        )
    return df

def F2H8_NHAKHO():
    """
    Get variable NHA KHO

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H8_NHAKHO
    """
    df = (FORM2[['V1', 'NhaKho']]
        .rename(columns={
            'V1': 'MANC',
            'NhaKho': 'F2H8_NHAKHO'
        })
        .fillna(0)
        )
    return df

def F2H8_NHAXE():
    """
    Get variable NHA XE

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H8_NHAXE
    """
    df = (FORM2[['V1', 'NhaXe']]
        .rename(columns={
            'V1': 'MANC',
            'NhaXe': 'F2H8_NHAXE'
        })
        .fillna(0)
        )
    return df

def F2H8_PHONGHOC():
    """
    Get variable PHONG HOC

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H8_PHONGHOC
    """
    df = (FORM2[['V1', 'PhongHoc']]
        .rename(columns={
            'V1': 'MANC',
            'PhongHoc': 'F2H8_PHONGHOC'
        })
        .fillna(0)
        )
    return df

def F2H9():
    """
    Get variable LOAI NHA VE SINH

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H9
    """
    cols = ['LoaiNhaVS1', 'LoaiNhaVS2', 'LoaiNhaVS3', 'LoaiNhaVS4', 'LoaiNhaVS5', ]
    df = (FORM2[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.LOAINHAVESINH))
    
    df['F2H9'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F2H10():
    """
    Get variable NUOC SINH HOAT

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H10
    """
    cols = ['NuocSinhHoat1', 'NuocSinhHoat2', 'NuocSinhHoat3', 'NuocSinhHoat4', 'NuocSinhHoat5', ]
    df = (FORM2[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.NUOCSINHHOAT))
    
    df['F2H10'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F2H11():
    """
    Get variable NUOC NAU AN

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H11
    """
    cols = ['NuocNauAn1', 'NuocNauAn2', 'NuocNauAn3', 'NuocNauAn4', 'NuocNauAn5', ]
    df = (FORM2[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.NUOCNAUAN))
    
    df['F2H11'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F2H12():
    """
    Get variable NUOC UONG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H12
    """
    cols = ['NuocUong1', 'NuocUong2', 'NuocUong3', 'NuocUong4', 'NuocUong5', ]
    df = (FORM2[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.NUOCUONG))
    
    df['F2H12'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F2H13():
    """
    Get variable VAT NUOI

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H13
    """
    cols = ['VatNuoi1', 'VatNuoi2', 'VatNuoi3', 'VatNuoi4', 'VatNuoi5', ]
    df = (FORM2[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.VATNUOI))
    
    df['F2H13'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F2H14():
    """
    Get variable NHA NGAP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H14
    """
    df = (FORM2[['V1', 'NhaNgap']]
        .rename(columns={
            'V1': 'MANC',
            'NhaNgap': 'F2H14'
        })
        .fillna('')
        .replace(label.TANSUAT))
    
    return df

def F2H15():
    """
    Get variable NGUOI HUT THUOC

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H15
    """
    cols = ['NguoiHutThuoc1', 'NguoiHutThuoc2', 'NguoiHutThuoc3', 'NguoiHutThuoc4', 
            'NguoiHutThuoc5', 'NguoiHutThuoc6', 'NguoiHutThuoc7', 'NguoiHutThuoc8', ]
    df = (FORM2[['V1'] + cols]
        .rename(columns={
            'V1': 'MANC',
        })
        .fillna('')
        .replace(label.SONGCHUNG))
    
    df['F2H15'] = df.apply(util.concatenate_columns, axis=1)
    df.drop(columns=cols, inplace=True)
    return df

def F2H16():
    """
    Get variable HAI LONG

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H16
    """
    df = (FORM2[['V1', 'HaiLong']]
        .rename(columns={
            'V1': 'MANC',
            'HaiLong': 'F2H16'
        })
        .fillna('KHONG RO')
        )
    
    return df

def F2H17():
    """
    Get variable CHI TIEU

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H17
    """
    df = (FORM2[['V1', 'ChiTieu']]
        .rename(columns={
            'V1': 'MANC',
            'ChiTieu': 'F2H17'
        })
        .fillna('KHONG RO')
        )
    
    return df

def F2H18():
    """
    Get variable THU NHAP

    Args:
        None

    Returns:
        DataFrame contains 2 columns MANC, F2H18
    """
    df = (FORM2[['V1', 'ThuNhap']]
        .rename(columns={
            'V1': 'MANC',
            'ThuNhap': 'F2H18'
        })
        .fillna('KHONG RO')
        )
    
    return df
