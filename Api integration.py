import requests
import psycopg2

# Step 1: Call the API
response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()

# Step 2: Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Step 3: Create table (if not exists)
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY,
    name TEXT,
    username TEXT,
    email TEXT
)
""")
conn.commit()

# Step 4: Insert data
for user in users:
    cur.execute("""
        INSERT INTO users (id, name, username, email)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
    """, (user['id'], user['name'], user['username'], user['email']))

conn.commit()

# Step 5: Close connection
cur.close()
conn.close()

print("Data inserted successfully.")
