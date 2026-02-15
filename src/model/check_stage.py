from mlflow import MlflowClient

client = MlflowClient()
for mv in client.search_model_versions("name='MyModelName'"):
    print(f"Version: {mv.version}, Stage: {mv.current_stage}")

