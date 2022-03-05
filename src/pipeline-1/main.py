import pandas as pd
import F2Z_helper as F2Z
import F2A_helper as F2A
import F2B_helper as F2B

def main():
    print("Execute pipeline 1")
    df = (F2Z.NGAY()
        .merge(F2Z.MAHS())
        .merge(F2Z.F2Z1())
        .merge(F2Z.F2Z2())
        .merge(F2Z.F2Z3())
        .merge(F2Z.F2Z4_1())
        .merge(F2Z.F2Z4_2())
        .merge(F2Z.F2Z5_1())
        .merge(F2Z.F2Z5_2())
        .merge(F2A.F2A1())
        .merge(F2A.F2A2())
        .merge(F2A.F2A3())
        .merge(F2A.F2A4())
        .merge(F2A.F2A5())
        .merge(F2A.F2A6())
        .merge(F2A.F2A7())
        .merge(F2A.F2A8())
        .merge(F2A.F2A9())
        .merge(F2A.F2A10())
        .merge(F2A.F2A11())
        .merge(F2B.F2B1_F2B11())
        .merge(F2B.F2B12_F2B15())
    )
    # view sample
    cols = [0] + list(range(32, 36))
    print(df.iloc[:, cols].info())
    print(df.iloc[:, cols].sample(5))
    # print(df.query('F2A5 != "KHONG"'))
    # print(df[df['F2A11'] == 'KHONG RO'])


if __name__ == "__main__":
    main()
