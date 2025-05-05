import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Durgha@04"
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS productivity_tracker")
cursor.execute("USE productivity_tracker")
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    task_name VARCHAR(255),
    description TEXT,
    category VARCHAR(100),
    start_time DATETIME,
    end_time DATETIME
)
""")
conn.commit()
cursor.close()
conn.close()
print("Database and table created.")
print("✅ Database 'productivity_tracker' and table 'tasks' created successfully!")