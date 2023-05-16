import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set(style="ticks", color_codes=True)
import geopandas as gpd
import adjustText as aT

df = pd.read_csv('data/bcc_abroad_foundation.csv')

geometry = gpd.points_from_xy(df.lng, df.lat)
geo_df = gpd.GeoDataFrame(df, geometry=geometry)

# load world map
worldmap = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))





continents = {'AF': 'pink',
    'AS': 'greed',
    'EU': 'blue',
    'NA': 'yellow',
    'SA': 'red'
}

fig, ax = plt.subplots(figsize=(50, 50))
worldmap.plot(ax=ax, color='lightgrey', edgecolor='black', alpha=0.4)
geo_df.plot(ax=ax, column='Code', cmap='Pastel2', markersize=10)

texts = [plt.text(geo_df.geometry.x[i], geo_df.geometry.y[i], geo_df.City[i], fontsize=8) for i in range(len(geo_df))]

# prevent text from overlapping
aT.adjust_text(texts, arrowprops=dict(arrowstyle='-', color='black', lw=0.5))

# set title
plt.title('BSCC Atlas Locations')

# set axis labels
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

plt.show()

fig.savefig('bscc_atlas_foundation.png', dpi=300, bbox_inches='tight')