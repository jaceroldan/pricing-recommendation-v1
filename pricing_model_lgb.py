import lightgbm as lgb
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import category_encoders as ce


# Load the car pricing dataset
data = pd.read_csv('dashboard_car_inventory.csv')

# Prepare the features and target variable
columns = ['color', 'number_of_seats', 'number_of_doors', 'type_of_gas', 'kilometers_per_liter', 'mileage']
X = data[columns].fillna(0)
y = data['rate'].fillna(0)

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Category encoding
encoder = ce.OrdinalEncoder(cols=columns)
X_train = encoder.fit_transform(X_train)
X_test = encoder.fit_transform(X_test)

# Convert the dataset into LightGBM format
lgb_train = lgb.Dataset(X_train, y_train)

# Set the parameters for LightGBM
params = {
    'objective': 'regression',
    'metric': 'rmse'
}

# Train the LightGBM model
model = lgb.train(params, lgb_train, num_boost_round=100)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: {rmse}")

# Example usage to predict car prices for new data
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
prediction = model.predict(new_data)
print(f"Predicted price: {prediction[0]}")
