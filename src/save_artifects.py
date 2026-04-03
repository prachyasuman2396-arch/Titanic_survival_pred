import os
import joblib
import json
def save_artifacts(model, params, output_dir="artifacts"):

    os.makedirs(output_dir, exist_ok=True)

    # Save pipeline
    joblib.dump(model, os.path.join(output_dir, "model.pkl"))

    # Save best parameters
    with open(os.path.join(output_dir, "best_params.json"), "w") as f:
        json.dump(params, f)

    print(" Artifacts saved successfully.")