'''
This module converts the excel dataset file into the csv file, processes the dataset with selected features,
get new dataframe, and store the new dataframe in csv file.

The whole process simply the original dataset and shortens the loading time for future data manipulations.
'''

import pandas as pd
import re
import json
from feature import *


path_excelfile = '../data/globalterrorismdb_0616dist.xlsx'

def excel_to_csv(path_excelfile):
    whole = pd.read_excel(path_excelfile)
    whole.to_csv('gtd_wholedata.csv')


def make_df():
    '''
    make the DataFrame with selected features
    rename the features
    add "casualties" as sum of "kills" and "wounds"
    '''
    df = pd.read_csv('gtd_wholedata.csv', usecols=selection(),
                         low_memory=False, index_col=0)
    df.columns = feature_names()
    df['casualties'] = df.kills + df.wounds
    return df


def save_df_csv():
    '''make a csv file with all selected features'''
    return make_df().to_csv('gtd_wholedata_selected.csv')


def load_df():
    '''load the DataFrame with selected features'''
    df = pd.read_csv('gtd_wholedata_selected.csv').fillna(0)
    return df

def df_year_idx():
    '''return the DataFrame with selected features, indexed by years'''
    return pd.read_csv('gtd_wholedata_selected.csv', index_col='year').fillna(0)


def load_json_file(filepath):
    if not re.match(r'.+\.(json){1}$', filepath):
        raise LoadJsonError
    else:
        with open('countries.geo.json') as json_data:
            j = json.load(json_data)
    return j
