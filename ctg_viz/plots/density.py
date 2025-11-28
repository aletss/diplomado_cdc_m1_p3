import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

# density (kde) chart using matplotlib
def density_matplotlib(df, column_values, column_category) -> plt.Figure:
    """Plots a density chart using matplotlib library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        column_values (str): Column with values to be used for densities
        column_category (str): Column with values to group by category

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    figsize=(8, 6)
    fig, ax = plt.subplots(figsize=figsize)
    
    categories = df[column_category].unique()
    for category in categories:
        subset = df[df[column_category] == category]
        if subset[column_values].unique().shape[0] < 2:
            continue
        subset[column_values].plot(kind='kde', ax=ax, label=category)
    
    ax.set_xlabel(column_values)
    ax.set_title(f'Density Plot of {column_values} by {column_category}')
    ax.legend()
    
    plt.tight_layout()
    return fig, ax

# density (kde) chart using seaborn
def density_seaborn(df, column_values, column_category) -> plt.Figure:
    """Plots a density chart using seaborn library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        column_values (str): Column with values to be used for densities
        column_category (str): Column with values to group by category

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    figsize=(8, 6)
    fig, ax = plt.subplots(figsize=figsize)
    
    for category in df[column_category].unique():
        subset = df[df[column_category] == category]
        if subset[column_values].unique().shape[0] < 2:
            continue
        sns.kdeplot(data=subset, x=column_values, hue=column_category, ax=ax, label=category)
    
    ax.set_xlabel(column_values)
    ax.set_title(f'Density Plot of {column_values} by {column_category}')
    ax.legend()
    
    return fig, ax

# density (kde) chart using plotly
def density_plotly(df, column_values, column_category) -> plt.Figure:
    """Plots a density chart using plotly library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        column_values (str): Column with values to be used for densities
        column_category (str): Column with values to group by category

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    # Group by category and create the necessary lists
    hist_data = []
    group_labels = []

    for category in df['DP'].unique():
        subset = df[df['DP'] == category]['b'].dropna()
        if subset.nunique() < 2:
            continue
        hist_data.append(subset)
        group_labels.append(category)

    # Create distplot with curve_type set to 'normal'
    fig = ff.create_distplot(hist_data, group_labels, show_hist=False,  show_rug=False)
    fig
    return fig
