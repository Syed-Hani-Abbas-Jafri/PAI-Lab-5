import csv

file_path = "patients.csv"
fieldnames = ["id", "age", "bmi", "blood_pressure", "glucose", "diabetes"]

rows = [
    {"id": "1", "age": "45", "bmi": "28.5", "blood_pressure": "120", "glucose": "140", "diabetes": "1"},
    {"id": "2", "age": "32", "bmi": "22.1", "blood_pressure": "110", "glucose": "95", "diabetes": "0"},
    {"id": "3", "age": "58", "bmi": "31.4", "blood_pressure": "135", "glucose": "180", "diabetes": "1"},
    {"id": "4", "age": "26", "bmi": "24.0", "blood_pressure": "115", "glucose": "88", "diabetes": "0"},
]

with open(file_path, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)


def display_records():
    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


def count_cases():
    positive = 0
    negative = 0
    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["diabetes"] == "1":
                positive += 1
            else:
                negative += 1
    return positive, negative


def high_glucose_patients(threshold):
    result = []
    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if float(row["glucose"]) > threshold:
                result.append(row)
    return result


def average_bmi_glucose():
    bmi_total = 0
    glucose_total = 0
    count = 0
    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            bmi_total += float(row["bmi"])
            glucose_total += float(row["glucose"])
            count += 1
    return bmi_total / count, glucose_total / count


def add_record(record):
    with open(file_path, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(record)


def update_record(patient_id, updated_fields):
    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    found = False
    for row in rows:
        if row["id"] == patient_id:
            row.update(updated_fields)
            found = True
    if found:
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    return found


print("All Records:")
display_records()

positive, negative = count_cases()
print(f"\nPositive Cases: {positive}")
print(f"Negative Cases: {negative}")

print("\nPatients with glucose above 130:")
for patient in high_glucose_patients(130):
    print(patient)

avg_bmi, avg_glucose = average_bmi_glucose()
print(f"\nAverage BMI: {avg_bmi:.2f}")
print(f"Average Glucose: {avg_glucose:.2f}")

add_record({"id": "5", "age": "40", "bmi": "27.0", "blood_pressure": "125", "glucose": "150", "diabetes": "1"})

update_record("2", {"glucose": "100"})

print("\nFinal Records:")
display_records()
