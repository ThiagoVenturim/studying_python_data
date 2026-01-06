import csv
import os

path = r"C:\Users\thiag\OneDrive\Área de Trabalho\Projetos\studying_python_data\Acessar_Dados\cars.csv"

with open(path, "r", newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=',')
    cars = list(reader)

if not cars:
    raise ValueError("CSV vazio, sem cabeçalho ou delimitador incorreto.")

for car in cars:
    if car['Year'] == '1999' and car['Make'] == 'Chevy' and car['Model'] == 'Venture':
        car['Price'] = '4500.00'

with open(path, "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=cars[0].keys())
    writer.writeheader()
    writer.writerows(cars)
