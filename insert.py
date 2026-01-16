import sqlite3

conn = sqlite3.connect('football.db')
cursor = conn.cursor()
query = """
INSERT INTO teams (x, y) 
VALUES 
('Buffalo','Bills'),
('Denver','Broncos'),
('Houstan','Texans'),
('New England', 'Patriots'),
('San Francisco', '49ers'),
('Seattle', 'Seahawks'),
('Los Angeles', 'Rams'),
('Chicago', 'Bears')
"""

cursor.execute(query)
conn.commit()
conn.close()