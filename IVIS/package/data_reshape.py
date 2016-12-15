'''
Created on Dec 14, 2016

@author: Caroline
'''
import pandas as pd

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