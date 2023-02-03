#%%
import folium
import pandas as pd
import numpy as np
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
scale = 14

train = pd.read_csv("train_data.csv")
test = pd.read_csv("test_data.csv")


train.loc[:, 'lat'] = round(train.lat, scale)
train.loc[:, 'lon'] = round(train.lon, scale)

test.loc[:, 'lat'] = round(test.lat, scale)
test.loc[:, 'lon'] = round(test.lon, scale)


# Concatenate train and test data
all_df = pd.concat([train, test], axis=0)
# Create new feature
all_df['loc_group'] = all_df.groupby(['lat', 'lon']).ngroup()

print(f'{all_df.loc_group.nunique()} unique locations')
all_df.loc[:, 'lat'] *= 100
all_df.loc[:, 'lon'] *= 100

# Get the unique location groups
loc_groups = all_df.groupby('loc_group')

# Create a folium map
m = folium.Map(location=[all_df['lat'].mean(), all_df['lon'].mean()], zoom_start=10)

# create the grid lines
lats = np.arange(-90, 90, 5)
lons = np.arange(-180, 180, 5)

# add the grid lines to the map
for lat in lats:
    folium.PolyLine(locations=[(lat, -180), (lat, 180)], color='black', opacity=0.5).add_to(m)

for lon in lons:
    folium.PolyLine(locations=[(-90, lon), (90, lon)], color='black', opacity=0.5).add_to(m)

# Plot the unique locations on the map
for i, loc_group in loc_groups:
    lat = loc_group['lat'].mean()
    lon = loc_group['lon'].mean()
    folium.CircleMarker(
        location=[lat, lon],
        color='blue',
        fill=True,
        fill_color='blue'
    ).add_to(m)

# Show the map
m
m.save("map2.html")
#%%
