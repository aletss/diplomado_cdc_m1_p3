import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# scatter chart using matplotlib
def scatter_matplotlib(df, column_x, column_y, column_category) -> plt.Figure:
    """Plots a scatter chart using matplotlib library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        column_x (str): Column with values to be plotted on the x axis
        column_y (str): Column with values to be plotted on the y axis
        column_category (str): Column with values to group by category

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    figsize=(8, 6)
    fig, ax = plt.subplots(figsize=figsize)
    
    categories = df[column_category].unique()
    for category in categories:
        subset = df[df[column_category] == category]
        ax.scatter(subset[column_x], subset[column_y], label=category, alpha=0.7)
    
    ax.set_xlabel(column_x)
    ax.set_ylabel(column_y)
    ax.set_title(f'Scatter Plot of {column_y} vs {column_x} by {column_category}')
    ax.legend()
    
    plt.tight_layout()
    return fig, ax

# scatter chart using seaborn
def scatter_seaborn(df, column_x, column_y, column_category) -> plt.Figure:
    """Plots a scatter chart using seaborn library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        column_x (str): Column with values to be plotted on the x axis
        column_y (str): Column with values to be plotted on the y axis
        column_category (str): Column with values to group by category

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    figsize=(8, 6)
    fig, ax = plt.subplots(figsize=figsize)
    
    sns.scatterplot(data=df, x=column_x, y=column_y, hue=column_category, alpha=0.7, ax=ax)
    
    ax.set_xlabel(column_x)
    ax.set_ylabel(column_y)
    ax.set_title(f'Scatter Plot of {column_y} vs {column_x} by {column_category}')
    ax.legend()
    
    plt.tight_layout()
    return fig, ax

# scatter chart using plotly
def scatter_plotly(df, column_x, column_y, column_category) -> plt.Figure:
    """Plots a scatter chart using plotly library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        column_x (str): Column with values to be plotted on the x axis
        column_y (str): Column with values to be plotted on the y axis
        column_category (str): Column with values to group by category

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    fig = px.scatter(
        df,
        x=column_x,
        y=column_y,
        color=column_category,
        title=f'Scatter Plot of {column_y} vs {column_x} by {column_category}',
        labels={column_x: column_x, column_y: column_y}
    )
    return fig
