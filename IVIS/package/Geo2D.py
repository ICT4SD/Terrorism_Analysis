from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np
from feature import *
from heatmap import *
from ipywidgets import *


def plot_2D_density(Year, MapStyle):
    df = user_df(Year)
    plt.figure(figsize=(18,10))

    m = Basemap('mill')
    m.drawcountries(linewidth=0.5, linestyle='solid', color='w', antialiased=1, ax=None, zorder=None)

    if MapStyle == 'Blue Marble':
        m.drawcoastlines()
        m.bluemarble()
    elif MapStyle == 'Etopo':
        m.etopo()
    else:
        m.fillcontinents()
        m.drawmapboundary()

    lat = make_list(df, 'latitude')
    lon = make_list(df, 'longitude')

    x,y = m(lon, lat)
    m.plot(x, y, 'r.', marker='o', markersize=3, alpha=.8)

    plt.title('Global Attack Density Dot Plot: {}-{}'.format(Year[0], Year[1]), size=16)
    plt.show()


def user_df(Year):
    '''
    Input Parameter
        - Year: Time Interval

    Return
        - a DataFrame
    '''
    gt_df = IVIS().gt_df
    df = gt_df[(gt_df.year <= Year[1]) & (gt_df.year >= Year[0])]
    return df


def year_interval():
    yr_interval = IntRangeSlider(value=[1996, 2000],
                                 min=1970,
                                 max=2015,
                                 step=1,
                                 description='Year:',
                                 disabled=False,
                                 continuous_update=False,
                                 orientation='horizontal',
                                 readout=True,
                                 readout_format='i',
                                 slider_color='white',
                                 color='black')
    yr_interval.layout.width = '80%'
    return yr_interval


def map_styles():
    return ('Blue Marble', 'Etopo', 'Plain')


def Display_Your_Geo2D_Map():
    return interact(plot_2D_density, Year=year_interval(), MapStyle=map_styles())
