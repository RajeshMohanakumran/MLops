from django.db import models
#Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area,
# Create your models here.
class LoanPrediction(models.Model):
    
    Gender = models.IntegerField(max_length=200)
    Married = models.IntegerField(max_length=200)
    Dependents = models.IntegerField(max_length=200)
    Education = models.IntegerField(max_length=200)
    Self_Employed = models.IntegerField()
    ApplicantIncome = models.IntegerField()
    CoapplicantIncome = models.IntegerField()
    LoanAmount = models.IntegerField()
    Loan_Amount_Term = models.IntegerField()
    Credit_History = models.IntegerField()
    Property_Area = models.IntegerField(max_length=7)