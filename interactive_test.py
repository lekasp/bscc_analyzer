import geopandas as gpd
import matplotlib.pyplot as plt
import webbrowser
import os
from geopandas import GeoDataFrame
from geopandas import points_from_xy

# create df from locations_sorted.tsv
df = gpd.read_file('data/locations_sorted.tsv', sep='\t')
world = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))


geometry = gpd.points_from_xy(df.long, df.lat)
geo_df = gpd.GeoDataFrame(df, geometry=geometry)

# delete unnecessary columns of geo_df
geo_df = geo_df.drop(['lat', 'long', 'field_1', 'id', 'country'], axis=1)

# add a column count to world
world['count'] = 0

# switch columns of world
world = world[['name', 'count', 'geometry']]

# extend world with geo_df
world = world.append(geo_df)

# hide where count is 0
world = world[world['count'] != 0]

print(world.head())


m = world.explore(column='count')
m.save('bscc_locations.html')
webbrowser.open('file://' + os.path.realpath('bscc_locations.html'))



