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
    # 5 created new dataframe for cat plot using melt to reformat it from wide to long format
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # 6 grouped and reformatted data and calculated counts
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'])['variable'].count().reset_index(name='total')
    
    # 7 prouced chart using seaborn catplot method
    chart = sns.catplot(x='variable', y='total', hue='value', kind='bar', col='cardio', data=df_cat, errorbar=None).fig

    #8  Stored output in fig variable
    fig = chart

    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11 cleaning dataframe by filtering out incorrect data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) 
    & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) 
    & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12 calculate correlation matrix
    corr = round(df_heat.corr(), 1)

    # 13 Data masking is a technique used to selectively highlight or hide certain data points based on specific conditions. This can help focus attention on particular areas of interest or patterns within the dataset.
    # trui returns a copy of an array with the elements below the k-th diagonal zeroed (upper triangle of array) and ones_like is used to get an array of ones with the same shape and type as an existing array
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14 Setting up the matplotlib figure
    fig, ax = plt.subplots()

    # 15 plot correlation matrix using seaborn heatmap.  With robust true the colormap (legend) range is computed with robust quantiles instead of the extreme values with annot true data values are written in each cell fmt is set to output data to 1 decimal place cmap set to coolwarm to represent temperature scale and cbar_kws is used to shrink the colorbar(legend) by half
    sns.heatmap(corr, robust=True, annot=True, mask = mask, ax = ax, fmt='.1f', cmap='coolwarm', cbar_kws={'shrink': 0.5})

    # prevent labels being cut off in png
    plt.tight_layout()

    # 16
    fig.savefig('heatmap.png')
    return fig
