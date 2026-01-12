import mysql.connector

try:
    cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1', database='sampledb')
    cursos = cnx.cursor()

    emps = [
       (9001, "Jeff Russel", "sales"),
       (9002, "Jane Boorman", "sales"),
       (9003, "Tom Heints", "sales")
    ]

    query_add_emp = ("""
        INSERT INTO emps(empno, empname, job)
        VALUES("%s, %s, %s");
    """)

    for emp in emps:
        cursos.execute(query_add_emp, emp)
    
    salary= [
        (9001, 3000),
        (9002, 2800),
        (9003, 2500)
    ]
    query_add_salary= ("""
        INSERT INTO salary (empno, salary)
        VALUES ("%s, %s")
    """)

    for sal in salary:
        cursos.execute(query_add_salary, sal)

    orders = [ 
        (2603, 9001, 35),
        (2617, 9001, 35),
        (2620, 9001, 139),
        (2621, 9002, 95),
        (2626, 9002, 218)
    ]
    query_add_order = ("""
        INSERT INTO orders(pono, empno, total)
        VALUES("%s, %s, %s");
    """)

    for order in orders:
        cursos.execute(query_add_order, order)
    
    cnx.commit()

except mysql.connector.Error as err:
    print("Erro Code: ", err.msg) 
    print("Erro-Message: {}".format(err.msg))
finally:
    cursos.close()
    cnx.close()