import pyodbc

conn = pyodbc.connect("DRIVER={SQL Server};"
                      "SERVER=DESKTOP-T9L8GOD\MSSQLSERVER01;"
                      "Database = AdventureWorks2012;"
                      "Trusted_Connection=yes;")

cursor = conn.cursor()

cursor.execute("""SELECT *
  FROM [AdventureWorks2012].[Person].[Person]""")

for row in cursor:
    print(f'row={row}')
