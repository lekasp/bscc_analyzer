import geopandas as gpd
import matplotlib.pyplot as plt
import adjustText as aT

# create df from bscc_atlas_locations.tsv
df = gpd.read_file('data/bscc_atlas_locations.tsv', sep='\t')


# rename columns of df
df.columns = ['name', 'gnd', 'lat', 'lng', 'address', 'country', 'country_code', 'country_gnd', 'continent', 'geometry']

# delete unnecessary columns
df = df.drop(['gnd', 'address', 'country', 'country_code', 'country_gnd', 'geometry'], axis=1)

# create point geometry
geometry = gpd.points_from_xy(df.lng, df.lat)
geo_df = gpd.GeoDataFrame(df, geometry=geometry)

# load world map
worldmap = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

fig, ax = plt.subplots(figsize=(50, 50))
worldmap.plot(ax=ax, color='lightgrey', edgecolor='black', alpha=0.4)
geo_df.plot(ax=ax, color='blue', markersize=10)

texts = [plt.text(geo_df.geometry.x[i], geo_df.geometry.y[i], geo_df.name[i], fontsize=8) for i in range(len(geo_df))]

# another way to annotate
# geo_df.apply(lambda x: ax.annotate(text=x[0], xy=x.geometry.coords[0], ha='center', fontsize=8), axis=1)

# prevent text from overlapping
aT.adjust_text(texts, arrowprops=dict(arrowstyle='-', color='black', lw=0.5))

# set title
plt.title('BSCC Atlas Locations')

# set axis labels
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

plt.show()

# save figure
fig.savefig('bscc_atlas_locations.png', dpi=300, bbox_inches='tight')