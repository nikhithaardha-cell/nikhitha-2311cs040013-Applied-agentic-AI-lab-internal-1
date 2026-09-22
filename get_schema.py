import sqlite3

# Connect to database
conn = sqlite3.connect("college.db")

cursor = conn.cursor()

# Get table information
cursor.execute("PRAGMA table_info(students)")

columns = cursor.fetchall()

print("Students Table Schema:")
print()

for column in columns:
    print("Column:", column[1])
    print("Data Type:", column[2])
    print()

conn.close()