import pandas as pd
from sklearn.impute import KNNImputer
from scipy import stats
import numpy as np

# Delete columns with more than 20% missing values
def drop_columns_with_missing_values(df, threshold=0.2) -> pd.DataFrame:
    """Delete columns that have more than a threshold percentage of nulls

    Args:
        dataframe (pd.DataFrame): Dataframe
        threshold (float, optional): Minimum value of nulls ration for columns to be droped. Defaults to 0.2.
    """
    columns_to_drop = []

    for col in df.columns:
        if df[col].isnull().mean() > threshold:
            columns_to_drop.append(col)

    columns_to_keep = [col for col in df.columns if col not in columns_to_drop]
    return df[columns_to_keep]

def imput_values(df, numeric_strategy='median') -> pd.DataFrame:
    """Imput missing values with median, mean or knn for numeric columns and mode for categorical columns

    Args:
        dataframe (pd.DataFrame): Dataframe
        numeric_strategy (str, optional): Strategy to imput numeric columns. Defaults to 'median' for numerical and 'mode' for categorical. Possible values are 'mean', 'median','mode' and 'knn'.
    """
    df_inputed = df.copy(deep=True) 
    if numeric_strategy not in ['mean', 'median', 'knn']:
        raise ValueError("Invalid numeric_strategy. Possible values are 'mean', 'median', and 'knn'.")

    numeric_cols = df_inputed.select_dtypes(include=['number']).columns
    categorical_cols = df_inputed.select_dtypes(include=['object', 'category']).columns

    print('Numeric columns to impute:', numeric_cols.tolist())
    print('Categorical columns to impute:', categorical_cols.tolist())

    # Impute numeric columns
    if numeric_strategy in ['mean', 'median']:
        for col in numeric_cols:
            if numeric_strategy == 'mean':
                impute_value = df_inputed[col].mean()
            if numeric_strategy == 'median':
                impute_value = df_inputed[col].median()
            df_inputed[col] = df_inputed[col].fillna(impute_value)
    elif numeric_strategy == 'knn':
        imputer = KNNImputer()
        print('Using KNN Imputer for numeric columns')
        df_inputed[numeric_cols] = imputer.fit_transform(df_inputed[numeric_cols])

    # Impute categorical columns
    for col in categorical_cols:
        mode_value = df_inputed[col].mode()[0]
        df_inputed[col] = df_inputed[col].fillna(mode_value)

    return df_inputed

# Remove outliers with IQR or z-score, both methods for numeric columns
def remove_outliers(df, columns=[], method='iqr', z_threshold=3.0) -> pd.DataFrame:
    """Remove outliers from numeric columns using IQR or z-score method

    Args:
        dataframe (pd.DataFrame): Dataframe
        method (str, optional): Method to remove outliers. Defaults to 'iqr'. Possible values are 'iqr' and 'zscore'.
        z_threshold (float, optional): Z-score threshold to identify outliers. Defaults to 3.0.
    """
    df_threatment = df.copy(deep=True)
    initial_rows = df_threatment.shape[0]

    if columns:
        numeric_cols = df_threatment[columns].select_dtypes(include=['number']).columns
    else:
        numeric_cols = df_threatment.select_dtypes(include=['number']).columns
    
    # Ommit columns with single unique value
    numeric_cols = [col for col in numeric_cols if df_threatment[col].nunique() > 1]

    if method == 'iqr':
        for col in numeric_cols:
            Q1 = df_threatment[col].quantile(0.25)
            Q3 = df_threatment[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            df_threatment = df_threatment[(df_threatment[col] >= lower_bound) & (df_threatment[col] <= upper_bound)]
            
    elif method == 'zscore':
        for col in numeric_cols:
            z_scores = stats.zscore(df_threatment[col])

            mask_remove_outliers = np.abs(z_scores) < z_threshold
            df_threatment = df_threatment[mask_remove_outliers]

    rows_removed = initial_rows - df_threatment.shape[0]
    print(f'Rows deleted: {rows_removed} ({(rows_removed / initial_rows) * 100:.2f}%)')
    
    return df_threatment
