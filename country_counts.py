import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("macosx")
import pandas as pd
import seaborn as sns

# Define col names
cols = ["id", "name", "lat", "long", "country", "count"]

# read df
loc_df = pd.read_csv('locations.tsv', sep='\t', names=cols, header=None)

# Sort df and remove unknown locations
loc_df_sorted = loc_df.sort_values(by=['count'], ascending=False)
loc_df_sorted.drop(index=loc_df_sorted.index[0], axis=0, inplace=True)
loc_df_sorted.drop(index=loc_df_sorted.index[2], axis=0, inplace=True)
loc_df_sorted.to_csv("locations_sorted.tsv", sep='\t')

# Locations for Country
loc_df_swiss = loc_df_sorted


# New df for locations counts > 10
loc_df_10 = loc_df_sorted[loc_df_sorted["count"] >= 15]
loc_df_10.to_csv("locations_10.tsv", sep='\t')


labels=["Great Britain", "Switzerland"]

ax = sns.barplot(data=loc_df_10, x="name", y="count", hue="country", dodge=False)
ax.set_xlabel("Location")
ax.set_ylabel("Count")
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.text(0, 1.08, 'Number of Country Counts', transform=ax.transAxes, size=18, weight=600, ha='left')
ax.text(0, 1.02, 'Count of Each Country Mention', transform=ax.transAxes, size=10, weight=600, color='#777777')
ax.text(0,-0.13, 'Source: Own Graph', transform=ax.transAxes, size=10, weight=200, color='#777777')
plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right', fontsize=8)
ax.grid(color='#777777', axis='y', which='both', ls='-', lw=0.2)
for container in ax.containers:
    ax.bar_label(container)
h, l = ax.get_legend_handles_labels()
ax.legend(h, labels, title="Country", loc='upper right')
plt.show()
