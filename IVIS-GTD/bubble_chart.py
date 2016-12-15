'''
Created on Dec 14, 2016

@author: Caroline
'''

from ipywidgets import *
import feature
import pandas as pd
import numpy as np
import heatmap as hm
import matplotlib.pyplot as plt
import math
import matplotlib.patches as mpatches
from matplotlib import cm
import bubble_chart_class as bcc
import data_reshape as rs

ivis = hm.IVIS()
bubble_chart_features = ['year', 'country', 'region', 'casualties']
gtd_bubble = ivis.gt_df[bubble_chart_features]
gtd_bubble = feature.replace_series_with_range(gtd_bubble, gtd_bubble['year'], 5)

#haven't updated the "feature" one on git.

bubble_chart = bcc.Bubble_Chart_Data(gtd_bubble, 'country', 'region', 'year ranges', 'casualties')

bubble_chart_yr = IntSlider(min=1975,max=2015,step=5,value=1995, width = '90%')

def Display_Your_Bubble_Chart():
    '''
    Allow users to interactively explore data information
    and customize the bubble chart
    '''
    interact(bubble_chart.create_bubble_chart, year=bubble_chart_yr)
    

