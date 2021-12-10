import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pylab as plt

def load_and_process(df):
    df1=(
        pd.read_csv("D:\charts.csv.zip")
        .columns
        .drop(df.index[160000:328487])
        .nunique(axis=0)
        .info()
    )
    df2=(
        df1
        .plot(kind='scatter', x='rank', y='weeks-on-board')
        .plot(kind='scatter', x='peak-rank', y='weeks-on-board')
        .max()
        ['artist'].value_counts().idxmax()
        ['song'].value_counts().idxmax()
    )
    return df2