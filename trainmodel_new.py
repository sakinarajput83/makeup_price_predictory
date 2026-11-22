import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import pickle

# Load data
data = pd.read_excel("makeup_data.xlsx")

# Features and target
X = data[["Brand_Rating", "Weight", "SPF", "Customer_Rating"]]
y = data["Price"]

# Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Check accuracy
pred = model.predict(X_test)
print("Model Error (MAE):", mean_absolute_error(y_test, pred))
print("Model training done!")

# Save model
with open("makeup_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved: makeup_model.pkl")