import sqlite3
import pandas as pd

conn = sqlite3.connect('football.db')
cursor = conn.cursor()

query = """
    SELECT * 
    FROM teams;
"""

cursor.execute(query)
results = cursor.fetchall()
conn.close()

#records_df = pd.DataFrame(results, columns = ['id', 'x', 'y'])
#print(records_df)

lenghts = []
for results in results:
    lenghts.append(len(results[1]))
    

print(lenghts)
