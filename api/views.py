from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from .serializers import LoanPredictionSerializer
from rest_framework import status
from sklearn.preprocessing import LabelEncoder
import os
from django.conf import settings
# Construct the absolute file path within the Docker container
file_path = os.path.join(settings.BASE_DIR, 'LoanPrediction.csv')
# Load the dataset
data = pd.read_csv(file_path)


# Fill missing values with mode for categorical variables and mean for numerical variables
data['Gender'] = data['Gender'].fillna(data['Gender'].mode()[0])
data['Married'] = data['Married'].fillna(data['Married'].mode()[0])
data['Dependents'] = data['Dependents'].fillna(data['Dependents'].mode()[0])
data['Self_Employed'] = data['Self_Employed'].fillna(data['Self_Employed'].mode()[0])
data['LoanAmount'] = data['LoanAmount'].fillna(data['LoanAmount'].mean())
data['Loan_Amount_Term'] = data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mean())
data['Credit_History'] = data['Credit_History'].fillna(data['Credit_History'].mode()[0])

# Check for any remaining missing values
print(data.isnull().sum())



le = LabelEncoder()

# Fit the encoder on the categorical data



# Encoding Education feature


# Dropping Loan_ID and encoding Loan_Status
data = data.drop('Loan_ID', axis=1)


data['Loan_Status'] = le.fit_transform(data['Loan_Status'])
data['Gender'] = le.fit_transform(data['Gender'])
data['Married'] = le.fit_transform(data['Married'])
data['Dependents'] = le.fit_transform(data['Dependents'])
data['Self_Employed'] = le.fit_transform(data['Self_Employed'])
data['Property_Area'] = le.fit_transform(data['Property_Area'])
data['Education'] = le.fit_transform(data['Education'])


x = data.drop('Loan_Status', axis=1)
y = data['Loan_Status']

model = LogisticRegression()
model.fit(x, y)


@api_view(['POST'])
def predict(request):
    if request.method == 'POST':
        serializer = LoanPredictionSerializer(data=request.data)
        if serializer.is_valid():
            input_data = tuple(serializer.validated_data.values())
            input_numpy = np.asarray(input_data).reshape(1, -1)
            out = model.predict(input_numpy)
            # Handle the case where 'out' is not assigned in all execution paths
            prediction = "Eligible for Loan" if out == 1 else "Not eligible for Loan"
            return Response({'prediction': prediction}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)