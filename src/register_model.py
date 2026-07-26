import os
from azure.identity import DefaultAzureCredential
from azure.ai.ml import MLClient
from azure.ai.ml.entities import Model

subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
resource_group = os.environ["AZURE_RESOURCE_GROUP"]
workspace_name = os.environ["AZURE_ML_WORKSPACE"]

credential = DefaultAzureCredential()

ml_client = MLClient(
    credential=credential,
    subscription_id=subscription_id,
    resource_group_name=resource_group,
    workspace_name=workspace_name,
)

model = Model(
    path="models/student_model.pkl",
    name="student-score-model",
    description="Student Score Prediction Model",
    type="custom_model",
)

registered_model = ml_client.models.create_or_update(model)

print("------------------------------------------")
print("Model Registered Successfully")
print("------------------------------------------")
print(f"Model Name    : {registered_model.name}")
print(f"Model Version : {registered_model.version}")