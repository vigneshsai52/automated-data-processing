def clean_data(df):
    # Remove duplicate rows
    df = df.drop_duplicates().copy()

    # Fill missing values safely using .loc
    df.loc[:, "age"] = df["age"].fillna(df["age"].mean())
    df.loc[:, "salary"] = df["salary"].fillna(df["salary"].mean())

    return df
