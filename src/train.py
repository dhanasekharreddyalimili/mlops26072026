import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

print("Loading dataset...")

# Read dataset
df = pd.read_csv("data/student_marks.csv")

print(df.head())

# Features
X = df[['StudyHours']]

# Label
y = df['ExamScore']

print("\nSplitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training model...")

model = LinearRegression()

model.fit(X_train, y_train)

print("Training completed.")

print("\nTesting model...")

predictions = model.predict(X_test)

mse = mean_squared_error(y_test, predictions)

print("Mean Squared Error:", mse)

print("\nModel Equation")

print("Slope:", model.coef_[0])

print("Intercept:", model.intercept_)

print("\nSaving model...")

# Create models folder if it doesn't exist
models_folder = Path("models")
models_folder.mkdir(exist_ok=True)

# Save model inside models folder
model_path = models_folder / "student_model.pkl"
joblib.dump(model, model_path)

print(f"Model saved successfully at: {model_path}")
print("GitHub Actions Pipeline Test..")