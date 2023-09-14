import pandas as pd
import numpy as np

from bokeh.models import ColorBar, ColumnDataSource, LinearColorMapper, HoverTool
from bokeh.plotting import figure, output_notebook, show
from bokeh.tile_providers import get_provider
from bokeh.layouts import gridplot

# Safe graphes
from bokeh.io import export_svg

# Plotting the graphs in the Jupyter notebook
output_notebook()

# Import and prepare Data
results = pd.read_csv('data/csv_files/scores.csv')
locs = pd.read_csv('data/csv_files/locationsDegree_formatted.csv')

# Transform the coordinates using the EPSG 3857 System because it worked for Darwin. 
locs.Longitude = locs.Longitude * 20037508.34 / 180
locs.Latitude = np.log(np.tan((90 + locs.Latitude) * np.pi / 360)) / (np.pi / 180)
locs.Latitude = locs.Latitude.apply(lambda x : x * 20037508.34 / 180)

#Drop results all
results = results.iloc[:-4,:]
# Only select Location and f1_score
results = results[results['test_set'] == 1][['Location', 'f1_score']]
# Reset Index
results.set_index(np.arange(len(results)), inplace=True)
# Merge dataframe with locations for easy plotting
df = results.merge(locs, on='Location', how='inner')

Locations = ['Albury', 'BadgerysCreek', 'Cobar', 'CoffsHarbour', 'Moree', 'Newcastle','NorahHead', 'NorfolkIsland', 
             'Penrith', 'Richmond' ,'Sydney', 'SydneyAirport','WaggaWagga', 'Williamtown', 'Wollongong', 'Canberra', 
             'Tuggeranong','MountGinini', 'Ballarat', 'Bendigo', 'Sale', 'MelbourneAirport', 'Melbourne','Mildura', 
             'Nhil', 'Portland', 'Watsonia', 'Dartmoor', 'Brisbane', 'Cairns','GoldCoast', 'Townsville', 'Adelaide', 
             'MountGambier', 'Nuriootpa', 'Woomera','Albany', 'Witchcliffe', 'PearceRAAF', 'PerthAirport', 'Perth', 
             'SalmonGums','Walpole', 'Hobart', 'Launceston', 'AliceSprings', 'Darwin', 'Katherine','Uluru']

f1 =[0.71945701, 0.69886364, 0.6779661 , 0.7605985 , 0.68503937,
       0.62555066, 0.7032967 , 0.67042254, 0.73767258, 0.72924188,
       0.7264    , 0.70169492, 0.68901304, 0.66666667, 0.72168285,
       0.703125  , 0.69874477, 0.76059322, 0.73992674, 0.70560748,
       0.5       , 0.6581741 , 0.63052209, 0.62305296, 0.68867925,
       0.76388889, 0.68729642, 0.75862069, 0.67322835, 0.70689655,
       0.66883117, 0.69902913, 0.67857143, 0.78286558, 0.6900369 ,
       0.47567568, 0.64745763, 0.7962675 , 0.78857143, 0.73504274,
       0.78095238, 0.57386364, 0.74566474, 0.63519313, 0.67068273,
       0.66666667, 0.76979742, 0.01      , 0.63076923]

scores = pd.DataFrame()
scores['Location'] = Locations
scores['f1_score'] = f1


df_rob = scores.merge(locs, on='Location', how='inner')

# Map with hover tools

source = ColumnDataSource(df_rob)

# Creating the CARTODBPOSITRON tile from get_provider

tile = get_provider('CARTODBPOSITRON')

pallet = ['#FD2D01', '#FE5E3C', '#FF886F', '#FFB1A0', '#9EFE9C', '#78FE76', '#07FE03']

exp_cmap = LinearColorMapper(palette=pallet, 
                             low = min(df["f1_score"]), 
                             high = max(df["f1_score"]))

bar = ColorBar(color_mapper=exp_cmap, location=(0,0))

tooltips = [("Location", "@Location"), 
            ("f1-score", "@f1_score")]

# Initialization of the original figure
# See the entire map and all clusters
fig1 = figure(
    x_range=(12500000, 17500000),
    y_range=(-6000000, -1400000),   # y-axis range
    x_axis_type = 'mercator',       # type of the axis, in this case a mercator projection which is 
    y_axis_type = 'mercator'        # used to find one's way on a flat map of the Earth
    )
                                        
fig1.add_tile(tile) 

fig1_circle = fig1.circle(
    x = 'Longitude',    # x-axis
    y = 'Latitude',     # y-axis
    fill_color = {"field":"f1_score", "transform":exp_cmap},
    size = 10,          # circle size
    source = source     # data source
    )     

fig1.add_layout(bar, "left")  

hover1 = HoverTool(tooltips = tooltips, renderers = [fig1_circle])

    # Displaying the figure
fig1.add_tools(hover1)

# Initialization of the small figure
# See the the bottom right part and all clusters no labels
fig2 =  figure(
    x_range=(14500000, 17500000),
    y_range=(-5000000, -3000000),   # y-axis range
    x_axis_type = 'mercator',       # type of the axis, in this case a mercator projection which is 
    y_axis_type = 'mercator'        # used to find one's way on an flat map of the Earth
    )                              
      

fig2.add_tile(tile) 

fig2_circle = fig2.circle(
    x = 'Longitude',           # x-axis
    y = 'Latitude',           # y-axis
    fill_color = {"field":"f1_score", "transform":exp_cmap},
    size = 10,           # circle size
    source = source
    )  

fig2.add_layout(bar, "left")
hover2 = HoverTool(tooltips = tooltips, renderers = [fig2_circle])

# Displaying the figure
fig2.add_tools(hover2)
# Displaying the figure
grid = gridplot([[fig1, fig2]], width=600, height=600)

show(fig1)
show(fig2)
