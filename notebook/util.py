import pandas as pd
import numpy as np

def multiple_response(df, prefix='', id_vars='V1', labels={}, wide=False):
    df1 = df.replace(99, np.nan)
    keys = [c for c in df1 if c.startswith(prefix)]
    df2 = pd.melt(df1, id_vars=id_vars, value_vars=keys, value_name=prefix).drop(columns='variable')
    df2 = df2.drop_duplicates([id_vars, prefix])
    df2 = df2[~df2[prefix].isna()].set_index(id_vars)
    if labels:
        df2 = df2.replace(labels)
    if wide:
        dfw = pd.crosstab(df2.index, df2[prefix])
        dfw.index.name = id_vars
        dfw.columns.name = None
        return dfw
    else:
        return df2