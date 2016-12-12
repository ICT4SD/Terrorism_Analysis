'''
This modules contains various functions, serving for feature manipulations.
Functions includes:
    - feature selection
    - feature renaming
    - extract unique names
    - convert feature value series into list
    - group columns and other uses

@author: Xianzhi Cao (xc965) and Caroline Roper (cer446)
'''


import numpy as np
import data


def selection():
    '''
    feature selection
    '''
    features = ['eventid', 'iyear', 'country_txt', 'region_txt', \
                'latitude', 'longitude', \
                'attacktype1_txt', 'nkill', 'nwound']
    return features


def feature_names():
    '''
    rename the features for easier re-processing
    '''
    return ['year', 'country', 'region', 'latitude', 'longitude', \
                         'attacktype', 'kills', 'wounds']


def make_array(dataset, col_name):
    '''
    Parameter
        - dataset                                         | DataFrame
        - col_name                                        | str
    Return
        an array of all lists of selected feature values  | np.array
    '''
    new_list = []
    for i in dataset[col_name].values.tolist():
        new_list.append(i)
    return np.array(new_list)


def make_log_array(dataset, col_name):
    '''
    Parameter
        - dataset                                 | DataFrame
        - col_name                                | str
    Return
        values of selected feature (in logarithm) | np.array
    '''
    new_list = []
    for i in dataset[col_name].values.tolist():
        new_list.append(np.log(i))
    return np.array(new_list)

#################################################################################
def find_null(dataset, col_name):
    '''
    NOT USING THIS! CAN I DELETE THIS FUNCTION?~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''
    df_null = dataset[dataset[col_name].isnull()]
    return df_null


def get_rid_of_null(dataset, col_name):
    '''
    NOT USING THIS! CAN I DELETE THIS FUNCTION?~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''
    df_not_null = dataset[dataset[col_name].notnull()]
    return df_not_null


def one_or_more_yr(dataset):
    '''
    NOT USING THIS! CAN I DELETE THIS FUNCTION?~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''
    '''
    This function allow users to choose whether they want to choose:
        1) a single year, or
        2) a multi-year time period
    to present feature occurrence patterns
    '''
    choice = input('To view by a single year, please enter "s"; by multiple continuous years, please enter "m".\nPlease enter: ')
    if choice.lower() == 's':
        return select_by_year(dataset)
    elif choice.lower() == 'm':
        return select_btw_years(dataset)
    else:
        raise ValueError


def select_by_year(dataset):
    '''
    NOT USING THIS! CAN I DELETE THIS FUNCTION?~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''
    '''allow users to select a dataframe by choosing a year between 1970 to 2015'''
    year = input('Please choose a year between 1970 to 2015: ')
    return dataset[(dataset['iyear']) == int(year)]


def select_btw_years(dataset):
    '''
    NOT USING THIS! CAN I DELETE THIS FUNCTION?~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    I CHANGED THIS FUNCTION INTO THE FUNCTION BELOW.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''
    '''allow users to select a dataframe by choosing starting and ending years between 1970 to 2015'''
    year1 = input('Please choose the beginning year between 1970 to 2015: ')
    year2 = input('Please choose the ending year between 1970 to 2015: ')
    return dataset[dataset.iyear.isin(range(int(year1), int(year2)+1))]
#################################################################################

def df_sel_btw_years(year_interval):
    '''
    Parameter
        - year_interval: Time Interval           |   tuple
    Return
        - all data in the chosen time interval   |   DataFrame
    '''
    gt_df = data.load_df()
    df_intv = gt_df[(gt_df.year <= year_interval[1]) & (gt_df.year >= year_interval[0])]
    return df_intv


def make_five_year_start(dataset):
    '''
    Parameter
        - dataset | DataFrame
    periods are partitioned by every 5 years
        eg. period 1990 means from year 1990 to year 1994
    returns a Series
    '''
    dataset['period'] = [int(i/5)*5 for i in dataset.year]
    return dataset['period']


### Caroline's functions

def create_counts(data, group_by_columns, column_to_count):
    '''Takes a list of column names and a column to count and counts rows by those column name, including nulls'''
    all_columns = group_by_columns + [column_to_count]
    data = data.loc[:,all_columns].fillna(value = 1)
    grouped = data.groupby(group_by_columns)
    return grouped.count()

def unstack_table(data):
    '''Unstacks data until there's only one row index remaining'''
    data = data.fillna(0)
    i = 0
    while i < data.index.nlevels:
        data = data.unstack()
        i = i + 1
    return data

def remove_zeros(series):
    return series[series > 0]

def convert_series(series, label):
    '''Takes a series and label for the series' values, returns df with 2 columns: the series' row index, & the series' values'''
    converted = pd.DataFrame(series)
    converted.columns = [label]
    converted.reset_index(level=0, inplace=True)
    return converted

def group_by_columns(data, group_by_columns, column_to_agg):
    '''Takes a list of column names and a column to count and counts rows by those column name, including nulls'''
    all_columns = group_by_columns + [column_to_agg]
    data.loc[:, column_to_agg] = data.loc[:, column_to_agg].fillna(value=0)
    data = data.loc[:,all_columns]
    grouped = data.groupby(group_by_columns)
    return grouped

def sum_by_groups(grouped):
    '''Takes output of group function and sums data'''
    sums = grouped.sum().dropna()
    sums.columns = ['sum']
    return sums

def count_by_groups(grouped):
    '''Takes output of group function and counts data'''
    counts = grouped.count().dropna()
    counts.columns = ['count']
    return counts
### Caroline's make_five_year_start function goes here :)
### Viola, where did your "make 5" function go?
### It's right above your codes :DDD
