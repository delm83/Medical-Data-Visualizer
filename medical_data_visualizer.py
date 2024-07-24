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
    # 5 created new dataframe for cat plot
    df_cat = pd.melt(df, id_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke', 'cardio'])


    # 6 grouped and reformatted data and calculated counts
    df_cat = df_cat.groupby(['cardio', 'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke' ]).size().reset_index(name='counts')
    

    # 7 converted data into long format and prouced chart using seaborn catplot method
    df_cat = pd.melt(df_cat, id_vars=['cardio', 'counts'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    chart = sns.catplot(x='variable', y='counts', hue='value', kind='bar', col='cardio', data=df_cat)

    # 8  Stored output in fig variable
    
    fig = chart


    # 9
    fig.savefig('catplot.png')
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
