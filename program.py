import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load loan payment data
train_data = pd.read_csv('loan_data.csv')

# Load validation data
validation_data = pd.read_csv('validation_data.csv')

# Add the Net Take Home (NTH) amount as a feature in the dataframe
train_data['nth_amount'] = train_data['income'] * 0.4
validation_data['nth_amount'] = validation_data['income'] * 0.4

# Convert categorical variables into dummy variables
train_data = pd.get_dummies(train_data, columns=['employmentstatus'])
validation_data = pd.get_dummies(validation_data, columns=['employmentstatus'])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(train_data[['income', 'credit_score', 'loan_amount', 'nth_amount', 'employmentstatus_Employed', 'employmentstatus_Unemployed']],
                                                    train_data['default'],
                                                    test_size=0.2,
                                                    random_state=42)

# Create logistic regression model
log_reg = LogisticRegression()

# Train the model on the training set
log_reg.fit(X_train, y_train)

# Use the model to predict loan payment default on the test set
y_pred = log_reg.predict(X_test)
default_percent = (y_pred.sum() / len(y_pred)) * 100
print('Chance of default:', default_percent, '%')

# Evaluate the model's accuracy on the test set
accuracy = accuracy_score(y_test, y_pred)
print('Model accuracy:', accuracy)
