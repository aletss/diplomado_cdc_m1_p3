import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def boxplot_matplotlib(df, column_values, column_cathegory=None) -> plt.Figure:
    """Plots boxplot using matplotlib library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        column_values (str): Column with values to plot
        column_cathegory (str, optional): Column with categories to group the values. Defaults to None.

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    figsize=(8, 6)
    fig, ax = plt.subplots(figsize=figsize)
    if column_cathegory:
        data_to_plot = [df[df[column_cathegory] == cat][column_values].dropna() for cat in df[column_cathegory].unique()]
        ax.boxplot(data_to_plot, labels=df[column_cathegory].unique(), patch_artist=True)
        ax.set_title(f'Boxplot of {column_values} by {column_cathegory}')
    else:
        ax.boxplot(df[column_values].dropna(), patch_artist=True)
        ax.set_title(f'Boxplot of {column_values}')

    ax.set_ylabel(column_values)
    plt.tight_layout()
    return fig, ax

# boxplot using seaborn
def boxplot_seaborn(df, column_values, column_cathegory=None) -> plt.Figure:
    """Plots boxplot using seaborn library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        column_values (str): Column with values to plot
        column_cathegory (str, optional): Column with categories to group the values. Defaults to None.

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    figsize=(8, 6)
    fig, ax = plt.subplots(figsize=figsize)
    if column_cathegory:
        sns.boxplot(x=column_cathegory, y=column_values, data=df, ax=ax)
        ax.set_title(f'Boxplot of {column_values} by {column_cathegory}')
    else:
        sns.boxplot(y=column_values, data=df, ax=ax)
        ax.set_title(f'Boxplot of {column_values}')

    ax.set_ylabel(column_values)
    plt.tight_layout()
    return fig, ax

# boxplot using plotly
def boxplot_plotly(df, column_values, column_cathegory=None) -> plt.Figure:
    """Plots boxplot using seaborn library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        column_values (str): Column with values to plot
        column_cathegory (str, optional): Column with categories to group the values. Defaults to None.

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    

    if column_cathegory:
        fig = px.box(df, x=column_cathegory, y=column_values, title=f'Boxplot of {column_values} by {column_cathegory}')
    else:
        fig = px.box(df, y=column_values, title=f'Boxplot of {column_values}')

    fig.update_layout(yaxis_title=column_values)
    return fig
