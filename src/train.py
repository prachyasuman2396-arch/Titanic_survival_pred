import joblib
import json

from sklearn.model_selection import GridSearchCV
# from sklearn.metrics import roc_auc_score,accuracy_score

from src.pipeline import get_pipeline

# from src.split import split_data

# from src.data_loader import load_data

def train_model(X_train, y_train):

    pipeline = get_pipeline()

    param_grid = {
        'model__n_estimators': [100, 200, 300],
        'model__max_depth': [5, 10, None],
        'model__min_samples_split': [2, 5, 10]
    }

    grid = GridSearchCV(
        pipeline,
        param_grid=param_grid,
        cv=5,
        scoring='roc_auc',   
        n_jobs=-1,
        verbose=2
    )

    grid.fit(X_train, y_train)

    return grid



