'''
This module includes:
    - IVIS class, with the attrubutes:
        1. feature-selected dataframe of Global Terrorism Database
        2. a unieque list of region names
    - visualization function of the dataset in heatmap
    - the target feature
    - the visualizing color palette

@author: Xianzhi Cao (xc965)
'''


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from feature import *
from data import *
from ipywidgets import *


class IVIS(object):
    '''
    contains attributes of:
        - DataFrame of Global Terrorism data selection
        - list of all regions' names
        - function of get
    '''
    def __init__(self):
        self.gt_df = load_df()
        self.region_names = self.gt_df.region.unique().tolist()


    def countries_by_region(self):
        '''
        Return a dict with items:
            - keys:    region names
            - values:  country names keyed by certain region
        '''
        country_names = {}
        for region in self.region_names:
            country_names[region] = self.gt_df[self.gt_df.region == region].dropna().country.unique()
        return country_names


def Heatmap_by_region(Indication, Region, Cmap):
    '''
    Parameters
        - Indication: feature of damages    | str
        - Region    : name of region        | str
        - Cmap      : color map             | str
    Return
        A Heatmap
            of value of chosen indication
            by countrys in chosen region,
            colored with chosen cmap
    '''
    dat = IVIS().gt_df[IVIS().gt_df.region == Region]  # DataFrame filtered with region
    couple_cols = dat[['year', 'country', Indication]]
    couple_cols.reset_index(inplace=True)
    cp_cols = couple_cols.drop('index', 1)
    y_c = cp_cols.groupby(['year', 'country']).sum()
    y_c = y_c.reset_index()

    # proportionally set the height of the figure size
    # by the number of countries in the chosen region
    fig = plt.figure(figsize=(25, int(len(IVIS().countries_by_region()[Region])*3/4)))

    # use pivot table to set data in heatmap plot format
    pivot_table = y_c.pivot('country', 'year', Indication).fillna(0)
    plt.title('Yearly Number of {} in {} by Terror Attacks (1970-2015)\n'.format(Indication.capitalize(),
                                                                               Region), size = 20)
    plt.xlabel('Regions', size = 14)
    plt.ylabel('Years', size = 14)
    plt.xticks(rotation=-15)

    # plot heatmap
    sns.heatmap(pivot_table,
                annot=False,
                fmt='.0f',
                linewidths=.5,
                square=True,
                cmap=Cmap,
                cbar_kws={"orientation": "horizontal"}
                )
    #fig.tight_layout()
    plt.show()


def region_picker():
    '''
    Return a string of region name from users' manual pick
    '''
    return Dropdown(options=tuple(IVIS().region_names),
                    description='Region',
                    disabled=False,
                    button_style='info' # 'success', 'info', 'warning', 'danger' or ''
                    )


def Cmap_palette():
    '''
    Return a tring of color from users' manual pick
    '''
    return Dropdown(options={'Aqua': 'cool', 'Lemon': 'Wistia', 'NYU Pride': 'Purples_r', 'Alert': 'Reds', 'B&W': 'gist_gray_r', 'Classic': 'RdBu_r'},
                    value='cool',
                    description='Palette',
                    disabled=False,
                    button_style='info')



def Indication_selection():
    '''
    Return a tring of feature name from users' manual pick
    '''
    return ToggleButtons(options={'Kills': 'kills', 'Wounds': 'wounds', 'Casualties': 'casualties'},
                         value='casualties',
                         description='Indication',
                         disabled=False,
                         button_style='',  # 'success', 'info', 'warning', 'danger' or ''
                         tooltip='Description')


def Display_Your_Heatmap():
    '''
    Allow users to interactively explore data information
    and customize the heatmap
    '''
    interact(Heatmap_by_region,
             Region=region_picker(),
             Cmap = Cmap_palette(),
             Indication = Indication_selection())
