import sqlite3

# Create database
conn = sqlite3.connect("college.db")

# Create cursor
cursor = conn.cursor()

# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    marks INTEGER
)
""")

# Insert sample data
students = [
    (1, "Ravi", "CSE", 85),
    (2, "Priya", "ECE", 72),
    (3, "Anil", "CSE", 91),
    (4, "Sita", "EEE", 65),
    (5, "Rahul", "CSE", 78)
]

cursor.executemany(
    "INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?)",
    students
)

conn.commit()
conn.close()

print("Database created successfully!")