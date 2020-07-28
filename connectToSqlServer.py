import pyodbc

conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};SERVER=NICOLAS\\SQLEXPRESS;Database=pythondb;UID=sa;PWD=pass')

cursor = conn.cursor()
cursor.execute('select * from pythondb.dbo.student')

for row in cursor:
    print(row)
 