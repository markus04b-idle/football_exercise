import sqlite3

conn = sqlite3.connect('football.db')

cursor = conn.cursor()

query = """

CREATE TABLE IF NOT EXISTS teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    x TEXT,
    y TEXT
);

"""

cursor.execute(query)
conn.commit()
conn.close()