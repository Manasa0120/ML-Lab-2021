!pip install db-sqlite3
import sqlite3
conn = sqlite3.connect ('test.db')
cur = conn.cursor()
print ("DB Created Successfully")

conn.execute('''CREATE TABLE COMPANY1
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print ("Table created successfully");

conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'Texas', 20000.00 )");

conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Perry', 27, 'Houston', 15000.00 )");

conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Berry', 25, 'Hawai', 20000.00 )");

conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Terry', 31, 'Rich-Mond ', 65000.00 )");

conn.commit()
print ("Records created successfully");

for row in conn.execute('select * from COMPANY1'):
        print(row)
