import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# violin chart using matplotlib only
def violin_matplotlib(df, column_values, column_category) -> plt.Figure:
    """Plots a violin chart using matplotlib library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        column_values (str): Column with values to be used for densities
        column_category (str): Column with values to group by category

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    figsize=(8, 6)
    fig, ax = plt.subplots(figsize=figsize)
    
    data_to_plot = [df[df[column_category] == cat][column_values].dropna() for cat in df[column_category].unique()]
    ax.violinplot(data_to_plot, showmeans=False, showmedians=True)
    ax.set_xticks(range(1, len(df[column_category].unique()) + 1))
    ax.set_xticklabels(df[column_category].unique())
    
    ax.set_xlabel(column_category)
    ax.set_ylabel(column_values)
    ax.set_title(f'Violin Plot of {column_values} by {column_category}')
    
    plt.tight_layout()
    return fig, ax

# violin chart using seaborn 
def violin_seaborn(df, column_values, column_category) -> plt.Figure:
    """Plots a violin chart using seaborn library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        column_values (str): Column with values to be used for densities
        column_category (str): Column with values to group by category

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    figsize=(8, 6)
    fig, ax = plt.subplots(figsize=figsize)
    
    sns.violinplot(x=column_category, y=column_values, data=df, ax=ax)
    
    ax.set_xlabel(column_category)
    ax.set_ylabel(column_values)
    ax.set_title(f'Violin Plot of {column_values} by {column_category}')
    
    plt.tight_layout()
    return fig, ax

# violin chart using plotly 
def violin_plotly(df, column_values, column_category) -> plt.Figure:
    """Plots a violin chart using plotly library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        column_values (str): Column with values to be used for densities
        column_category (str): Column with values to group by category

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    # Remove categoreies with less than 2 unique values
    valid_categories = df[column_category].value_counts()[df[column_category].value_counts() >= 2].index
    df = df[df[column_category].isin(valid_categories)]
    
    # Create the violin plot
    fig = px.violin(df, y=column_values, x=column_category, box=True) 

    fig.update_layout(
        title=f'Violin Plot of {column_values} by {column_category}',
        xaxis_title=column_category,
        yaxis_title=column_values
    )

    return fig