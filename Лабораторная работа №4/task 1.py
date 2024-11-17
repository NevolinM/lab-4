import json

# TODO решите задачу
def task() -> float:
    filename = "input.json"
    with open(filename) as file:
        data = json.load(file)
    total = sum(item["score"] * item["weight"] for item in data)
    return round(total, 3)

print(task())
