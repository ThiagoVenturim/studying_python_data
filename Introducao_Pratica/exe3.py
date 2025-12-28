#PANDAS
import pandas as pd 

name = ['Jeff Russel', 'Jane Boorman', 'Tom Heints']
emps_name =pd.Series(name, index= [ 9001, 9002, 9003], name = 'names')

# print(emps_name.iloc[:])
# print(emps_name.loc[:])

email = [ 'jeff.russel@gmail.com', 'jane.boorman@gmail.com', 'tom.heints@gmail.com']
emps_email = pd.Series(email, index= [9001,9002,9003], name  = 'emails')

phone = ['0000-0000','1111-1111','2222-2222']
emps_phone = pd.Series(phone, index = [ 9001,9002,9003], name='phones')
df = pd.concat([emps_name, emps_email, emps_phone], axis=1)
print(df)


