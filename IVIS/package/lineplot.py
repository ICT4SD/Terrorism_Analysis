'''
This module allows users to:
    - select country or the whole world
    - visualize the terror attack occurrences
    - use scipy and seaborn to make 'smooth line' visualization
    - get the overview statistical analyzing information of chosen country
    - customize color

@author: Xianzhi Cao (xc965)
'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import spline
from ipywidgets import *
from data import *


def set_as_index(df, colname):
    '''
    use this function to set DataFrame's feature,
    such as 'year' and 'country', as index
    '''
    return df.set_index(colname)

def df_occur_by_ctr(ctr_name):
    '''
    Parameter
         - ctr_name: country name | str
    Return
         - number of attack occurrences in the chosen country
           across the whole time series
           (years without occurrences are omitted) | DataFrame
    '''
    df = load_df()
    # It is necessary to convert the variable "df_call_c"
    # to the transposing DataFrame format
    # for countries with only one time attack occurrence
    # Otherwise will cause bugs
    df_all_c = set_as_index(df, 'country').ix[ctr_name]
    if type(df_all_c) == pd.Series:
        df_all_c = pd.DataFrame(df_all_c).T
    df_yr = pd.DataFrame(df_all_c.groupby('year').count().eventid)
    df_yr.columns = ['occur']
    return df_yr.reset_index()

def df_occur_by_ctr_allyears(ctr_name):
    '''
    Parameter
         - ctr_name: country name | str
    Return
         - number of attack occurrences in the chosen country
           across the whole time series
           (years without occurrences are not omitted) | DataFrame
    '''
    dic_yr = {'year': list(range(1970, 2016)),
              'null': np.zeros((2015-1970)+1, dtype=int)}
    df_years = pd.DataFrame(dic_yr)
    df_full_yr = pd.merge(df_years, df_occur_by_ctr(ctr_name),
                          on='year', how='outer').fillna(0)
    return df_full_yr[['year', 'occur']]


def gtd_country_names():
    '''
    return a list of all the country names
    started with 'The Whole World'
    '''
    all_ctr = sorted(load_df().country.unique())
    all_ctr.insert(0, 'The Whole World')
    return all_ctr


def drop93(df):
    '''
    Parameter
        - df : DataFrame  | DataFrame
    Return
        a DataFrame without the year 1993,
        since there is no data in the GT Database
    '''
    return df[df.year != 1993]


def world_stats():
    '''
    Return a statistical analyzing table of
    all countries' attack data
    across the whole time series | DataFrame
    '''
    stats_list = ['count', 'sum', 'mean', 'max']
    feature_list = ['year', 'kills', 'wounds', 'casualties']
    world_stats = load_df()[feature_list].groupby('year').agg(stats_list).reset_index()
    return world_stats


def plot_line(Country, Color):
    '''
    Parameters
        Country: country name | str
        Color: color of plot   | str
    '''
    fig = plt.figure(figsize=(15, 6))

    if Country == 'The Whole World':
        x = world_stats().year
        y = world_stats().casualties['count']
    elif Country not in gtd_country_names():
        raise NoCountryDataError
    else:
        df_all = df_occur_by_ctr_allyears(Country)
        df = drop93(df_all)  # drop the data-lacking year in the original dataset
        x = df.year
        y = df.occur
    # set smooth linestyle
    x = np.array(x)
    y = np.array(y)
    x_smooth = np.linspace(x.min(), x.max(), 900)
    y_smooth = spline(x, y, x_smooth)
    # set the seaborn gird background as white
    sns.set(style="whitegrid")
    plt.plot(x_smooth, y_smooth, '-', color=Color, linewidth=3)
    plt.title('Terrorist Attack Occurrence in {} (1970-2015)'.format(Country))
    plt.xlabel('Year', size=14)
    plt.ylabel('Number of Attack Occurrences', size=14)
    plt.legend(['Terror Attack Occurance in {}'.format(Country)])
    plt.show()


def color_picker():
    '''
    Return a color string from users' manual picks
    '''
    clr = ColorPicker(concise=False, description='Color', value='#ea5f58')
    return clr


def Display_Your_LinePlot():
    '''
    Allow users to interactively customize lineplot
    '''
    try:
        return interact(plot_line,
                        Country=gtd_country_names(),
                        Color=color_picker())
    except NoCountryDataError as x:
        print(x)
