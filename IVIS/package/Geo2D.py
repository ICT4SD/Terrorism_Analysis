from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from package import feature


def plot_2D_density(dataset):
    plt.figure(figsize=(18,15))
    m = Basemap(projection='mill', llcrnrlon=-180, urcrnrlon=180,\
                llcrnrlat=-70, urcrnrlat=85, resolution='c', )

    m.drawcountries(linewidth=0.5, linestyle='solid', color='w', antialiased=1, ax=None, zorder=None)
    m.fillcontinents()
    m.drawmapboundary()

    lat = feature.make_list(dataset, 'latitude')
    lon = feature.make_list(dataset, 'longitude')

    x,y = m(lon, lat)
    m.plot(x, y, 'r.', marker='.', markersize=3, alpha=.5)

    plt.title('Global Attack Density: 1970-2015')
    plt.show()
    