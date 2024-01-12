import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
# suppress display of warnings
import warnings
warnings.filterwarnings("ignore")

# impor
# classification models
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn import metrics
df=pd.read_csv('train (1)')
df.head()
# # Check for missing values in each column
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])
print(df.describe())
# df.describe()
# Visualize the distribution of the target variable 'SalePrice'
sns.histplot(df['SalePrice'])
plt.show()
# Drop columns with a high percentage of missing values
# For example, you can set a threshold (e.g., 30%) and drop columns with more than 30% missing values
threshold = 0.3
cols_to_drop = missing_values[missing_values / len(df) > threshold].index
df = df.drop(columns=cols_to_drop)

# Impute missing values for numerical columns (e.g., with mean)
df.fillna(df.mean(), inplace=True)

# Impute missing values for categorical columns (e.g., with mode)
df.fillna(df.mode().iloc[0], inplace=True)
# Explore correlation between numerical variables
correlation_matrix = df.corr()
plt.figure(figsize=(24, 20))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.show()
# One-hot encode categorical variables
df_encoded = pd.get_dummies(df, drop_first=True)
from sklearn.preprocessing import StandardScaler

# Separate features and target variable
X = df_encoded.drop('SalePrice', axis=1)
y = df_encoded['SalePrice']

# Standardize numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')
# Import additional models
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

# Initialize and train additional models
rf_model = RandomForestRegressor(random_state=42)
svm_model = SVR()

# Train models
rf_model.fit(X_train, y_train)
svm_model.fit(X_train, y_train)

# Make predictions
y_pred_rf = rf_model.predict(X_test)
y_pred_svm = svm_model.predict(X_test)

# Evaluate additional models
mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

mse_svm = mean_squared_error(y_test, y_pred_svm)
r2_svm = r2_score(y_test, y_pred_svm)

print('Random Forest Model:')
print(f'Mean Squared Error: {mse_rf}')
print(f'R-squared: {r2_rf}')
print('\nSupport Vector Machine (SVM) Model:')
print(f'Mean Squared Error: {mse_svm}')
print(f'R-squared: {r2_svm}')
# Visualize actual vs. predicted values
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred, alpha=0.5)
plt.title('Linear Regression: Actual vs. Predicted')
plt.xlabel('Actual SalePrice')
plt.ylabel('Predicted SalePrice')

plt.subplot(1, 2, 2)
plt.scatter(y_test, y_pred_rf, alpha=0.5)
plt.title('Random Forest: Actual vs. Predicted')
plt.xlabel('Actual SalePrice')
plt.ylabel('Predicted SalePrice')

plt.tight_layout()
plt.show()
# Import GridSearchCV for hyperparameter tuning
from sklearn.model_selection import GridSearchCV

# Define the parameter grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Initialize the Random Forest model
rf_model_tuned = RandomForestRegressor(random_state=42)

# Initialize GridSearchCV
grid_search = GridSearchCV(estimator=rf_model_tuned, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)

# Fit the grid search to the data
grid_search.fit(X_train, y_train)

# Get the best parameters
best_params = grid_search.best_params_
print(f'Best Hyperparameters: {best_params}')

# Use the best model for prediction
best_rf_model = grid_search.best_estimator_
y_pred_best_rf = best_rf_model.predict(X_test)

# Evaluate the best model
mse_best_rf = mean_squared_error(y_test, y_pred_best_rf)
r2_best_rf = r2_score(y_test, y_pred_best_rf)

print('Best Random Forest Model:')
print(f'Mean Squared Error: {mse_best_rf}')
print(f'R-squared: {r2_best_rf}')
# Visualize actual vs. predicted values for the best Random Forest model
plt.scatter(y_test, y_pred_best_rf, alpha=0.5)
plt.title('Best Random Forest Model: Actual vs. Predicted')
plt.xlabel('Actual SalePrice')
plt.ylabel('Predicted SalePrice')
plt.show()
# Extract feature importances from the best Random Forest model
feature_importances = best_rf_model.feature_importances_

# Create a DataFrame to display feature importances
feature_importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': feature_importances})

# Sort features by importance in descending order
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

# Visualize feature importances
plt.figure(figsize=(24, 12))
sns.barplot(x='Importance', y='Feature', data=feature_importance_df)
plt.title('Feature Importances - Best Random Forest Model')
plt.show()
# Import necessary library
from pdpbox import pdp, get_dataset, info_plots

# Select a feature for which you want to create a partial dependence plot
selected_feature = 'OverallQual'

# Create the partial dependence plot
pdp_feature = pdp.pdp_isolate(model=best_rf_model, dataset=X_test, model_features=X.columns, feature=selected_feature)

# Visualize the PDP
pdp.pdp_plot(pdp_feature, selected_feature)
plt.title(f'Partial Dependence Plot for {selected_feature}')
plt.show()
