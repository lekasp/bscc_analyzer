import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("macosx")
import pandas as pd
import seaborn as sns

# Define col names
cols = ["id", "name", "lat", "long", "country", "count"]

# read df
loc_df = pd.read_csv('data/locations.tsv', sep='\t', names=cols, header=None)

# Sort df and remove unknown locations
loc_df_sorted = loc_df.sort_values(by=['count'], ascending=False)
loc_df_sorted.drop(index=loc_df_sorted.index[0], axis=0, inplace=True)
loc_df_sorted.drop(index=loc_df_sorted.index[2], axis=0, inplace=True)
loc_df_sorted.to_csv("locations_sorted.tsv", sep='\t')

# Get Sum of Country Codes
country_df = loc_df_sorted[['country','count']].copy()
country_df_sum = country_df.groupby(['country']).sum()
country_df_sum.to_csv("country_sum.tsv", sep='\t')
test_df = pd.read_csv('country_sum.tsv', sep='\t')
print(test_df)

#Barplot
ax = sns.barplot(data=test_df, x="country", y="count", hue="country", dodge=False, order=["GB", "CH"])

ax.set_xlabel("Country")
ax.set_ylabel("Count")
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.text(0, 1.08, 'Number of Country Counts', transform=ax.transAxes, size=18, weight=600, ha='left')
ax.text(0, 1.02, 'Count of Each Country Mention', transform=ax.transAxes, size=10, weight=600, color='#777777')
ax.text(0,-0.13, 'Source: Own Graph', transform=ax.transAxes, size=10, weight=200, color='#777777')
plt.setp(ax.get_xticklabels(), horizontalalignment='right', fontsize=8)
ax.grid(color='#777777', axis='y', which='both', ls='-', lw=0.2)
for container in ax.containers:
    ax.bar_label(container)
ax.legend([],[], frameon=False)
plt.show()
