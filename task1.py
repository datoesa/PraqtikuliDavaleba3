import sqlite3

connection = sqlite3.connect('person.db')
cursor = connection.cursor()


cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees(
            name TEXT NOT NULL,
            LastName TEXT,
            age INTEGER,
            city TEXT NOT NULL,
            salary INTEGER)""")

cursor.execute("INSERT INTO employees VALUES('gio', 'gulordava', 22, 'Tbilisi', 900)")
cursor.execute("INSERT INTO employees VALUES('lika', 'kutaladze', 25, 'Tbilisi', 1500)")
cursor.execute("INSERT INTO employees VALUES('nika', 'bezhuashvili', 21, 'Tbilisi', 1200)")
cursor.execute("INSERT INTO employees VALUES('hanns', 'müller', 22, 'Berlin', 2200)")
cursor.execute("INSERT INTO employees VALUES('ilse', 'schmidt', 25, 'Berlin', 3000)")
cursor.execute("INSERT INTO employees VALUES('mark', 'fischer', 21, 'Berlin', 2500)")

connection.commit()

cursor.execute('SELECT "საშუალო ხელფასი "|| city || "-ში არის: "|| AVG(salary) FROM employees GROUP BY city')

print(cursor.fetchall())
