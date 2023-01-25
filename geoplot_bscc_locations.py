import geopandas as gpd
import matplotlib.pyplot as plt
import adjustText as aT

# create df from bscc_atlas_locations.tsv
df = gpd.read_file('data/locations_sorted.tsv', sep='\t')

# rename columns of df
df.columns = ['number', 'gnd', 'name', 'lat', 'lng', 'country_code', 'count', 'geometry']

# delete unnecessary columns
df = df.drop(['number', 'gnd', 'geometry'], axis=1)

# create point geometry
geometry = gpd.points_from_xy(df.lng, df.lat)
geo_df = gpd.GeoDataFrame(df, geometry=geometry)

# load world map with europe only from gdp datasets
worldmap = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
europemap = worldmap[worldmap['continent'] == 'Europe']
fig, ax = plt.subplots(figsize=(20, 20))
europemap.plot(ax=ax, color='lightgrey', edgecolor='black', alpha=0.4)

# plot points
geo_df.plot(ax=ax, color='blue', markersize=10)
texts = [plt.text(geo_df.geometry.x[i], geo_df.geometry.y[i], geo_df.name[i], fontsize=8) for i in range(len(geo_df))]

# another way to annotate
# geo_df.apply(lambda x: ax.annotate(text=x[0], xy=x.geometry.coords[0], ha='center', fontsize=8), axis=1)

# prevent text from overlapping
#aT.adjust_text(texts, arrowprops=dict(arrowstyle='-', color='black', lw=0.5))

# bounding box
ax.set_xlim(-10, 15)
ax.set_ylim(40, 65)


# set title with size 30
plt.title('BSCC Locations')

# set axis labels with size 20
ax.tick_params(axis='both', which='major', labelsize=20)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

plt.show()

# save figure
fig.savefig('bscc_locations.png', dpi=300, bbox_inches='tight')
