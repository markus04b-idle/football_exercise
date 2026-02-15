import sqlite3
import gradio as gr
import pandas as pd

def fetch_points():
    conn = sqlite3.connect('football.db')
    cursor = conn.cursor()
    query = """ 
        SELECT *
        FROM teams;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    records_df = pd.DataFrame(results, columns=['id', 'x', 'y'])
    return records_df

iface = gr.Interface(fn=fetch_points, inputs=[], outputs=gr.Dataframe(headers=['id', 'x', 'y']))

iface.launch()