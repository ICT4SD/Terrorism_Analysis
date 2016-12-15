import AnalysisAndLinePlot as al
import heatmap as ht
import choropleth as choro
import Geo2D as geo
import bubble_chart as bubble


def IVIS_AL():
    return al.Display_Your_Analysis_And_LinePlot()


def IVIS_HT():
    return ht.Display_Your_Heatmap()


def IVIS_CHR():
    return choro.Display_Your_Choropleth()


def IVIS_GEO():
    return geo.Display_Your_Geo2D_Map()

def IVIS_BC():
    return bubble.Display_Your_Bubble_Chart()
