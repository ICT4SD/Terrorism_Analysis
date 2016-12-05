'''
This module allows user to visualize the data in heatmap. Users will be able to select:
    - the year 
    - the region
    - the target feature
    - the visualizing color palette

@author: Xianzhi Cao (xc965)
'''


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from feature import *
from ipywidgets import *
from IPython.display import display
from nltk.sem.chat80 import region


class IVIS(object):
    
    def __init__(self):
        self.gt_df = pd.read_csv('gtd_wholedata_selected.csv')
        self.region_names = self.gt_df.region.unique().tolist()
#         self.year = year
#         self.region_sel = region_sel
         
    
    def countries_by_region(self):
        country_names = {}
        for region in self.region_names:
            country_names[region] = self.gt_df[self.gt_df.region == region].dropna().country.unique()
            
        return country_names
            
            
def Heatmap_by_region(Indication, Region, Cmap):
    dat = IVIS().gt_df[IVIS().gt_df.region == Region]
    couple_cols = dat[['year', 'country', Indication]]
    couple_cols.reset_index(inplace=True)
    cp_cols = couple_cols.drop('index', 1)
    y_c = cp_cols.groupby(['year', 'country']).sum()
    y_c = y_c.reset_index()

    fig = plt.figure(figsize=(25, int(len(IVIS().countries_by_region()[Region])*2/3)))
    pivot_table = y_c.pivot('country', 'year', Indication).fillna(0)
    plt.title('Yearly Number of {} in {} by Terror Attacks (1970-2015)'.format(Indication.capitalize(), 
                                                                               Region), size = 16)
    plt.xlabel('Regions', size = 14)
    plt.ylabel('Years', size = 14)
    plt.xticks(rotation=-15)
    
    # plot heatmap
    sns.heatmap(pivot_table, annot=False, fmt='.0f', 
                linewidths=.5, square=True, cmap=Cmap, cbar_kws={"orientation": "horizontal"})
    #fig.tight_layout()
    plt.show()


def Cmap_palette():
    return Dropdown(options={'Aqua': 'cool', 'Lemon': 'Wistia', 'NYU Pride': 'Purples_r', 'Alert': 'Reds', 'B&W': 'gist_gray_r', 'Classic': 'RdBu_r'}, 
                    value='cool', description='Palette', disabled=False, button_style='')


        
def Indication_selection():
    return ToggleButtons(options={'Casualties': 'casualties', 'Wounds': 'wounds'},
                         description='Indication', disabled=False, button_style='', tooltip='Description')
    



