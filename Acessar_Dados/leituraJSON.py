import json, csv

path = "cars.csv"
with open(path, "r") as csv_file:
    csv_read = csv.DictReader(csv_file)
    cars = []
    for row in csv_read:
        cars.append(dict(row))
with open("cars.json", "w") as json_write:
    json.dump(cars, json_write)
with open("cars.json", "r") as json_file:
    records = json.load(json_file)
    for record in records:
        print(f"years: {record["Year"]}/nmake {record[" Make"].strip()}\nmodel: {record[" Model"]}\nprice: {record[" Price"].strip()}\n"
        )