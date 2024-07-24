import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2 added overweight column, value is 1 (overweight) if BMI >25 else 0
df['overweight'] = np.where(df['weight'].values/(df['height'].values/100)**2 > 25, 1, 0)

# 3 normalized data by changing cholestorol & gluc values to 1 (bad) if current value is > 1 else 0 (good)
df[['cholesterol', 'gluc']] = np.where(df[['cholesterol', 'gluc']].values > 1, 1, 0)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # 6
    #df_cat = None
    

    # 7



    # 8
    #fig = df_cat


    # 9
    #fig.savefig('catplot.png')
    print(df_cat)
    return df


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    #fig, ax = None

    # 15



    # 16
    #fig.savefig('heatmap.png')
    #return fig
