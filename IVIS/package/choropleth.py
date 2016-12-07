'''Need to add Documentations'''

'''Not the final version yet'''


import pandas as pd
import numpy as np
import re
import folium
from feature import *
from ipywidgets import *
from IPython.display import display
from heatmap import Indication_selection
from data import load_json_file


class Choropleth(object):
    def __init__(self, Year, Indication):
        self.Year = Year
        self.Indication = Indication

    def damage_by_year(self):
        '''
        Return a grouped DataFrmae of chosen indication values by the given year.
        '''
        gt_df = pd.read_csv('gtd_wholedata_selected.csv')
        gt_df_yr = gt_df[['country', self.Indication]].fillna(0)[gt_df.year==self.Year]
        dam = gt_df_yr.groupby(['country']).sum()
        return dam

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
    js_countries = []
    for i in range(j.shape[0]):
        s = re.findall(r'\{\'name\'\:\s\'\D*\'\}', str(j.iloc[i]))
        name = re.findall(r'\'[A-Z]+\D*\'', s[0])[0].replace('\'', '')
        js_countries.append(name)
    return np.array(js_countries)


def js_country_names():
    js_ctr = pd.DataFrame(find_js_country_names(), columns=['country'])
    return js_ctr


def plot_choropleth(Indication, Color, Year):
    gtd_data = Choropleth(Year, Indication).all_ctr_dam()
    world_geo = r'countries.geo.json'

    up = Choropleth(Year, Indication).scale_max()

    map = folium.Map(location=[32, -90],
                     zoom_start=1.95,
                     min_zoom=1.95,
                     tiles='Mapbox bright')
    map.choropleth(geo_path=world_geo, data=gtd_data,
                   columns=['country', Indication],
                   threshold_scale=[0, 10, 100, 300, up/2, up],
                   key_on='feature.properties.name',
                   fill_color=Color, fill_opacity=0.5, line_opacity=0.5,
                   legend_name='Casualty Level',
                   reset=True)

    # map.add_child(folium.LayerControl())
    # map.save(outfile='GTD Choropleth.html')
    return map


def year_slider():
    yr = IntSlider(value=2000,
                     min=1970,
                     max=2015,
                     step=1,
                     description='Year:',
                     disabled=False,
                     continuous_update=False,
                     orientation='horizontal',
                     readout=True,
                     readout_format='i',
                     slider_color='white')
    yr.layout.width = '80%'
    return yr


def Color_palette():
    return Dropdown(options={'Ocean': 'PuBu', 'Orchid': 'RdPu', \
                             'NYU Pride': 'BuPu', 'Alert': 'OrRd', \
                             'Water Green': 'GnBu', 'Autumn Leaf': 'YlOrBr'},
                    value='BuPu',
                    description='Palette',
                    disabled=False,
                    button_style='')


def Display_Your_Chorpleth():
    return interact(plot_choropleth, Year=year_slider(), Indication=Indication_selection(), Color=Color_palette())
