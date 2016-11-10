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
    features = ['eventid', 'iyear', 'extended', 'country_txt', 'region_txt', 'city', 
                         'latitude', 'longitude', 'doubtterr', 'multiple', 'success', 'suicide', 
                         'attacktype1', 'attacktype1_txt',
                         'targtype1', 'targtype1_txt',
                         'weaptype1', 'weaptype1_txt',
                         'nkill', 'nwound', 'property']
    return features


def make_list(dataset, col_name):
    new_list = []
    
    for i in dataset[col_name].values.tolist():
        new_list.append(i)
        
    return np.array(new_list)


def make_log_list(dataset, col_name):
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


def group_feature():
    pass


def rank_feature():
    pass

