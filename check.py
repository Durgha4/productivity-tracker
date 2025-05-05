import mysql.connector
print("✅ mysql-connector-python is installed and working!")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Durgha@04"
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE productivity_tracker")
conn.close()
print("✅ Database 'productivity_tracker' created successfully!")