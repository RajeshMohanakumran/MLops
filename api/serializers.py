from rest_framework import serializers
from .models import LoanPrediction

class LoanPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model=LoanPrediction
        fields='__all__'