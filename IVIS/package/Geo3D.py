'''
Created on Nov 7, 2016

@author: Viola
'''

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from package import feature

m = Basemap()

fig = plt.figure(figsize=(18,18))
ax = Axes3D(fig)

ax.azim = 270
#ax.elev = 50
ax.dist = 7
#ax.set_axis_off()

polys = []
for polygon in m.landpolygons:
    polys.append(polygon.get_coords())

lc = PolyCollection(polys, edgecolor='w',
                   facecolor='#FFFFFF', closed=False)

ax.add_collection3d(lc)
ax.add_collection3d(m.drawcoastlines(linewidth=0.1))
ax.add_collection3d(m.drawcountries(linewidth=0.1))


# User can choose a year between 1970 to 2015
def select_year(dataset, year):
    year = input('Please choose a year between 1970 to 2015: ')
    return dataset[dataset['iyear'==year]]


def get_geolocs(dataframe):
    lons = feature.make_list(dataframe, 'longitude')
    lats = feature.make_list(dataframe, 'latitude')
    x, y = m(lons, lats)
    return x, y

def choose_feature(dataframe, col_name):
    feature_shown = feature.make_log_list(dataframe, col_name)
    return feature_shown

def plot_bar3d(dataframe, feature_name):
    geo_locs = get_geolocs(dataframe)
    feature = choose_feature(dataframe, feature_name)
    ax.bar3d(geo_locs[0], geo_locs[1], np.zeros(len(geo_locs[0])), 1, 1, feature, color= 'violet', alpha=0.08)

def show_3d(dataset, col_name):
    plot_bar3d(feature.get_rid_of_null(dataset, col_name), col_name)
    plt.title('Numbers of {} by Terrorism Attack'.format(col_name))
    plt.show()