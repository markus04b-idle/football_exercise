import sqlite3

conn = sqlite3.connect('football.db')
cursor = conn.cursor()
query = """
    DELETE FROM teams WHERE id < 9;
"""

cursor.execute(query)
conn.commit()
conn.close() 