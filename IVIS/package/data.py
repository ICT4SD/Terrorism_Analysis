'''
This module converts the excel dataset file into the csv file, processes the dataset with selected features,
get new dataframe, and store the new dataframe in csv file.

The whole process simply the original dataset and shortens the loading time for future data manipulations.
'''

import pandas as pd
import numpy as np
from feature import *


path_excelfile = '../data/globalterrorismdb_0616dist.xlsx'

def excel_to_csv(path_excelfile):
    whole = pd.read_excel(path_excelfile)
    whole.to_csv('gtd_wholedata.csv')


def make_df():
    df_new = pd.read_csv('gtd_wholedata.csv', usecols=selection(), low_memory=False, index_col=0)
    df_new.columns = feature_names()
    return df_new


def save_df_csv():
    '''make a csv file with all selected features'''
    return make_df().to_csv('gtd_wholedata_selected.csv')


def load_json_file(filepath):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', 100000)
    json_df = pd.read_json(filepath).iloc[:, :-1]
    return json_df
