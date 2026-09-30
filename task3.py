import json

file_path = "model_results.json"

results = [
    {"model": "LogisticRegression", "accuracy": 0.82, "precision": 0.80, "recall": 0.78, "f1_score": 0.79},
    {"model": "RandomForest", "accuracy": 0.88, "precision": 0.86, "recall": 0.85, "f1_score": 0.855},
    {"model": "SVM", "accuracy": 0.85, "precision": 0.83, "recall": 0.84, "f1_score": 0.835},
]

with open(file_path, "w") as file:
    json.dump(results, file, indent=4)


def load_results():
    with open(file_path, "r") as file:
        return json.load(file)


def save_results(results):
    with open(file_path, "w") as file:
        json.dump(results, file, indent=4)


def highest_accuracy_model():
    results = load_results()
    return max(results, key=lambda r: r["accuracy"])


def highest_f1_model():
    results = load_results()
    return max(results, key=lambda r: r["f1_score"])


def add_model(record):
    results = load_results()
    results.append(record)
    save_results(results)


def update_model(model_name, updated_fields):
    results = load_results()
    found = False
    for r in results:
        if r["model"] == model_name:
            r.update(updated_fields)
            found = True
    if found:
        save_results(results)
    return found


def remove_model(model_name):
    results = load_results()
    new_results = [r for r in results if r["model"] != model_name]
    if len(new_results) == len(results):
        return False
    save_results(new_results)
    return True


print("Model with highest accuracy:", highest_accuracy_model())
print("Model with highest F1-score:", highest_f1_model())

add_model({"model": "XGBoost", "accuracy": 0.90, "precision": 0.89, "recall": 0.88, "f1_score": 0.885})

update_model("SVM", {"accuracy": 0.86})

remove_model("LogisticRegression")

print("\nFinal Results:")
for r in load_results():
    print(r)
