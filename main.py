import sqlite3

conn = sqlite3.connect('autoparts.db')
cursor = conn.cursor()

sql =('''
    CREATE TABLE IF NOT EXISTS interior_parts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL
    )
''')
cursor.execute(sql)

sql =('''
    CREATE TABLE IF NOT EXISTS exterior_parts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL
    )
''')
cursor.execute(sql)

# interior vehicle parts
cursor.execute('''INSERT INTO interior_parts  (name, price) VALUES ('Front seat', 26300.00)''' )
cursor.execute('''INSERT INTO interior_parts  (name, price) VALUES ('Back seats', 45100.00)''' )
cursor.execute('''INSERT INTO interior_parts  (name, price) VALUES ('Engine', 35000.00)''' )
cursor.execute('''INSERT INTO interior_parts  (name, price) VALUES ('Exhaust pipe', 25800.00)''' )
cursor.execute('''INSERT INTO interior_parts  (name, price) VALUES ('Front doors', 67500.00)''' )
cursor.execute('''INSERT INTO interior_parts (name, price) VALUES ('Back doors', 5300.00)''' )


# exterior vehicle parts

cursor.execute('''INSERT INTO exterior_parts (name, price) VALUES ('Front Bumper', 11100.00)''' )
cursor.execute('''INSERT INTO exterior_parts (name, price) VALUES ('Back bumper', 21100.00)''' )
cursor.execute('''INSERT INTO exterior_parts (name, price) VALUES ('Tail light', 36100.00)''' )
cursor.execute('''INSERT INTO exterior_parts (name, price) VALUES ('Headlight', 25100.00)''' )
cursor.execute('''INSERT INTO exterior_parts (name, price) VALUES ('Roof racks', 55500.00)''' )
cursor.execute('''INSERT INTO exterior_parts (name, price) VALUES ('Side mirrors', 6100.00)''' )

conn.commit()
conn.close()

