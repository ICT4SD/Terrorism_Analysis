'''
This module allows users to:
    - select country or the whole world
    - get the overall statistical analyzing information of chosen country
    - visualize the terrorism caused occurrences, casualties, deaths or wounds
    - make 'smooth line' visualization
    - select feature
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
         - ctr_name: country name or "The Whole World"  | str
    Return
         - number of attacks in the chosen country
           across the whole time series
           (years without occurrences are omitted)      | DataFrame
    '''
    df = load_df()
    if ctr_name == 'The Whole World':
        df_all_c = df
    # It is necessary to convert the variable "df_call_c"
    # to the transposing DataFrame format
    # for countries with only one time attack occurrence
    # Otherwise will cause bugs
    else:
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

def df_ctr_all(Country):
    '''
    Retrun a DataFrame from 1970 to 2015
    with features includes:
        - selected ones
        - number of annual attack occurrences
    for the chosen country
    '''
    df1 = df_ctr(Country).groupby('year').sum().reset_index()
    df2 = df_occur_by_ctr_allyears(Country)
    df_merge = pd.merge(df1, df2, on='year', how='outer').fillna(0).sort_values(by='year')
    return df_merge.reset_index().drop(['index'], 1)

def df_ctr(Country):
    if Country == 'The Whole World':
        df_ctr = load_df()
    else:
        df_ctr = load_df()[load_df().country == Country]
    return df_ctr.drop(['eventid', 'latitude', 'longitude'], 1)


def df_ctr_all(Country):
    '''
    Parameter
        Country | str
    Retrun
        a DataFrame (excluding 1993)
    Features
        - year: 1970 to 2015
        - number of kills, wounds and casualties
        - number of annual attack occurrences
    '''
    df1 = df_ctr(Country).groupby('year').sum().reset_index()
    df2 = df_occur_by_ctr_allyears(Country)
    df_merge = pd.merge(df1, df2, on='year', how='outer').fillna(0).sort_values(by='year')
    df = df_merge.reset_index().drop(['index'], 1)
    return drop93(df)  # drop the data-lacking year in the original dataset


def ctr_stats(Country):
    '''
    Return a statistical analyzing table of
    the chosen country's attack data
    across the whole time series | DataFrame
    '''
    ctr_stats = df_ctr_all(Country).describe().T
    ctr_stats['sum'] = df_ctr_all(Country).sum()
    return ctr_stats

def analy_ctr(Country):
    '''
    Return a short statistical analysis of
    the chosen country's attack data
    across the whole time series | String
    '''
    desc = ctr_stats(Country)
    df_ixby_yr = df_ctr_all(Country).set_index('year')
    analysis_str = '\
             Statistical Analysis - Terror Attacks in {}                        \n\
                                  * * *                                         \n\
--------------------------------------------------------------------------------\n\
During the year 1970 to 2015:                                                   \n\
    - The year with the most attacks:        {}                                 \n\
             * {} times of terror attacks in {} in this year                    \n\
    - The year with the most damages:        {}                                 \n\
             * {} suffered the most severe damage by terrorism in this year.    \n\
             * {} people were killed or wounded.                                \n\
             * {} times of terror attacks in {} in this year                    \n\
    - Occurrence of Terror Attacks                                              \n\
             * The total number:              {} \n \
            * The annual average:            {} \n \
            * The standard deviation:        {} \n \
   - Casualties                                 \n \
        1) The total number:                 {} \n \
            * kills                          {} \n \
            * wounds                         {} \n \
        2) The annual average:               {} \n \
            * kills                          {} \n \
            * wounds                         {} \n \
        3) The standard deviation:           {} \n \
            * kills                          {} \n \
            * wounds                         {} \n \
--------------------------------------------------------------------------------\n'
    analysis = analysis_str.format(Country,
                                   np.argmax(df_ixby_yr.occur),               # the year with maximum occurrence
                                   int(df_ixby_yr.occur.max()),               # the maximum occurrence
                                   Country,
                                   np.argmax(df_ixby_yr.casualties),          # the year with maximum casualties
                                   Country,
                                   str(int(desc.loc['casualties', 'max'])),   # the largest number of casualties
                                   str(int(desc.loc['occur', 'max'])),        # the largest number of occurrences
                                   Country,
                                   str(int(desc.loc['occur', 'sum'])),        # total number of attacks
                                   str(int(desc.loc['occur', 'mean'])),       # mean of annual attacks
                                   str(desc.loc['occur', 'std']),             # std of annual attacks
                                   str(int(desc.loc['casualties', 'sum'])),   # total number of casualties
                                   str(int(desc.loc['kills', 'sum'])),        # total number of people killed
                                   str(int(desc.loc['wounds', 'sum'])),       # total number of wounded
                                   str(int(desc.loc['casualties', 'mean'])),  # mean of annual casualties
                                   str(int(desc.loc['kills', 'mean'])),       # mean of annual kills
                                   str(int(desc.loc['wounds', 'mean'])),      # mean of annual wounds
                                   str(desc.loc['casualties', 'std']),        # std of annual casualties
                                   str(desc.loc['kills', 'std']),             # std of annual kills
                                   str(desc.loc['wounds', 'std']),            # std of annual wounds
                                  )
    return analysis

def analy_and_plot(Country, Feature, Color):
    '''
    Parameters
        Country: country name  | str
        Color: color of plot   | str
    '''
    fig = plt.figure(figsize=(15, 5))

    df = df_ctr_all(Country)
    x = df.year
    y = df[Feature]

    # set smooth linestyle
    x = np.array(x)
    y = np.array(y)
    x_smooth = np.linspace(x.min(), x.max(), 900)
    y_smooth = spline(x, y, x_smooth)

    # set the seaborn gird background as white
    sns.set(style="whitegrid")
    plt.plot(x_smooth, y_smooth, '-', color=Color, linewidth=3)
    plt.title('Terror Attack {} in {} (1970-2015)'.format(Feature.capitalize(), Country), size=16)
    plt.xlabel('Year', size=14)
    plt.ylabel('Number of Terror {}'.format(Feature.capitalize()), size=14)
    plt.legend(['Terror {} in {}'.format(Feature.capitalize(), Country)])
    plt.show()
    print(analy_ctr(Country))


def color_picker():
    '''
    Return a color string from users' manual picks
    '''
    clr = ColorPicker(concise=False, description='Color:', value='#41c5f6')
    return clr


def country_picker():
    return Dropdown(options=gtd_country_names(),
                    description='Country:',
                    disabled=False,
                    button_style='info'
                    )


def feature_picker():
    return Dropdown(options={'Occurrence': 'occur',
                             'Casualty': 'casualties',
                             'Death': 'kills',
                             'Wounds': 'wounds'},
                    description='Feature:',
                    disabled=False,
                    button_style='info'
                    )


def Display_Your_Analysis_And_LinePlot():
    '''
    Allow users to interactively customize lineplot
    '''
    try:
        return interact(analy_and_plot,
                        Country=country_picker(),
                        Feature=feature_picker(),
                        Color=color_picker())
    except NoCountryDataError as x:
        print(x)
