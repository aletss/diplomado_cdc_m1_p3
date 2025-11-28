import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.figure_factory as ff

# heatmap chart using matplotlib only
def corr_heatmap_matplotlib(df, columns, correlation_method='pearson') -> plt.Figure:
    """Plots a heatmap chart using matplotlib library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        columns (list): Columns with values to be used to compute correlation matrix
        correlation_method (str, optional): Correlation method that will be used. Can be pearson or spearman. Default is pearson.

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    # Validate correlation method
    if correlation_method not in ['pearson', 'spearman']:
        raise ValueError("correlation_method must be 'pearson' or 'spearman'")
    
    # Filter dataframe to only include specified columns
    df_subset = df[columns].copy()
    
    # Compute correlation matrix
    corr_matrix = df_subset.corr(method=correlation_method)
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create heatmap using imshow
    im = ax.imshow(corr_matrix, cmap='coolwarm', aspect='auto', 
                   vmin=-1, vmax=1, interpolation='nearest')
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Correlation Coefficient', rotation=270, labelpad=20, fontsize=11)
    
    # Set ticks and labels
    n_cols = len(columns)
    ax.set_xticks(np.arange(n_cols))
    ax.set_yticks(np.arange(n_cols))
    ax.set_xticklabels(columns, rotation=45, ha='right', fontsize=10)
    ax.set_yticklabels(columns, fontsize=10)
    
    # Add correlation values as text annotations
    for i in range(n_cols):
        for j in range(n_cols):
            value = corr_matrix.iloc[i, j]
            # Use white text for dark backgrounds, black for light
            text_color = 'white' if abs(value) > 0.5 else 'black'
            ax.text(j, i, f'{value:.2f}', 
                   ha='center', va='center', 
                   color=text_color, fontsize=9)
    
    # Add title
    method_title = correlation_method.capitalize()
    ax.set_title(f'{method_title} Correlation Heatmap', 
                fontsize=14, fontweight='bold', pad=20)
    
    # Add grid
    ax.set_xticks(np.arange(n_cols + 1) - 0.5, minor=True)
    ax.set_yticks(np.arange(n_cols + 1) - 0.5, minor=True)
    ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5)
    ax.tick_params(which='minor', size=0)
    
    # Adjust layout
    plt.tight_layout()
    
    return fig

# heatmap chart using seaborn
def corr_heatmap_seaborn(df, columns, correlation_method='pearson') -> plt.Figure:
    """Plots a heatmap chart using seaborn library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        columns (list): Columns with values to be used to compute correlation matrix
        correlation_method (str, optional): Correlation method that will be used. Can be pearson or spearman. Default is pearson.

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    # Validate correlation method
    if correlation_method not in ['pearson', 'spearman']:
        raise ValueError("correlation_method must be 'pearson' or 'spearman'")
    
    # Filter dataframe to only include specified columns
    df_subset = df[columns].copy()
    
    # Compute correlation matrix
    corr_matrix = df_subset.corr(method=correlation_method)
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create heatmap using seaborn
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', 
                vmin=-1, vmax=1, square=True, cbar_kws={"label": "Correlation Coefficient"}, ax=ax)
    
    # Add title
    method_title = correlation_method.capitalize()
    ax.set_title(f'{method_title} Correlation Heatmap', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Adjust layout
    plt.tight_layout()
    
    return fig

# heatmap chart using plotly
def corr_heatmap_plotly(df, columns, correlation_method='pearson') -> plt.Figure:
    """Plots a heatmap chart using plotly library

    Args:
        df (pandas.DataFrame): Dataframe with data to plot
        columns (list): Columns with values to be used to compute correlation matrix
        correlation_method (str, optional): Correlation method that will be used. Can be pearson or spearman. Default is pearson.

    Returns:
        plt.Figure: Returns a matplotlib Figure object
    """
    # Validate correlation method
    if correlation_method not in ['pearson', 'spearman']:
        raise ValueError("correlation_method must be 'pearson' or 'spearman'")
    
    # Filter dataframe to only include specified columns
    df_subset = df[columns].copy()
    
    # Compute correlation matrix
    corr_matrix = df_subset.corr(method=correlation_method)
    
    # Create heatmap using plotly
    fig = ff.create_annotated_heatmap(
        z=corr_matrix.values,
        x=list(corr_matrix.columns),
        y=list(corr_matrix.index),
        colorscale='RdBu',
        zmin=-1,
        zmax=1,
        annotation_text=np.round(corr_matrix.values, 2).astype(str).tolist(),
        showscale=True,
        colorbar=dict(title='Correlation Coefficient')
    )
    
    # Add title
    method_title = correlation_method.capitalize()
    fig.update_layout(
        title=f'{method_title} Correlation Heatmap',
        title_x=0.5,
        width=800,
        height=600
    )
    
    return fig