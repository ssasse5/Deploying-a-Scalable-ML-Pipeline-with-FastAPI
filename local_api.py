import json
import requests

url = "http://127.0.0.1:8000"

# Try sending a GET request
try:
    r = requests.get(url)
    print(f"Status Code: {r.status_code}")
    print(f"Message: {r.json()}")  # Ensures the response is valid JSON
except requests.exceptions.RequestException as e:
    print(f"Error: Could not connect to API - {e}")
    exit(1)

# Sample data for POST request
data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States"
}

# Try sending a POST request
post_url = "http://127.0.0.1:8000/data/"
try:
    r = requests.post(post_url, json=data)
    print(f"Status Code: {r.status_code}")

    # Check if the response is JSON before attempting to parse
    if "application/json" in r.headers.get("Content-Type", ""):
        print(f"Result: {r.json()}")
    else:
        print("Error: Response is not in JSON format.")
        print(f"Response Text: {r.text}")  # Print raw response for debugging

except requests.exceptions.RequestException as e:
    print(f"Error: Could not connect to API - {e}")
