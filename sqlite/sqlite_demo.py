import sqlite3
from sample_class import Employee

#create an app -> where we can add update and delete employees from our database

#create a new file to store our database
#or
#create an inmemory database
# conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('employee.db')

#create a cursor which allows us to execute sql commands
c = conn.cursor()

# c.execute("""CREATE TABLE employees (
#     first text,
#     last text,
#     pay integer
#         )""")


emp_1 = Employee('Meredith', 'Grey', 80000)
emp_2 = Employee('Derek', 'Sheppard', 80000)


c.execute("INSERT INTO employees VALUES('Viktor','Axelsen',56000)") 


# c.execute("INSERT INTO employees VALUES('Jon','Jones',75000)")
# c.execute("INSERT INTO employees VALUES('Jon','Axelsen',75000)")



c.execute("SELECT * FROM employees WHERE last = 'Axelsen'")


# print(c.fetchone())

print(c.fetchall())


# c.fetchone() -> fetches only one row in our result
# c.fetchmany('<no of rows we want to see after the result>')
# c.fetchall() -> fetches all of the rows after our result
#it means fetch all of the result, or a single result or a number of results




# -> commits our changes to the database
conn.commit()


conn.close()






















