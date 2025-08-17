"""
build_features.py

This module creates features from raw data for model training and inference.
"""

import pandas as pd


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add custom features to the dataset.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe with raw/cleaned data.

    Returns
    -------
    pd.DataFrame
        Dataframe with new feature columns.
    """
    # TODO: implement feature engineering steps.
    # Example:
    # df["feature_sum"] = df["col1"] + df["col2"]
    return df


def main():
    """Main method for feature engineering."""
    # Example usage: load processed data, add features, save features.
    input_path = "data/processed/data.csv"
    output_path = "data/processed/features.csv"

    df = pd.read_csv(input_path)
    df_features = add_features(df)
    df_features.to_csv(output_path, index=False)


if __name__ == "__main__":
    main()
