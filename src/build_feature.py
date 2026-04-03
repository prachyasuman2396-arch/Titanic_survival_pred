import pandas as pd

def build_feature(df:pd.DataFrame)->pd.DataFrame:
    df = df.copy()

    df['missing_age'] = df['Age'].isna().astype(int)
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Age_group'] = pd.cut(
    df['Age'],
    bins=[0, 17, 60, 120],
    labels=['minor', 'adult', 'senior']
    )
    df['is_child'] = (df['Age'] < 12).astype(int)
    
    df['has_cabin'] = df['Cabin'].notnull().astype(int)
    df['cabin_female'] = ((df['Sex']=='female')&(df['has_cabin']==1)).astype(int)
    
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['Title'] = df['Name'].str.extract('([A-Za-z]+)\.')
    df['is_high_status'] = df['Title'].isin(['Sir','Lady','Countess']).astype(int)
    df['Title'] = df['Title'].replace([
    'Lady','Countess','Capt','Col','Don','Dr','Major','Rev','Sir','Jonkheer','Dona'
    ], 'Rare')
    
    
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    df = df.drop(['PassengerId','Name','Cabin','Ticket'],axis = 1,errors = 'ignore')

    return df