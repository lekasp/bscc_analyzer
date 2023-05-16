import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap as Basemap

# create df from 0_1951_edges.tsv
df = pd.read_csv('data/output_1951/0_1951_edges.tsv', sep='\t')
print(df)


