from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier

from src.build_feature import build_feature


def get_pipeline():

    feature_pipeline = FunctionTransformer(build_feature,validate=False)

    
    num_cols = [
        'Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'missing_age', 'is_child',
        'has_cabin', 'cabin_female','FamilySize', 'is_high_status', 'IsAlone'
    ]

    cat_cols = [
        'Sex', 'Embarked',
        'Age_group', 'Title'
    ]

    
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median'))
    ])

    cat_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='constant',fill_value='Unknown')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer([
        ('num', num_pipeline, num_cols),
        ('cat', cat_pipeline, cat_cols)
    ])

   
    model = RandomForestClassifier(
        random_state=42,
        class_weight='balanced'
    )

    
    pipeline = Pipeline([
        ('feature_engineering', feature_pipeline),
        ('preprocessing', preprocessor),
        ('model', model)
    ])

    return pipeline