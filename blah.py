import sqlite3

# Sample data (replace with your actual database connection and query)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER, name TEXT, email TEXT)")
cursor.execute("INSERT INTO users VALUES (1, 'Alice', 'alice@example.com')")
cursor.execute("INSERT INTO users VALUES (2, 'Bob', 'bob@example.com')")
conn.commit()

cursor.execute("SELECT id, name, email FROM users")
rows = cursor.fetchall()

# Get column names from cursor.description
column_names = [description[0] for description in cursor.description]

# Convert list of tuples to list of dictionaries
result_dicts = [dict(zip(column_names, row)) for row in rows]

print(result_dicts)

conn.close()