import streamlit as st
import numpy as np
import pandas as pd

# Import your plotting functions

from ctg_viz.plots import histograms, boxplots, barplots, density, scatter, violin, heatmap


# Load your data
data_path = 'data/CTG.csv' # Data must be stored in the data/ folder after you download the file. You can also modify the path
df = pd.read_csv(data_path)

# Charts
# 1.1 Histograma
columns = ['b', 'e']
fig_hist, ax = histograms.histogram_matplotlib(df[columns].dropna(), columns, show_density=True, show_kde=True)

# 2.1 Boxplots
category_column = 'DP'
fig_box, ax = boxplots.boxplot_seaborn(df, 'b', category_column)

# 2.2 Barplots
category_column = 'DP'
fig_bar = barplots.barh_plotly(df, category_column)

# 3.5 Scatterplot
column_x = 'b'
column_y = 'e'
fig_scatter = scatter.scatter_plotly(df, column_x, column_y, 'DP')

# 3.5 density
fig_density, ax = density.density_seaborn(df, 'b', 'DP')

# 3.6 density
fig_violin, ax = violin.violin_seaborn(df, 'b', 'DP')

# 3.7 density
columns = ['b', 'e', 'LB']
corr_method = 'spearman'
fig_heatmap = heatmap.corr_heatmap_plotly(df, columns, corr_method)


st.title("Multi-Library Plot Dashboard")

st.header("Matplotlib Histogram")
st.pyplot(fig_hist)

st.header("Seaborn Boxplot")
st.pyplot(fig_box)

st.header("Plotly Horizontal Bar (Interactive!)")
st.plotly_chart(fig_bar) # use plotly_chart for plotly express

st.header("Plotly Scatter (Interactive!)")
st.plotly_chart(fig_scatter) # use plotly_chart for plotly express

st.header("Seaborn Density")
st.pyplot(fig_density)

st.header("Seaborn Violin")
st.pyplot(fig_violin)

st.header("Plotly Heatmap with correlations (Interactive!)")
st.plotly_chart(fig_heatmap) # use plotly_chart for plotly express
