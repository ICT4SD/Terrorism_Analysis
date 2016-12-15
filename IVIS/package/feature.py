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
import pandas as pd


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


def make_list(dataset, col_name):
    '''
    Parameter
        - dataset                    | DataFrame
        - col_name                   | str
    Return
        values of selected feature   | np.array
    '''
    new_list = []
    for i in dataset[col_name].values.tolist():
        new_list.append(i)
    return np.array(new_list)


def make_log_list(dataset, col_name):
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

def create_range(series_to_group, group_size):
    '''Turns a series into groups of a specified size'''
    bins = np.arange(min(series_to_group) - group_size, max(series_to_group) + group_size, group_size)
    ranges = pd.cut(series_to_group, bins)
    ranges.name = series_to_group.name + ' ranges'
    return ranges

def replace_series_with_range(data, series_to_group, group_size):
    '''Removes year column and merges range column'''
    ranges = create_range(series_to_group, group_size)
    data_replaced = pd.concat([data, pd.DataFrame(ranges)], axis = 1).drop(series_to_group.name, 1)
    return data_replaced
