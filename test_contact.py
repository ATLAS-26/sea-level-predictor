import requests
import json

# Test the contact endpoint
url = "http://localhost:5000/contact"
data = {
    "firstName": "John",
    "lastName": "Doe",
    "email": "john@example.com",
    "subject": "Test Contact Form",
    "message": "This is a test message from the contact form."
}

try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")