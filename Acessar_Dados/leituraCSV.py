import csv
path = "cars.csv"
with open(path, "r") as csv_file:

    #csv_read = csv.DictReader(csv_file)
    #cars = []
    #for row in csv_read:
    #    cars.append(dict(row))
    #print(cars)
    
    csv_read = csv.reader(csv_file)
    cars = [ ]
    for row in csv_read:
        cars.append(row)
    print(cars)