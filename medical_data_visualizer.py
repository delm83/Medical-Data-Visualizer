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

#cleaning data by filtering out incorrect data
df = df[df['ap_lo'] <= df['ap_hi']]
df = df[df['height'] >= df['height'].quantile(0.025)]
df = df[df['height'] <= df['height'].quantile(0.975)]
df = df[df['weight'] >= df['weight'].quantile(0.025)]
df = df[df['weight'] <= df['weight'].quantile(0.975)]

# 4
def draw_cat_plot():
    # 5 created new dataframe for cat plot in long format
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # 6 grouped and reformatted data and calculated counts
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'])['variable'].count().reset_index(name='total')
    
    # 7 prouced chart using seaborn catplot method
    chart = sns.catplot(x='variable', y='total', hue='value', kind='bar', col='cardio', data=df_cat, errorbar=None)

    #8  Stored output in fig variable
    
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
