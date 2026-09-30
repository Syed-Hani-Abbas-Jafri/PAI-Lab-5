import requests
import json
import csv

url = "https://api.agify.io"
params = {"name[]": ["michael", "sara", "ahmed", "ali", "john"]}

data = None

try:
    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.Timeout:
    print("Request timed out.")
except requests.exceptions.ConnectionError:
    print("Connection error.")
except requests.exceptions.HTTPError:
    print("HTTP error occurred.")
except requests.exceptions.RequestException as error:
    print("Request failed:", error)
except json.JSONDecodeError:
    print("Invalid JSON data received.")
else:
    ages = [item["age"] for item in data if item.get("age") is not None]
    average_age = sum(ages) / len(ages) if ages else 0
    highest = max(data, key=lambda item: item["age"] or 0)

    print("Retrieved Data:", data)
    print("Average Age:", average_age)
    print("Highest Age Prediction:", highest)
    print("Count:", len(data))

    try:
        with open("age_predictions.json", "w") as file:
            json.dump(data, file, indent=4)

        with open("age_predictions.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "age", "count"])
            writer.writeheader()
            writer.writerows(data)
    except (OSError, IOError) as error:
        print("File error:", error)
finally:
    print("API request attempt finished.")

try:
    with open("age_predictions.json", "r") as file:
        saved_json = json.load(file)
    print("\nVerified JSON Data:", saved_json)

    with open("age_predictions.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        print("\nVerified CSV Data:")
        for row in reader:
            print(row)
except FileNotFoundError:
    print("Saved file not found.")
except json.JSONDecodeError:
    print("Invalid JSON data in saved file.")
