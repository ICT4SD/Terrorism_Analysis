"""
add hovering descriptions of specific attack information.
"""




'''
Created on Nov 7, 2016

We should write all the procedures, including packing installing, data downloading, etc. into the user's manual;
we also need to write specific guidance of all the functions about the program.

Write clean code, look at the documentations and use multiple functions to show our capabilities.

Important: We should put emphasis on the data ANALYSING part as well!

Finally, test the program, and make sure all tests are passed.
Test modules should be put under the top level of the project directory.

@author: Viola
'''
import numpy as np


def selection():
    features = ['eventid', 'iyear', 'country_txt', 'region_txt','latitude', 'longitude', \
                         'attacktype1_txt', 'nkill', 'nwound']
    return features


def feature_names():
    return ['year', 'country', 'region', 'latitude', 'longitude', \
                         'attacktype', 'kills', 'wounds']


def make_list(dataset, col_name):
    '''extract a list of values in selected feature and return as a numpy array'''
    new_list = []
    for i in dataset[col_name].values.tolist():
        new_list.append(i)
    return np.array(new_list)


def make_log_list(dataset, col_name):
    '''extract a list of values in logarithm in selected feature and return as a numpy array'''
    new_list = []
    for i in dataset[col_name].values.tolist():
        new_list.append(np.log(i))
    return np.array(new_list)


def find_null(dataset, col_name):
    df_null = dataset[dataset[col_name].isnull()]
    return df_null


def get_rid_of_null(dataset, col_name):
    df_not_null = dataset[dataset[col_name].notnull()]
    return df_not_null


def one_or_more_yr(dataset):
    """
    This function allow users to choose whether they want to choose:
        1) a single year, or
        2) a multi-year time period
    to present feature occurrence patterns
    """
    choice = input('To view by a single year, please enter "s"; by multiple continuous years, please enter "m".\nPlease enter: ')
    if choice.lower() == 's':
        return select_by_year(dataset)
    elif choice.lower() == 'm':
        return select_btw_years(dataset)
    else:
        raise ValueError


def select_by_year(dataset):
    '''allow users to select a dataframe by choosing a year between 1970 to 2015'''
    year = input('Please choose a year between 1970 to 2015: ')
    return dataset[(dataset['iyear']) == int(year)]


def select_btw_years(dataset):
    '''allow users to select a dataframe by choosing starting and ending years between 1970 to 2015'''
    year1 = input('Please choose the beginning year between 1970 to 2015: ')
    year2 = input('Please choose the ending year between 1970 to 2015: ')
    return dataset[dataset.iyear.isin(range(int(year1), int(year2)+1))]


def make_five_year_start(dataset):
    # periods are partitioned by every 5 years
    # eg. period 1990 means from year 1990 to year 1994
    # returns a Series
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


def choose_feature(dataset, col_name):
    '''
    allow users  to choose a feature type to present on the map
    the value will be presented in logarithm
    '''
    feature_shown = make_log_list(dataset, col_name)
    return feature_shown


def group_feature():
    pass


def rank_feature():
    pass
