from sklearn.model_selection import train_test_split
import pandas as pd
def split_data(df: pd.DataFrame):
    X = df.drop('Survived', axis=1)
    y = df['Survived']

    return train_test_split(
        X, y,
        test_size=0.2,
        stratify=y,  
        random_state=42
    )
