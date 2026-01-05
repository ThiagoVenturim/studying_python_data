import pandas as pd 
data = [
        [2608, '9001', 35],
        [2617, '9001', 35],
        [2620, '9001', 139],
        [2621, '9002', 95],
        [2626, '9002', 218]
    ]
orders = pd.DataFrame(data, columns= ['Pono', 'Empno', 'Total'])

data = [
        ['9001','Jeff Russell', 'sales'],
        ['9002','Jane Boorman', 'sales'],
        ['9003','Tom Heints', 'sales']
    ]
    
emps = pd.DataFrame(data, columns = ['Empno', 'Name', 'Job'])

emps_order = emps.merge(orders, how= 'inner', left_on='Empno', right_on='Empno').set_index('Pono')
print(emps_order)

print(orders.groupby(['Empno'])['Total'].mean())
print(orders.groupby(['Empno'])['Total'].sum())