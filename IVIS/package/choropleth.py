'''Need to add Documentations'''

'''Not the final version yet'''


import pandas as pd
import numpy as np
import re
import folium
from feature import *
from ipywidgets import *
from heatmap import *
from data import *
from UserError import *


class Choropleth(object):
    def __init__(self, Year, Indication):
        self.Year = Year
        self.Indication = Indication
        self.df_by_yr = df_year_idx().loc[self.Year].fillna(0)

    def damage_by_year(self):
        '''
        Return a grouped DataFrame of chosen indication values
        by the countries in the given year.
        '''
        dam_df_yr = self.df_by_yr[['country', self.Indication]]
        return dam_df_yr.groupby(['country']).sum()

    def max_dam(self):
        '''
        Return the maximum value of the chosen indication by the chosen year
        '''
        dam_series = self.damage_by_year()[self.Indication]
        return dam_series.max()

    def scale_max(self):
        return (int(self.max_dam() / 100) + 1) * 100


    def all_ctr_dam(self):
        dam_by_year = Choropleth(self.Year, self.Indication).damage_by_year().reset_index()
        js_ctr = js_country_names()
        merged_df = pd.merge(dam_by_year, js_ctr, on='country', how='outer').fillna(-99)
        sorted_df = merged_df.sort_values(by='country')
        new_df = sorted_df.reset_index().drop('index', 1)
        return new_df


def find_js_country_names():
    j = load_json_file('countries.geo.json')
    ls = []
    for i in j['features']:
        ls.append(i['properties']['name'])
    return np.array(ls)


def js_country_names():
    js_ctr = pd.DataFrame(find_js_country_names(), columns=['country'])
    return js_ctr


def plot_choropleth(Indication, Color, Year):

    if int(Year) == 1993:
        print('Data of 1993 is not available in Global Terrorism Database.\n\
Click the link to learn why.\nhttps://www.start.umd.edu/gtd/faq/')

    elif int(Year) not in range(1970, 2016):
        raise NoDataError
    else:
        gtd_data = Choropleth(Year, Indication).all_ctr_dam()
        world_geo = r'countries.geo.json'

        up = Choropleth(Year, Indication).scale_max()

        map = folium.Map(location=[32, -90],
                         zoom_start=2,
                         min_zoom=2,
                         tiles='Mapbox bright')
        map.choropleth(geo_path=world_geo, data=gtd_data,
                       columns=['country', Indication],
                       threshold_scale=[0, 10, 100, up/3, up*2/3, up],
                       key_on='feature.properties.name',
                       fill_color=Color, fill_opacity=0.7, line_opacity=0.2,
                       legend_name='Casualty Level',
                       reset=True)
        return map


def year_slider():
    yr = IntSlider(value=2000,
                   min=1970,
                   max=2015,
                   step=1,
                   description='Year',
                   disabled=False,
                   continuous_update=False,
                   orientation='horizontal',
                   readout=True,
                   readout_format='i',
                   slider_color='white'
                   )
    yr.layout.width = '80%'
    return yr


def Color_palette():
    return Dropdown(options={'Ocean': 'PuBu', 'Orchid': 'RdPu', \
                             'NYU Pride': 'BuPu', 'Alert': 'OrRd', \
                             'Water Green': 'GnBu', 'Autumn Leaf': 'YlOrBr'},
                    value='PuBu',
                    description='Palette',
                    disabled=False,
                    button_style='info')


def Display_Your_Choropleth():
    try:
        return interact(plot_choropleth,
                        Year=year_slider(),
                        Indication=Indication_selection(),
                        Color=Color_palette()
                        )
    except NoDataError as x:
        print(x)
