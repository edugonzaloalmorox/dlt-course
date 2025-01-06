import duckdb 
import dlt
import re

conn = duckdb.connect("pokemon_data_pipeline.duckdb")

# Test the connection
try:
    conn.execute("SELECT 1")  
    print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")

#  Prints the table 
table = conn.sql("SELECT * from pokemon_data_20250106081219.pokemon").df()
                 
print(table)


