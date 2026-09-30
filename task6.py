import requests

base_url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(f"{base_url}/1", timeout=5)
    response.raise_for_status()
    print("GET Status:", response.status_code)
    print("GET Response:", response.json())

    prediction = {"title": "cat", "body": "confidence: 0.95", "userId": 1}
    response = requests.post(base_url, json=prediction, timeout=5)
    response.raise_for_status()
    print("\nPOST Status:", response.status_code)
    print("POST Response:", response.json())

    updated_prediction = {"title": "dog", "body": "confidence: 0.90", "userId": 1}
    response = requests.put(f"{base_url}/1", json=updated_prediction, timeout=5)
    response.raise_for_status()
    print("\nPUT Status:", response.status_code)
    print("PUT Response:", response.json())

    patch_data = {"body": "confidence: 0.99"}
    response = requests.patch(f"{base_url}/1", json=patch_data, timeout=5)
    response.raise_for_status()
    print("\nPATCH Status:", response.status_code)
    print("PATCH Response:", response.json())

    response = requests.delete(f"{base_url}/1", timeout=5)
    response.raise_for_status()
    print("\nDELETE Status:", response.status_code)

except requests.exceptions.Timeout:
    print("Request timed out.")
except requests.exceptions.ConnectionError:
    print("Connection error.")
except requests.exceptions.HTTPError:
    print("HTTP error occurred.")
except requests.exceptions.RequestException as error:
    print("Request failed:", error)
