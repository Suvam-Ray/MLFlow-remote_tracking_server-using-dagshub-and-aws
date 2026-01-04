from mlflow.tracking import MlflowClient

# Initialize the MLflow Client
client = MlflowClient()

# Define the model name and version
model_name = "diabetes-rf" # This should be fetched programatically in live project
model_version = 3  # Replace with the specific version number you want to transition or fetch the latest version dynamically from the MLFlow

# Transition the model version to a new stage
new_stage = "Production"  # Possible values: "None", "Staging", "Production", "Archived"
client.transition_model_version_stage(
    name=model_name,
    version=model_version,
    stage=new_stage,
    archive_existing_versions=True # If set to false then the exsiting version is not archived
)

print(f"Model version {model_version} transitioned to {new_stage}")