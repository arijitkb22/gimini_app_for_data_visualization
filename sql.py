import sqlite3
connection = sqlite3.connect("employee.db")

# Create Cursor -> Temp work station for database
cursor = connection.cursor()

# Create table
table_info = """ 
Create table EMP(NAME VARCHAR(25), DESIGNATION VARCHAR(25), EXPERIANCE INT,
PROFILE VARCHAR(25));

"""
cursor.execute(table_info)

# Insert records
cursor.execute(""" insert into EMP values('Arijit', 'SE1', 2, 'UI')""")
cursor.execute(""" insert into EMP values('Jit', 'SE2', 5, 'QE')""")
cursor.execute(""" insert into EMP values('Bimal', 'SSE', 5, 'BE')""")
cursor.execute(""" insert into EMP values('Sneha', 'SSE', 3, 'BE')""")
cursor.execute(""" insert into EMP values('Sumit', 'SSE', 3, 'QE')""")
cursor.execute(""" insert into EMP values('Minhaz', 'SSE', 5, 'UI')""")

#Display Data

print('Data are: ')
data = cursor.execute(""" Select * From EMP""")
for row in data:
    print(row)

# Closeing connection
connection.commit()
connection.close()
