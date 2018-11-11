# -*- coding: utf-8 -*-
"""
Interactive map from Shapefile.

Created on Wed Jan 17 14:34:14 2018

@author: Henrikki Tenkanen
"""
import geopandas as gpd
from bokeh.plotting import save, figure, show
from bokeh.models import GeoJSONDataSource, HoverTool, LogColorMapper, CategoricalColorMapper
from bokeh.palettes import Spectral9 as palette
import pysal as ps

# Filepaths
address_fp = r"C:\HY-DATA\HENTENKA\CSC\Data\dataE5\addresses.shp"
metro_fp = r"C:\HY-DATA\HENTENKA\CSC\Data\dataE5\metro.shp"
ttime_fp = r"C:\HY-DATA\HENTENKA\CSC\Data\dataE5\TravelTimes_to_5975375_RailwayStation.shp"

# Read data
address = gpd.read_file(address_fp)
metro = gpd.read_file(metro_fp)
poly = gpd.read_file(ttime_fp)

# Reproject
address = address.to_crs(epsg=3067)
metro = metro.to_crs(epsg=3067)
poly = poly.to_crs(epsg=3067)

# Classify the travel time data
# -----------------------------

# Replace NoData values (-1) to 999
poly = poly.replace(-1, 999)

# Create breaks for the classes
breaks = [x for x in range(5, 200, 5)]

# Create legend labels
upper_limit = 60
step = 5
names = ["%s-%s " % (x-5, x) for x in range(step, upper_limit, step)]
names.append("%s <" % upper_limit)
    
# Classify the data based in 5 minute intervals
classifier = ps.User_Defined.make(bins=breaks)
pt_classif = poly[['pt_r_t']].apply(classifier)
pt_classif.columns = ['tclass']
poly = poly.join(pt_classif)

# Add labels to the classes
poly['label_pt'] = None
for i in range(len(names)):
   poly.loc[poly['tclass'] == i, 'label_pt'] = names[i]
   
# Update all cells that didn’t get any value with "60 <"
poly['label_pt'] = poly['label_pt'].fillna("%s <" % upper_limit)

# Convert the GeoDataFrame into a format 
# that Bokeh understands
point_src = GeoJSONDataSource(geojson=address.to_json())
line_src = GeoJSONDataSource(geojson=metro.to_json())
poly_src = GeoJSONDataSource(geojson=poly.to_json())

# Initialize the figure with title and specify also the width and height of the plot. 
# active_scroll parameter determines that the 'wheel_zoom' is activated by default.
p = figure(title="Travel times to Helsinki city center by public transportation", 
           plot_width=650, plot_height=500, active_scroll = "wheel_zoom")

# Remove grid lines from the map
p.grid.grid_line_color = None

# Create a colormapper
color_mapper = LogColorMapper(palette=palette)

# Add the polygon layer with the colors and legend
grid = p.patches('xs', 'ys', source=poly_src, name='grid',
                 fill_color={'field': 'tclass', 'transform': color_mapper},
                 line_color='black', line_width=0.03)

# Add stations
stations = p.circle(x='x', y='y', source=point_src, name='stations', color='green', size=8)

# Add metro line
p.multi_line('xs', 'ys', source=line_src, color='red', line_width=3)

# Add Hover tools
# ---------------

# Hover for points 
point_hover = HoverTool(renderers=[stations])
point_hover.tooltips = [('Address', '@address'),
                     ('Point-ID', '@id')
                     ]
# Separate hover for polygons
poly_hover = HoverTool(renderers=[grid])
poly_hover.tooltips = [('Travel time', '@pt_r_t')]

# Add the tools to the map
p.add_tools(point_hover)
p.add_tools(poly_hover)

# Show it in Sphinx
show(p)



