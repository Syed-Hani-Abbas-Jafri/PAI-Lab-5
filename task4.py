import requests

url = "https://api.agify.io"
params = {"name": "michael"}

try:
    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()
    data = response.json()

    if response.status_code == 200:
        prediction = data.get("age")
        confidence = data.get("count")
        input_name = data.get("name")
        print("Input Name:", input_name)
        print("Predicted Age:", prediction)
        print("Confidence (Count):", confidence)
    else:
        print("API could not provide the requested result.")

except requests.exceptions.Timeout:
    print("Request timed out.")
except requests.exceptions.ConnectionError:
    print("Connection error.")
except requests.exceptions.HTTPError:
    print("HTTP error occurred.")
except requests.exceptions.RequestException as error:
    print("Request failed:", error)
