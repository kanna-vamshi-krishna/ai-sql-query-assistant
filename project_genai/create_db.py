import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE STUDENT(
NAME VARCHAR(25),
CLASS VARCHAR(25),
SECTION VARCHAR(25),
MARKS INT
)
""")

cursor.execute("INSERT INTO STUDENT VALUES('Krish','Data Science','A',90)")
cursor.execute("INSERT INTO STUDENT VALUES('John','Data Science','B',100)")
cursor.execute("INSERT INTO STUDENT VALUES('Mukesh','Data Science','A',86)")
cursor.execute("INSERT INTO STUDENT VALUES('Jacob','DEVOPS','A',50)")
cursor.execute("INSERT INTO STUDENT VALUES('Dipesh','DEVOPS','A',35)")

conn.commit()
conn.close()

print("Database created successfully")