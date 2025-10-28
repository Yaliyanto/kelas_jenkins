import requests
import json

url = "https://reqres.in/api/users"
headers = {"x-api-key": "reqres-free-v1"}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
print("Response Body:")
print(json.dumps(response.json(), indent=4))  # <-- rapihin JSON

assert response.status_code == 200, f"Expected 200, got {response.status_code}"
print("✅ Test passed! Response status is 200.")
