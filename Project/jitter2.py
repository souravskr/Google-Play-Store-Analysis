from cycler import cycler
import calendar
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.layouts import column
from bokeh.plotting import figure, show, output_file
from bokeh.transform import jitter


# def read_file(csv_file):
#     df = pd.read_csv(csv_file)
#     df['Year'] = pd.DatetimeIndex(df['lastUpdated']).year
#     df['Month'] = pd.DatetimeIndex(df['lastUpdated']).month
#     df['lastUpdated'] = pd.to_datetime(df['lastUpdated'])
#     df['rating'].fillna(df['rating'].mean(), inplace=True)
#     df['rating'] = df['rating'].round(1)
#     df['Month'] = df['Month'].apply(lambda x: calendar.month_abbr[x])
#     return df


# def plot_jitter2(data_frame):
#     pricing = sorted(data_frame.price.unique())
#     jitter_plot = figure(plot_width=1600, plot_height=800,
#                          title="Application Rating Vs Price of Applications", y_axis_type='log')

#     jitter_plot.xgrid.grid_line_color = "red"
#     jitter_plot.xaxis[0].ticker = pricing
#     jitter_plot.circle(x=jitter('price', 0.4), y='installs',
#                        size=9, alpha=0.4, source=data_frame, color="red")
#     jitter_plot.xaxis.axis_label = 'price'
#     jitter_plot.yaxis.axis_label = 'No. of Installations'
#     output_file("./Data/jitter2.html")
#     show(jitter_plot)
#     return True


# if __name__ == "__main__":

#     try:
#         # call file download process
#         plot_jitter2(read_file('./Data/cleanData.csv'))

#     except Exception as e:
#         print(e)
