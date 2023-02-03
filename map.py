#%%
import folium
import pandas as pd
import numpy as np
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

all_df.to_csv('raw_data.csv', index=False)

#%%
