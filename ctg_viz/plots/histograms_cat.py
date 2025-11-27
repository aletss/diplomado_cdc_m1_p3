
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns

def histogram_matplotlib(df, column_values, column_category=None, show_kde=False, show_density=False):
    """Plot histograms with optional category splitting and KDE overlay.

    Args:
        df (pandas.DataGrame): The input dataframe containing the data.
        column_values (str): Name of the column containing numeric values to plot.
        column_category (str, optional): Name of the column to split data by categories. If None, plots single histogram.. Defaults to None.
        show_kde (bool, optional): Whether to overlay a Kernel Density Estimate curve.. Defaults to False.

    Returns:
        fig, ax : matplotlib figure and axes objects
    """
    BINS = 30
    ALPHA = 0.6
    FIGSIZE = (10, 6)
    
    fig, ax = plt.subplots(figsize=FIGSIZE)
    
    if column_category is None:
        # Single histogram without categories
        data = df[column_values].dropna()
        ax.hist(data, bins=BINS, alpha=ALPHA, edgecolor='black', density=(show_kde or show_density))
        
        if show_kde and len(data) > 1 and data.std() > 0:
            x = np.linspace(data.min(), data.max(), 200)
            kde = stats.gaussian_kde(data)
            ax.plot(x, kde(x), linewidth=2, label='KDE')
            ax.legend()
    else:
        # Multiple histograms split by category
        categories = df[column_category].dropna().unique()
        colors = plt.cm.tab10(np.linspace(0, 1, len(categories)))
        
        for cat, color in zip(categories, colors):
            data = df[df[column_category] == cat][column_values].dropna()
            
            if len(data) < 2:
                continue
                
            ax.hist(data, bins=BINS, alpha=ALPHA, edgecolor='black', 
                    label=str(cat), color=color, density=(show_kde or show_density))
            
            if show_kde and len(data) > 1 and data.std() > 0:
                x = np.linspace(data.min(), data.max(), 200)
                kde = stats.gaussian_kde(data)
                ax.plot(x, kde(x), linewidth=2, color=color)
        
        ax.legend(title=column_category)
    
    ax.set_xlabel(column_values)
    ax.set_ylabel('Density' if show_kde else 'Frequency')
    ax.set_title(f'Distribution of {column_values}' + 
                 (f' by {column_category}' if column_category else ''))
    
    plt.tight_layout()
    return fig, ax



def histogram_seaborn(df, column_values, column_category=None, show_kde=False, show_density=False):
    """Plot histograms with optional category splitting and KDE overlay.

    Args:
        df (pandas.DataGrame): The input dataframe containing the data.
        column_values (str): Name of the column containing numeric values to plot.
        column_category (str, optional): Name of the column to split data by categories. If None, plots single histogram.. Defaults to None.
        show_kde (bool, optional): Whether to overlay a Kernel Density Estimate curve.. Defaults to False.
        show_density (bool, optional): Whether to show density instead of frequency.. Defaults to False.

    Returns:
        fig, ax : matplotlib figure and axes objects
    """
    BINS = 30
    ALPHA = 0.6
    FIGSIZE = (10, 6)
    
    fig, ax = plt.subplots(figsize=FIGSIZE)
    
    sns.histplot(
        data=df,
        x=column_values,
        hue=column_category,
        kde=show_kde,
        stat='density' if (show_density or show_kde) else 'count',
        common_norm=False,
        bins=BINS,
        alpha=ALPHA,
        edgecolor='black',
        ax=ax
    )
    
    ax.set_xlabel(column_values)
    ax.set_ylabel('Density' if show_density else 'Frequency')
    ax.set_title(f'Distribution of {column_values}' + 
                 (f' by {column_category}' if column_category else ''))
    
    plt.tight_layout()
    return fig, ax

def histogram_plotly(df, column_values, column_category=None, show_kde=False, show_density=False):
    """Plot histograms with optional category splitting and KDE overlay.

    Args:
        df (pandas.DataGrame): The input dataframe containing the data.
        column_values (str): Name of the column containing numeric values to plot.
        column_category (str, optional): Name of the column to split data by categories. If None, plots single histogram.. Defaults to None.
        show_kde (bool, optional): Whether to overlay a Kernel Density Estimate curve.. Defaults to False.
        show_density (bool, optional): Whether to show density instead of frequency.. Defaults to False.

    Returns:
        fig: plotly figure object
    """
    BINS = 30
    OPACITY = 0.6
    WIDTH = 1000
    HEIGHT = 600
    
    histnorm = 'probability density' if show_density else None
    
    fig = px.histogram(
        df,
        x=column_values,
        color=column_category,
        nbins=BINS,
        opacity=OPACITY,
        histnorm=histnorm,
        barmode='overlay',
        title=f'Distribution of {column_values}' + (f' by {column_category}' if column_category else '')
    )
    
    if show_kde:
        if column_category is None:
            data = df[column_values].dropna()
            if len(data) > 1 and data.std() > 0:
                x_range = np.linspace(data.min(), data.max(), 200)
                kde = stats.gaussian_kde(data)
                fig.add_trace(go.Scatter(x=x_range, y=kde(x_range), mode='lines', name='KDE'))
        else:
            categories = df[column_category].dropna().unique()
            colors = px.colors.qualitative.Plotly
            
            for i, cat in enumerate(categories):
                data = df[df[column_category] == cat][column_values].dropna()
                if len(data) > 1 and data.std() > 0:
                    x_range = np.linspace(data.min(), data.max(), 200)
                    kde = stats.gaussian_kde(data)
                    color = colors[i % len(colors)]
                    fig.add_trace(go.Scatter(
                        x=x_range, 
                        y=kde(x_range), 
                        mode='lines', 
                        name=f'{cat} KDE',
                        line=dict(color=color)
                    ))
    
    fig.update_layout(
        xaxis_title=column_values,
        yaxis_title='Density' if show_density else 'Frequency',
        width=WIDTH,
        height=HEIGHT
    )
    
    return fig

# Example usage:
if __name__ == "__main__":
    import pandas as pd
    
    # Create sample data
    np.random.seed(42)
    df = pd.DataFrame({
        'value': np.concatenate([
            np.random.normal(50, 10, 200),
            np.random.normal(70, 15, 200),
            np.random.normal(40, 8, 200)
        ]),
        'category': ['A'] * 200 + ['B'] * 200 + ['C'] * 200
    })
    
    # Plot without categories
    fig1, ax1 = histogram_matplotlib(df, 'value', show_kde=True)
    
    # Plot with categories
    fig2, ax2 = histogram_matplotlib(df, 'value', 'category', show_kde=True)
    
    
    df2 = pd.read_csv('D:/m1_practica3/CTG.csv')
    print(df2.head())
    fig3, ax3 = histogram_matplotlib(df2, column_values='e', column_category='DP', show_kde=True)

    fig4, ax4 = histogram_matplotlib(df2, column_values='e', column_category='DP', show_density=True)

    fig5, ax5 = histogram_seaborn(df2, column_values='e', column_category='DP', show_density=True)
    fig6, ax6 = histogram_seaborn(df2, column_values='e', column_category='DP', show_kde=True)
    fig7, ax7 = histogram_seaborn(df, 'value', 'category', show_kde=True, show_density=True)
    
    # plt.show()


    fig8 = histogram_plotly(df, 'value', 'category', show_kde=True, show_density=True)
    fig8.show()
    fig9 = histogram_plotly(df2, 'e', 'DP', show_kde=True, show_density=True)
    fig9.show()
