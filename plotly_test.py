import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import plotly as py

# load data
df = pd.read_csv('data/bscc_atlas_locations.tsv', sep='\t')

# rename columns
df.columns = ['name', 'gnd', 'lat', 'lng', 'address', 'country', 'country_code', 'country_gnd', 'continent_code']

#insert for missing values in continent_code NA
df['continent_code'] = df['continent_code'].fillna('NA')

# change continent codes to continent names
df['continent_code'] = df['continent_code'].replace({'NA': 'North America (3)', 'SA': 'South America (5)', 'EU': 'Europe (15)', 'AS': 'Asia (29)', 'AF': 'Africa (5)', 'OC': 'Oceania'})

# remove unnecessary columns
df2 = df.drop(['gnd', 'address', 'country_code', 'country_gnd'], axis=1)

fig = px.scatter_geo(df2, lat='lat', lon='lng', hover_name='name', color='continent_code', projection='natural earth',
                     size_max=10, opacity=0.5, title='BSCC Atlas Locations',
                     labels={'name': 'Name'},
                     hover_data={'lat': False, 'lng': False, 'continent_code': False, 'country': False})


fig.update_traces(textposition='top center', mode='markers+text', textfont_size=8)

fig.update_traces(marker=dict(size=10))


fig.show()
