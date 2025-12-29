import json
import pandas as pd 
data =  [ 
    {"Empno": 9001 , "Salary":3000},
    {"Empno": 9002 , "Salary":2800},
    {"Empno": 9003 , "Salary":2500}
]
json_data = json.dumps(data)
salary = pd.read_json(json_data)
salary = salary.set_index('Empno')
print(salary)