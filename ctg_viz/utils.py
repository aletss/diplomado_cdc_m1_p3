import pandas as pd

def check_data_completeness_alejandro_sosa_murguia(df) -> pd.DataFrame:
    """Generate a report of data completeness for each column in the dataframe.

    Args:
        df (pd.DataFrame): Input dataframe.

    Returns:
        pd.DataFrame: Dataframe containing completeness report.
    """
    columns = ['Column', 'Data Type', 'Non-Null Count', 'Null Count', 'Completeness (%)', 'Mean', 'Median', 'Std Dev', 'Min', 'Max']
    report = []

    total_rows = df.shape[0]

    for col in df.columns:
        non_null_count = df[col].count()
        null_count = total_rows - non_null_count
        completeness = (non_null_count / total_rows) * 100
        data_type = df[col].dtype

        if pd.api.types.is_numeric_dtype(df[col]):
            mean = df[col].mean()
            median = df[col].median()
            std_dev = df[col].std()
            min_val = df[col].min()
            max_val = df[col].max()
        else:
            mean = median = std_dev = min_val = max_val = None

        report.append({
            'Column': col,
            'Data Type': data_type,
            'Non-Null Count': non_null_count,
            'Null Count': null_count,
            'Completeness (%)': completeness,
            'Mean': mean,
            'Median': median,
            'Std Dev': std_dev,
            'Min': min_val,
            'Max': max_val
        })

    return pd.DataFrame(report, columns=columns)
