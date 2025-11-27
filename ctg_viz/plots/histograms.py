#import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.figure_factory as ff
from scipy import stats

df = pd.read_csv('D:/m1_practica3/CTG.csv')

# Default color palettes
MATPLOTLIB_COLORS = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
                     '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

def histogram_matplotlib(df, columns, show_density=False, show_kde=False, bins=30, alpha=0.7, chart_title='Histogram') -> plt.figure:
    fig, ax = plt.subplots(figsize=(8, 5))
    
    for i, column in enumerate(columns):
        values = df[column]
        color = MATPLOTLIB_COLORS[i % len(MATPLOTLIB_COLORS)]

        ax.hist(values, bins=bins, alpha=alpha, label=column, 
                    density=(show_density), edgecolor='black'
                    , color=color)

        if show_kde:
            x_range = np.linspace(min(values), max(values), 20)
            kde = stats.gaussian_kde(values)
            ax.plot(x_range, kde(x_range), '-', linewidth=2, label=f'{column} KDE', color=color, alpha=0.7)

        if show_density:
            x_range = np.linspace(min(values), max(values), 20)
            mu, std = np.mean(values), np.std(values)
            density = stats.norm.pdf(x_range, mu, std)
            ax.plot(x_range, density, '--', linewidth=2, label=f'{column} Normal', color=color, alpha=0.7)

        

    # Add labels and a title for clarity
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title(chart_title)
    ax.legend()

    return fig

def histogram_seaborn(df, columns, show_kde=False, show_density=False, chart_title='Histogram'):
    fig, ax = plt.subplots(figsize=(8, 5))
    
    for column in columns:
        sns.histplot(data=df, x=column, kde=show_kde, ax=ax, stat='density' if show_density else 'frequency', label=column)
    
    ax.set_title(chart_title)
    ax.legend()
    
    return fig


def histogram_plotly(df, columns, bins=30, show_kde=False, show_density=False, chart_title='Histogram'):
    """Returns a plotly Figure object."""
    histnorm = 'probability density' if (show_density or show_kde) else None
    
    fig = px.histogram(
        df,
        x=columns,
        barmode='overlay',
        histnorm=histnorm,
        title=chart_title,
        opacity=0.7
    )
    
    if show_kde:
        colors = px.colors.qualitative.Plotly
        for i, col in enumerate(columns):
            data = df[col].dropna()
            x_range = np.linspace(data.min(), data.max(), 200)
            kde = stats.gaussian_kde(data)
            y_kde = kde(x_range)
            
            fig.add_trace(go.Scatter(
                x=x_range,
                y=y_kde,
                mode='lines',
                name=f'{col} (KDE)',
                line=dict(color=colors[i % len(colors)], width=2)
            ))
    
    fig.update_layout(
        xaxis_title='Value',
        yaxis_title='Density' if (show_density or show_kde) else 'Count',
        legend_title='Variable',
        bargap=0.1
    )
    
    return fig