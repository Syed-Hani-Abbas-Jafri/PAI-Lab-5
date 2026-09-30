import requests
import json
import csv

url = "https://api.quotable.io/quotes/random"
params = {"tags": "life"}

try:
    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()
    data = response.json()

    results = []
    for item in data:
        results.append({
            "text": item.get("content"),
            "author": item.get("author"),
            "tags": ", ".join(item.get("tags", [])),
            "length": item.get("length")
        })

    for r in results:
        print(r)

    with open("quotes.json", "w") as file:
        json.dump(results, file, indent=4)

    with open("quotes.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["text", "author", "tags", "length"])
        writer.writeheader()
        writer.writerows(results)

    print("Data saved successfully.")

except requests.exceptions.Timeout:
    print("Request timed out.")
except requests.exceptions.ConnectionError:
    print("Connection error.")
except requests.exceptions.HTTPError:
    print("HTTP error occurred.")
except requests.exceptions.RequestException as error:
    print("Request failed:", error)
except (OSError, IOError) as error:
    print("File error:", error)
