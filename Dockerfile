# Use the official Python image as base
FROM python:3.12.2
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN python -m venv /venv
RUN pip install djangorestframework
RUN pip install django-cors-headers
RUN pip install django
RUN pip install pandas
RUN pip install numpy
RUN pip install scikit-learn
# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt . 
RUN pip install -r requirements.txt
# Copy the backend source code to the working directory
COPY . .
 # Copy the CSV file into the container
COPY LoanPrediction.csv /app/LoanPrediction.csv
# Expose port 8000 to the outside world
EXPOSE 8000
# Command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]