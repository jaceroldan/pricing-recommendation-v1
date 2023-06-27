from util.util import query
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, median_absolute_error
import category_encoders as ce


def xgb_predict(sample):
    """
    Sample - a dictionary containing keys corresponding to the columns
    variable below and field values of a real-world example.
    """

    # Read data
    data = pd.read_csv('pricing_model_utils/dashboard_car_inventory.csv')

    # TODO (jace) for later to get fresh data every time.
    # make this a pipeline
    # result = query(
    #     'SELECT * FROM dashboard.car_inventory ORDER BY id ASC'
    # )

    # Designate features and target label
    columns = ['color', 'number_of_seats', 'number_of_doors', 'type_of_gas', 'kilometers_per_liter', 'mileage']
    # 3, 13, 14, 15, 16, 26
    # 12
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
    color = sample['color']
    number_of_seats = sample['number_of_seats']
    number_of_doors = sample['number_of_doors']
    type_of_gas = sample['type_of_gas']
    kilometers_per_liter = sample['kilometers_per_liter']
    mileage = sample['mileage']
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
    return recommended_price[0]

    # Data visualization
    # import seaborn as sns
    # import matplotlib.pyplot as plt

    # Scatter plot of regression line
    # sns.scatterplot(x=y_test, y=predictions)
    # plt.xlabel('Actual values')
    # plt.ylabel('Predicted values')
    # plt.title('Regression: Actual vs Predicted')
    # plt.show()

    # Residual plot
    # residuals = y_test - predictions
    # sns.scatterplot(x=predictions, y=residuals)
    # plt.axhline(y=0, color='red', linestyle='--')
    # plt.xlabel('Predicted Values')
    # plt.ylabel('Residuals')
    # plt.title('Regression: Residual Plot')
    # plt.show()

    # Distribution of residuals
    # sns.histplot(residuals, kde=True)
    # plt.xlabel('Residuals')
    # plt.ylabel('Density')
    # plt.title('Distribution of Residuals')
    # plt.show()

    # TODO (jaceroldan)
    # Feature importance plot (assuming you have feature names and their coefficients)
    # feature_names = ['Feature 1', 'Feature 2', 'Feature 3']
    # coefficients = [0.5, 0.3, -0.1]

    # sns.barplot(x=coefficients, y=feature_names)
    # plt.xlabel('Coefficient')
    # plt.ylabel('Feature')
    # plt.title('Feature Importance')
    # plt.show()
