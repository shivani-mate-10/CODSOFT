# -*- coding: utf-8 -*-
"""Task1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ArqH00EUtuWT6D2HYWgcn1MfTJQWYPU6

#Importing Libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

"""#Loading Datset"""

Titanic_data=pd.read_csv('Titanic-Dataset.csv')
Titanic_data

"""#Dimension Of Dataset"""

print(Titanic_data.shape)

"""#Checking if there is any null value in Dataset"""

Titanic_data.isna().sum()

# Cabin column contains many missing columns so we'll drop the Cabin column
Data1 = Titanic_data.drop(columns='Cabin')
Data1

# Replace the missing values in Age column with mean value
Data1['Age'].fillna(Data1['Age'].mean(), inplace=True)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np
#Fill missing Embarked values with the most frequent value
imputer = SimpleImputer(strategy='most_frequent')
Data1['Embarked'] = imputer.fit_transform(Data1[['Embarked']]).ravel()

Data1.isna().sum()

# Statistical measures about the data
Data1.describe()

Data1.info()

# Printing the target column
Data1["Survived"]

# Finding the number of people survived and not survived
Data1['Survived'].value_counts()

# Graphical representation of Survived Passenger column
sns.countplot(x='Survived', data=Data1)
plt.title('Count of Survived and Not Survived in Titanic Data')

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np
# Use OneHotEncoder to encode 'Sex' and 'Embarked'
categorical_features = ['Sex', 'Embarked']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Preprocess numeric features
numeric_features = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

# Combine preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])
# Define the preprocessing pipeline
X = Data1.drop(columns=['Survived', 'PassengerId', 'Name', 'Ticket'])
y = Data1['Survived']

"""#Splitting data into train and test"""

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train, X_test, y_train, y_test

#Model evaluation
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# Create the model pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

accuracy, precision, recall, f1, conf_matrix, class_report

#Make prediction
# Example new data (assuming the same structure as the training data)
new_data = pd.DataFrame({
    'Pclass': [3, 1],
    'Sex': ['male', 'female'],
    'Age': [22, 38],
    'SibSp': [1, 1],
    'Parch': [0, 0],
    'Fare': [7.25, 71.2833],
    'Embarked': ['S', 'C']
})
print(new_data)

# Make predictions
new_predictions = model.predict(new_data)
new_predictions