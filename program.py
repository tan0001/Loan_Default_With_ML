import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load loan payment data
loan_data = pd.read_csv('loan_data.csv')

# Add the Net Take Home (NTH) amount as a feature in the dataframe
loan_data['nth_amount'] = loan_data['income'] * 0.4

# Convert categorical variables into dummy variables
dummy_vars = pd.get_dummies(loan_data['employment_status'])
loan_data = pd.concat([loan_data, dummy_vars], axis=1)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    loan_data[['income', 'credit_score', 'loan_amount', 'self-employed', 'employed','nth_amount']],
    loan_data[['approved','default']],
    test_size=0.2,
    random_state=42
)

# Create logistic regression model
log_reg = LogisticRegression()

# Train the model on the training set
log_reg.fit(X_train, y_train)

# Use the model to predict loan payment default on the test set
y_pred = log_reg.predict(X_test)
default_percent = y_pred*100
print('Chance of default:', default_percent, '%')

# Evaluate the model's accuracy on the test set
accuracy = accuracy_score(y_test, y_pred)
print('Model accuracy:', accuracy)
