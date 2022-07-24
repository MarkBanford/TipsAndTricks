import pyodbc

conn = pyodbc.connect("DRIVER={SQL Server};"
                      "SERVER=DESKTOP-T9L8GOD\MSSQLSERVER01;"
                      "Database = AdventureWorks2012;"
                      "Trusted_Connection=yes;")

cursor = conn.cursor()

TABLE_NAME = 'TableTester'


def create(conn):
    print("Creating Table")
    cursor = conn.cursor()
    cursor.execute(""" USE AdventureWorks2012 CREATE TABLE Tester2
    (PersonID int,
    LastName varchar(50),
    FirstName varchar(25),
    Age tinyint);""")
    conn.commit()


def read(conn):
    print("Reading Table")
    cursor = conn.cursor()
    cursor.execute("""SELECT *
  FROM [AdventureWorks2012].[dbo].[Tester2]""")
    for row in cursor:
        print(f'row={row}')
    print()


def update(conn):
    print("Updating Table")
    cursor = conn.cursor()
    cursor.execute(""" UPDATE[AdventureWorks2012].[dbo].[Tester2]
    SET LastName='Thomas'
    WHERE LastName='Smith'""")
    conn.commit()


def delete(conn):
    print('Delete')
    cursor = conn.cursor()
    cursor.execute(""" DELETE FROM [AdventureWorks2012].[dbo].[Tester2]
    WHERE LastName='LN2'
    """)
    conn.commit()


