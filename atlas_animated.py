import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import plotly as py

# interactive map bscc locations

# load data
df = pd.read_csv('data/bcc_abroad_foundation.csv')

#insert for missing values in continent_code NA
df['Secured'] = df['Secured'].fillna('NA')
df['Foundation'] = df['Foundation'].fillna('NA')
df['Earliest'] = df['Earliest'].fillna('NA')



# change continent codes to continent names
df['Code'] = df['Code'].replace({'NA': 'North America (3)', 'SA': 'South America (5)', 'EU': 'Europe (15)', 'AS': 'Asia (29)', 'AF': 'Africa (5)', 'OC': 'Oceania'})

df.sort_values('Date', inplace=True)

print(df)
fig = px.scatter_geo(df, lat='lat', lon='lng', hover_name='City', color='Code', projection='natural earth',
                     size_max=10, opacity=0.5, title='BSCC Atlas Locations',
                     labels={'City': 'City'}, animation_frame='Date', animation_group='City',
                     hover_data={'lat': False, 'lng': False, 'Code': False, 'Country': False})


fig.update_traces(textposition='top center', mode='markers+text', textfont_size=8)

fig.update_traces(marker=dict(size=10))


fig.show()