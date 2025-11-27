import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# line chart using matplotlib
def line_matplotlib(df, columns, column_index=None) -> plt.Figure:
    """Plots a line chart using matplotlib library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        columns (list): List of colums with values to be plotted
        column_index (str, optional): Column with values for x axis

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    figsize=(8, 6)
    fig, ax = plt.subplots(figsize=figsize)
    
    if column_index:
        df = df.sort_values(column_index)
        for col in columns:
            ax.plot(df[column_index], df[col], label=col)
        ax.set_title(f'Line Plot of {", ".join(columns)} by {column_index}')
        ax.set_xlabel(column_index)
    else:
        for col in columns:
            ax.plot(df.index, df[col], label=col)
        ax.set_title(f'Line Plot of {", ".join(columns)}')
        ax.set_xlabel('Index')

    ax.legend()

    return fig, ax

# line chart using seaborn
def line_seaborn(df, columns, column_index=None) -> plt.Figure:
    """Plots a line chart using seaborn library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        columns (list): List of colums with values to be plotted
        column_index (str, optional): Column with values for x axis

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    figsize=(8, 6)
    fig, ax = plt.subplots(figsize=figsize)
    
    if column_index:
        df = df.sort_values(column_index)
        for col in columns:
            sns.lineplot(x=column_index, y=col, data=df, ax=ax, label=col, estimator=None)
        ax.set_title(f'Line Plot of {", ".join(columns)} by {column_index}')
        ax.set_xlabel(column_index)
    else:
        for col in columns:
            sns.lineplot(x=df.index, y=col, data=df, ax=ax, label=col, estimator=None)
        ax.set_title(f'Line Plot of {", ".join(columns)}')
        ax.set_xlabel('Index')

    ax.legend()

    return fig, ax

# line chart using plotly
def line_plotly(df, columns, column_index=None) -> plt.Figure:
    """Plots a line chart using plotly library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        columns (list): List of colums with values to be plotted
        column_index (str, optional): Column with values for x axis

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    if column_index:
        df = df.sort_values(column_index)
        fig = px.line(df, x=column_index, y=columns, title=f'Line Plot of {", ".join(columns)} by {column_index}')
    else:
        fig = px.line(df, x=df.index, y=columns, title=f'Line Plot of {", ".join(columns)}')
    
    return fig