# Libraries
from math import pi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import calendar
from cycler import cycler
from bokeh.io import output_file, show
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum
from bokeh.layouts import column
from bokeh.transform import jitter
import operator


# data fetching
df = pd.read_csv('./Data/cleanData.csv')

# Splitting Year and Month from the lastUpdated column and rounded ratings value
df['Year'] = pd.DatetimeIndex(df['lastUpdated']).year
df['Month'] = pd.DatetimeIndex(df['lastUpdated']).month
df['lastUpdated'] = pd.to_datetime(df['lastUpdated'])
df['rating'].fillna(df['rating'].mean(), inplace=True)
df['rating'] = df['rating'].round(1)

# Converting number into months
df['Month'] = df['Month'].apply(lambda x: calendar.month_abbr[x])


# Spliting dataframe from 'rated' column where rated is 'Everyone'
everyone_rated_df = df.copy()[df['rated'] == 'Everyone']
everyone_rated = df.copy()[df['rated'] == 'Everyone']
everyone_rated_df.set_index('Year', inplace=True)
everyone_rated_df.sort_index(inplace=True)
everyone_rated.sort_index(inplace=True)

# ***************************************************************************

# Char # 1 Genre(Everyone) vs No. of Application in 2018
plt.figure(figsize=(10, 5))
chart1 = sns.countplot(
    data=everyone_rated[everyone_rated['Year'] == 2018],
    x='category',
    palette='Set1'
)
chart1.set_xticklabels(chart1.get_xticklabels(),
                       rotation=45, horizontalalignment='right')
plt.xlabel('Classifications of Applications')
plt.ylabel('No. of Application')
plt.title("Genre(Everyone) vs No. of Application Got Updated in 2018")
fig_1 = chart1.get_figure()
fig_1.savefig("./Data/counter_plot.png", dpi=300, bbox_inches="tight")

# ***************************************************************************


# Cat Plot  (Genre(Everyone) vs No. of Application Got Updated in 2015 & 2018)
plt.figure(figsize=(18, 10))
chart2 = sns.catplot(
    data=everyone_rated[everyone_rated['Year'].isin(np.arange(2016, 2019, 1))],
    x='category',
    kind='count',
    palette='Set1',
    col='Year',
    aspect=1,
)
chart2.set_xticklabels(rotation=65, horizontalalignment='right')
plt.xlabel('Classifications of Applications')
plt.ylabel('No. of Application')
#plt.title("Genre(Everyone) vs No of Application")
#plt.title("Genre(Everyone) vs No of Application")
chart2.savefig("./Data/cat_plot.png", dpi=300, bbox_inches="tight")


# ***************************************************************************


# Heatmap Os Version vs Category
# Application from Family category support highest number of the devices
by_category = (df
               .groupby('category')
               .filter(lambda x: len(x) > 0)
               .groupby(['category', 'osVer'])
               .size()
               .unstack()
               )
plt.figure(figsize=(10, 10))
chart3 = sns.heatmap(
    by_category,
    square=True,
    cbar_kws={'fraction': 0.01},
    cmap='OrRd',
    linewidth=1
)

chart3.set_xticklabels(chart3.get_xticklabels(),
                       rotation=45, horizontalalignment='right')
chart3.set_yticklabels(chart3.get_yticklabels(),
                       rotation=45, horizontalalignment='right')

plt.xlabel('Android Version')
plt.ylabel('Application Classifications')
plt.title('Android Version vs Application Classifications', fontsize=20)
plt.subplots_adjust(top=0.9)
fig_3 = chart3.get_figure()
fig_3.savefig("./Data/heatmap_1.png", dpi=300, bbox_inches="tight")


# ***************************************************************************


# Heatmap Applications got Update (in months)
by_category = (df
               .groupby('Year')
               .filter(lambda x: len(x) > 0)
               .groupby(['Year', 'Month'])
               .size()
               .unstack()
               )
plt.figure(figsize=(10, 10))
chart4 = sns.heatmap(
    by_category,
    square=True,
    cbar_kws={'fraction': 0.01},
    cmap='OrRd',
    linewidth=1
)

chart4.set_xticklabels(chart4.get_xticklabels(),
                       rotation=45, horizontalalignment='right')
chart4.set_yticklabels(chart4.get_yticklabels(),
                       rotation=45, horizontalalignment='right')

plt.xlabel('Month')
plt.ylabel('Year')
plt.title('Applications got Update (in months)', fontsize=20)
plt.subplots_adjust(top=0.9)
fig_4 = chart4.get_figure()
fig_4.savefig("./Data/heatmap_2.png", dpi=300, bbox_inches="tight")


# ***************************************************************************


# Mean and standard deviation plot
byCategory = df.groupby('category')
plt.figure(figsize=(35, 15))
std = byCategory.std()
std = pd.DataFrame(std[['rating']])
avg = byCategory.mean()
avg = pd.DataFrame(avg[['rating']])
my_colors = 'rgbkymc'
chart5 = avg.plot(figsize=(15, 5), legend=False, kind="bar",
                  rot=90, color=my_colors, fontsize=12, yerr=std)
chart5.set_title(
    "Average Rating & Std. Deviation of Application Categories", fontsize=18)
chart5.set_xlabel("Application Classification", fontsize=18)
chart5.set_ylabel("App Rating", fontsize=18)
chart5.set_ylim(0, 6)
fig_5 = chart5.get_figure()
fig_5.savefig("./Data/mean_plot.png", dpi=300, bbox_inches="tight")


# ***************************************************************************

# 'Supported Android Version with No. of Reviews based on Games
game_data = byCategory.get_group('GAME')

plt.figure(figsize=(10, 8))
chart6 = sns.swarmplot(data=game_data, x='osVer', y='reviews', hue='rated')
# chart6.legend_.remove()
plt.margins(0.02)
plt.title('Supported Android Version with No. of Reviews based on Games', fontsize=20)
plt.xlabel('Android Version', fontsize=20)
plt.ylabel('No. of Reviews', fontsize=20)
# plt.ylim(0, None)
chart6.set_yscale('log')
chart6.set_xticklabels(chart6.get_xticklabels(),
                       rotation=45, horizontalalignment='right')
fig_6 = chart6.get_figure()
fig_6.savefig("./Data/swarm_plot.png", dpi=300, bbox_inches="tight")


# ***************************************************************************f

# Box Plot Family Applications with Supported Android Version and their User Reviews

family_data = byCategory.get_group('FAMILY')
plt.figure(figsize=(15, 8))
chart7 = sns.boxplot(data=family_data, x='osVer', y='reviews', hue='rated')
plt.margins(0.02)
plt.title('Family Applications with Supported Android Version and their User Reviews', fontsize=20)
plt.xlabel('Android Version', fontsize=20)
plt.ylabel('No. of Reviews', fontsize=20)
chart7.set_yscale('log')
chart7.set_xticklabels(chart7.get_xticklabels(),
                       rotation=45, horizontalalignment='right')
fig_7 = chart7.get_figure()
fig_7.savefig("./Data/box_plot.png", dpi=300, bbox_inches="tight")


# ***************************************************************************

bycategory_count = byCategory.count()
bycategory_count_sr = bycategory_count.iloc[:, 0]

categories = {}
count = 0

for index, row in bycategory_count_sr.items():
    categories[index] = row


categories = sorted(categories.items(),
                    key=operator.itemgetter(1), reverse=True)

top_categories = {}
for item, element in categories:
    if (count < 20):
        top_categories[item] = element
        count += 1

# Pie plotting

output_file("./Data/pie.html")

x = top_categories

data = pd.Series(x).reset_index(name='value').rename(
    columns={'index': 'country'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20c[len(x)]

p = figure(plot_height=600, plot_width=800, title="Top 20 Application Categories Based on Application Number", toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='country', source=data)

p.axis.axis_label = None
p.axis.visible = False
p.grid.grid_line_color = None
show(p)


