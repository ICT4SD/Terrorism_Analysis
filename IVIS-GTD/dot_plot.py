from __future__ import print_function
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

import pandas as pd
import seaborn as sns
import math

import util as ut
from dot_plot_class import *
from Geo2d import year_interval_slider
import heatmap as hm

a = hm.IVIS()
a.gt_df.head()

dot_plot_features = ['country', 'year', 'attacktype', 'casualties']
gtd_dot = a.gt_df[dot_plot_features]

def attack_type():
	'''Return a string corresponding to an attack type'''
    attacktypes = list(set(a.gt_df['attacktype']))
    attack_type = widgets.Dropdown(
                                options=attacktypes,
                                value='Armed Assault',
                                description='Attack Type:',
                                disabled=False,
                                button_style='info') # 'success', 'info', 'warning', 'danger' or ''
    return attack_type

def metric_selection():
    '''
    Return a string of util name from users' manual pick
    '''
    metric = widgets.ToggleButtons(options={'Occurrences': 'occurrences', 'Casualties': 'casualties'},
                         value='occurrences',
                         description='Metric:',
                         disabled=False,
                         button_style='',  # 'success', 'info', 'warning', 'danger' or ''
                         tooltip='Description')
    return metric

def create_dot_plot(metric, attacktype, year_range):
    
    pd.options.mode.chained_assignment = None
    
    dot_plot = Dot_Plot_Data(a.gt_df, 'country', 'casualties', 'year', 'attacktype', metric)
    
    dot_plot.user_selection(year_range, attacktype)
    dot_plot.aggregate()
    dot_plot.convert_series(str.title(metric) + ' from ' + attacktype)
    dot_plot.take_top_20()
    
    sns.set(style="whitegrid")
    
    g = sns.PairGrid(dot_plot.data,
                     x_vars=str.title(metric) + ' from ' + attacktype, y_vars=['country'],
                     size=12, aspect=.50)

    # Draw a dot plot using the stripplot function
    g.map(sns.stripplot, size=10, orient="h",
          palette="Blues_r", edgecolor="gray")
    
    xmax = math.ceil(max(dot_plot.data[dot_plot.label])/1000)*1000

    g.set(xlim=(0, xmax), xlabel=str.title(metric), ylabel=str.title(dot_plot.yaxis_vals))

    # Use meaningful titles for the columns
    titles = ['Top Countries by ' + attacktype + ' ' + str.title(metric)]

    for ax, title in zip(g.axes.flat, titles):

        # Set a different title for each axes
        ax.set(title=title)

        # Make the grid horizontal instead of vertical
        ax.xaxis.grid(False)
        ax.yaxis.grid(True)

    sns.despine(left=True, bottom=True)

def Display_Your_Dot_Plot():
	 '''
    Allow users to customize the dot plot
    '''
    interact(create_dot_plot, metric = metric_selection(), attacktype = attack_type(), year_range = year_interval_slider());

