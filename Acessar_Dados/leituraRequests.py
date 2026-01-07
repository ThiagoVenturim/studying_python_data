import requests
r = requests.get('https://localhost/execerpt.txt')
for i, line in enumerate(r.text.split('\n')):
    if line.strip():
        print("Line %i": %(i), line.strip())