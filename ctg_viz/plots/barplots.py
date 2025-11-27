import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# horizontal bar using matplotlib
def barh_matplotlib(df, column_values) -> plt.Figure:
    """Plots boxplot using matplotlib library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        column_values (str): Column with values to plot

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    figsize=(8, 6)
    fig, ax = plt.subplots(figsize=figsize)

    data = df[column_values].value_counts().sort_values()
    
    ax.barh(y=data.index, width=data.values)
    ax.invert_yaxis()
    ax.set_title(f'Horizontal Barplot of {column_values}')

    ax.set_xlabel(column_values)
    plt.tight_layout()
    return fig, ax

# horizontal bar using seaborn
def barh_seaborn(df, column_values) -> plt.Figure:
    """Plots boxplot using seaborn library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        column_values (str): Column with values to plot

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    figsize=(8, 6)
    fig, ax = plt.subplots(figsize=figsize)

    data = df[column_values].value_counts().sort_values().reset_index()
    data.columns = [column_values, 'counts']
    data[column_values] = data[column_values].astype(str)
    
    sns.barplot(x='counts', y=column_values, data=data, ax=ax, orient='h')
    ax.invert_yaxis()
    ax.set_title(f'Horizontal Barplot of {column_values}')

    ax.set_xlabel(column_values)
    plt.tight_layout()
    return fig, ax

# horizontal bar using plotly
def barh_plotly(df, column_values) -> plt.Figure:
    """Plots boxplot using plotly library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        column_values (str): Column with values to plot

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """

    data = df[column_values].value_counts().sort_values().reset_index()
    data.columns = [column_values, 'counts']
    data[column_values] = data[column_values].astype(str)

    fig = px.bar(data, x='counts', y=column_values, orientation='h', title=f'Horizontal Barplot of {column_values}')
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    
    return fig
