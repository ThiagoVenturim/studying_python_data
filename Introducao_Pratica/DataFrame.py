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
print(emps)