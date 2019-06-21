#************************************Avg Size by Category***************************************
import pandas as pd
import numpy as np
from bokeh.models import PrintfTickFormatter
formatter = PrintfTickFormatter(format='%fM')
import holoviews as hv
from geoviews import dim, opts
hv.extension('bokeh')
renderer = hv.renderer('bokeh')

df1 = df[df['size'] != 'Varies with device']

df1.loc[df1['size'].str[-1] == 'k', ['size']] =pd.to_numeric(df1['size'].str[:-1], errors='coerce')/1000 

df1['size']=df1['size'].str[0:-1]
df1['size'] = pd.to_numeric(df1['size'], errors='coerce')
category_size = df1[['category', 'size']].dropna();

category_size = category_size.groupby('category', as_index=False).mean()

category_size.set_index('category', inplace=True)
v = category_size["size"].values.tolist()
i = category_size["size"].index.tolist()

bars = hv.Bars((i, v), hv.Dimension('category'), 'size').opts(tools=['hover'],xformatter= formatter,show_legend=False,fill_color=dim('category').str(),cmap='coolwarm')#  '#E933FF'
t = (bars.relabel('Avg. size by category').opts(invert_axes=True,height = 650, width=1000) )

renderer.save(t,"./Data/average_size")

# ***************************************************************************

