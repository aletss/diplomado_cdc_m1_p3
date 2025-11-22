import pandas as pd

def classify_column_types(df: pd.DataFrame) -> dict:
    """Classify columns into categorical, continuous numerical, and discrete numerical.

    Args:
        df (pd.DataFrame): Input dataframe.
    Returns:
        dict: Dictionary with keys 'categorical', 'continuous_numerical', and 'discrete_numerical' containing lists of column names.
    """
    
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    numerical_cols = df.select_dtypes(include=['number']).columns.tolist()

    # Contiuous (more than 10 unique values with numeric type)
    continuous_numerical_cols = [col for col in numerical_cols if df[col].nunique() > 10]
    # Discretes (10 or less unique values with numeric type)
    discrete_numerical_cols = [col for col in numerical_cols if df[col].nunique() <= 10]

    return {
        'categorical': categorical_cols,
        'continuous_numerical': continuous_numerical_cols,
        'discrete_numerical': discrete_numerical_cols
    }
