import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, median_absolute_error
import category_encoders as ce


# Read data
data = pd.read_csv('dashboard_car_inventory.csv')

# Designate features and target label
columns = ['color', 'number_of_seats', 'number_of_doors', 'type_of_gas', 'kilometers_per_liter', 'mileage']
features = data[columns].fillna(0)
target = data['rate'].fillna(0)

# Splits
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Category encoding
encoder = ce.OrdinalEncoder(cols=columns)
X_train = encoder.fit_transform(X_train)
X_test = encoder.fit_transform(X_test)

# Model training
model = xgb.XGBRegressor()
model.fit(X_train, y_train)

# Prediction scores
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
medae = median_absolute_error(y_test, predictions)
print(f"Mean Absolute Error: {mae:.2f}")
print(f"Mean Squared Error: {mse:.2f}")
print(f"Median Absolute Error: {medae:.2f}")

# Set test parameters
color = 'Green'
number_of_seats = 7.0
number_of_doors = 4.0
type_of_gas = 'Diesel'
kilometers_per_liter = 16.0
mileage = 1300.05
new_data = encoder.fit_transform(
    pd.DataFrame(
        {
            'color': [color],
            'number_of_seats': [number_of_seats],
            'number_of_doors': [number_of_doors],
            'type_of_gas': [type_of_gas],
            'kilometers_per_liter': [kilometers_per_liter],
            'mileage': [mileage],
        }
    )
)

# Make prediction
recommended_price = model.predict(new_data)
print(f"The recommended rental price is PHP {recommended_price[0]:.2f}")

# Data visualization
import seaborn as sns
import matplotlib.pyplot as plt

# Scatter plot of regression line
sns.scatterplot(x=y_test, y=predictions)
plt.xlabel('Actual values')
plt.ylabel('Predicted values')
plt.title('Regression: Actual vs Predicted')
plt.show()

# Residual plot
residuals = y_test - predictions
sns.scatterplot(x=predictions, y=residuals)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Regression: Residual Plot')
plt.show()

# Distribution of residuals
sns.histplot(residuals, kde=True)
plt.xlabel('Residuals')
plt.ylabel('Density')
plt.title('Distribution of Residuals')
plt.show()

# TODO (jaceroldan)
# Feature importance plot (assuming you have feature names and their coefficients)
# feature_names = ['Feature 1', 'Feature 2', 'Feature 3']
# coefficients = [0.5, 0.3, -0.1]

# sns.barplot(x=coefficients, y=feature_names)
# plt.xlabel('Coefficient')
# plt.ylabel('Feature')
# plt.title('Feature Importance')
# plt.show()
