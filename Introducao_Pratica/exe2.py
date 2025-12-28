#NUMPY
import numpy as np

jeffy_salary = [2700,3000,3000]
nick_salary = [2600,2800,2800]
tom_salary = [2300,2500,2500]
base_salario = np.array([jeffy_salary, nick_salary, tom_salary]) #combinando arrays 

jeffy_bonus = [500,400,400]
nick_bonus = [600,300,400]
tom_bonus = [200,500,400]
bonus = np.array([jeffy_bonus, nick_bonus, tom_bonus])

salario_bonus = base_salario + bonus # somando duas matrizes 

salario_max = np.amax(salario_bonus, axis=0)
salario_medio = np.median(salario_bonus, axis= 0)
#salario_medio = np.average(salario_bonus, axis= 1)
print(salario_bonus)
print(f"Salario Maximo:{salario_max}\nSalario Medio{salario_medio}")
