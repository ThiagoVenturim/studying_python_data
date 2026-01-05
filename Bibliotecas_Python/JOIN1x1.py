import json
import pandas as pd 

data = [
        ['9001','Jeff Russell', 'sales'],
        ['9002','Jane Boorman', 'sales'],
        ['9003','Tom Heints', 'sales']
    ]
    
emps = pd.DataFrame(data, columns = ['Empno', 'Name', 'Job'])
column_types = {'Empno': int, 'Name':str, 'Job': str}
emps= emps.astype(column_types)
emps= emps.set_index('Empno')
print(f" DataFrame Emps:\n{emps}\n")

data =  [ 
    {"Empno": 9001 , "Salary":3000},
    {"Empno": 9002 , "Salary":2800},
    {"Empno": 9003 , "Salary":2500}
]
json_data = json.dumps(data)
salary = pd.read_json(json_data)
salary = salary.set_index('Empno')
print(f"Data Frame Salary:\n{salary}\n")

emps_salary = emps.join(salary)
print(f"Data Frame apos Join entre emps e salary:\n{emps_salary}\n")

new_emps = pd.Series(
        {"Name": "Jonh Hardy", "Job": "sales"}, name = 9004
    )
emps = pd.concat([emps, new_emps.to_frame().T])
print(f"Atualizando emps:\n{emps}\n")

new_salary = pd.Series(
    {"Salary":3200}, name= 9005
    )   
salary = pd.concat([salary, new_salary.to_frame().T])
print(f"Atualizando salary:\n{salary}\n")


emps_salary = emps.join(salary);
print(f"Atualizando o Emps Salary JOIN:\n{emps_salary}\n")


emps_salary = emps.join(salary, how =  'inner')
print(f"Atualizando o Emps Salary INNER:\n{emps_salary}\n")

emps_salary = emps.join(salary, how =  'left')
print(f"Atualizando o Emps Salary LEFT:\n{emps_salary}\n")

emps_salary = emps.join(salary, how =  'right')
print(f"Atualizando o Emps Salary RIGHT:\n{emps_salary}\n")

emps_salary = emps.join(salary, how =  'outer')
print(f"Atualizando o Emps Salary OUTER:\n{emps_salary}\n")

