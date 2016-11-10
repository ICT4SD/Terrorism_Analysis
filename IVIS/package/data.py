'''
This module converts the excel dataset file into the csv file, processes the dataset with selected features,
get new dataframe, and store the new dataframe in csv file.

The whole process simply the original dataset and shortens the loading time for future data manipulations.
'''

import pandas as pd
import numpy as np
from package import feature


path_excelfile = '/Users/Viola/CDS/programmingDS/Project/Data/GTD_0616dist/globalterrorismdb_0616dist.xlsx'

def excel_to_csv(path_excelfile):
    whole = pd.read_excel(path_excelfile)
    whole.to_csv('wholedata.csv')
    
def make_df():
    df_raw = pd.read_csv('wholedata.csv', low_memory=False, index_col=0)
    features = feature.selection()
    return df_raw[features]

def save_df_csv():
    make_df().to_csv('wholedata_selected.csv')



    