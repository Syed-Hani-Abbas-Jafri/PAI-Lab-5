import os

file_path = "experiments.txt"


def create_file():
    if not os.path.exists(file_path):
        open(file_path, "w").close()


def add_experiment(exp_id, model, dataset, lr, epochs):
    with open(file_path, "a") as file:
        file.write(f"{exp_id},{model},{dataset},{lr},{epochs}\n")


def display_experiments():
    with open(file_path, "r") as file:
        lines = file.readlines()
    if not lines:
        print("No experiments found.")
        return
    for line in lines:
        exp_id, model, dataset, lr, epochs = line.strip().split(",")
        print(f"ID: {exp_id}, Model: {model}, Dataset: {dataset}, Learning Rate: {lr}, Epochs: {epochs}")


def search_experiment(exp_id):
    with open(file_path, "r") as file:
        lines = file.readlines()
    for line in lines:
        fields = line.strip().split(",")
        if fields[0] == exp_id:
            return fields
    return None


def update_experiment(exp_id, model, dataset, lr, epochs):
    with open(file_path, "r") as file:
        lines = file.readlines()
    found = False
    new_lines = []
    for line in lines:
        fields = line.strip().split(",")
        if fields[0] == exp_id:
            new_lines.append(f"{exp_id},{model},{dataset},{lr},{epochs}\n")
            found = True
        else:
            new_lines.append(line)
    if found:
        with open(file_path, "w") as file:
            file.writelines(new_lines)
    return found


def delete_experiment(exp_id):
    with open(file_path, "r") as file:
        lines = file.readlines()
    new_lines = [line for line in lines if line.strip().split(",")[0] != exp_id]
    if len(new_lines) == len(lines):
        return False
    with open(file_path, "w") as file:
        file.writelines(new_lines)
    return True


create_file()
add_experiment("E1", "ResNet50", "CIFAR10", "0.001", "50")
add_experiment("E2", "VGG16", "MNIST", "0.01", "30")
add_experiment("E3", "BERT", "IMDB", "0.0005", "10")

print("All Experiments:")
display_experiments()

print("\nSearch Experiment E2:")
result = search_experiment("E2")
if result:
    print(result)
else:
    print("Experiment not found.")

print("\nUpdate Experiment E2:")
if update_experiment("E2", "VGG16", "MNIST", "0.005", "40"):
    print("Experiment updated successfully.")
else:
    print("Experiment not found.")

print("\nDelete Experiment E4:")
if delete_experiment("E4"):
    print("Experiment deleted successfully.")
else:
    print("Experiment not found.")

print("\nFinal Experiments:")
display_experiments()
