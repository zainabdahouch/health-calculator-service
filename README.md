# Health Calculator API

This project is a Health Calculator API built using Flask. The application provides two primary functionalities:

**BMI Calculation**: Calculate the Body Mass Index (BMI) given a person's height and weight.

**BMR Calculation**: Calculate the Basal Metabolic Rate (BMR) using the Harris-Benedict equation based on height, weight, age, and gender.


The project is containerized using Docker and includes a CI/CD pipeline with GitHub Actions for automated testing and deployment to Azure Web App.


## Features
**BMI Calculation:**

Input: Height (in meters), Weight (in kg).  
Output: BMI value.

**BMR Calculation:**

Input: Height (in cm), Weight (in kg), Age (in years), Gender (Male/Female).  
Output: BMR value based on the Harris-Benedict formula.  

## API Endpoints
1. **Home Endpoint**


URL: /  
Method: GET  
Response:  
```
{
  "message": "Welcome to the Health Calculator app!"
}
```

2. **BMI Calculation**

URL: /bmi  
Method: POST  
Request Body  
```
{
  "height": 1.75,
  "weight": 70
}
```

Response:  
```
{
  "operation": "BMI",
  "result": 22.86
}
```

3. **BMR Calculation**  


URL: /bmr  
Method: POST  
Request Body:  
```
{
  "height": 175,
  "weight": 70,
  "age": 30,
  "gender": "male"
}
```

Response:  
```
{
  "operation": "BMR",
  "result": 1695.67
}
```
  
# Getting Started
## Prerequisites  
Python 3.9 or higher  
Docker  
Makefile support  
Azure account (for deployment)  
## Installation  


1. **Clone the repository**
```
git clone https://github.com/zainabdahouch/health-calculator-service

cd health-calculator
```

2. **Install dependencies**
```
make init
```

## Run Locally
```
make run
```

Activate the virtual environment and run the Flask app:  

The API will be available at http://localhost:5000

## Run in Docker  

Build and run the container:  
```
make build
make run-container
```

The API will be available at http://localhost:5000

## Testing  

Run the unit tests to ensure the correctness of the calculations:  
```
make test
```
Run the API tests to validate endpoints: 
```
make test-api
``` 

## Deployment  

The application is deployed to Azure Web App using GitHub Actions.  
The CI/CD pipeline automates:  

1. Building and testing the application.  
2. Deploying the Flask app to Azure on every push to the master branch.
