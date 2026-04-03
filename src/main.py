
from src.data_loader import load_data
from src.evaluate_model import evaluate_model
from src.train import train_model
from src.split import split_data
from src.save_artifects import save_artifacts

def main():

    # Load
    df = load_data("/Users/prachyasumandas/Documents/titanic/data/Titanic-Dataset.csv.xls")

    # Split
    X_train, X_test, y_train, y_test = split_data(df)

    # Train
    grid = train_model(X_train, y_train)

    best_pipeline = grid.best_estimator_

    print("\nBest Parameters:")
    print(grid.best_params_)

    # Evaluate
    evaluate_model(best_pipeline, X_test, y_test)

    save_artifacts(best_pipeline, grid.best_params_)

    

if __name__ == "__main__":
    main()
