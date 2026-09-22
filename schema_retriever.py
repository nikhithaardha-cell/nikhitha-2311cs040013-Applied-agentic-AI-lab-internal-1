import sqlite3

def get_schema():

    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    # Get all tables
    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
    """)

    tables = cursor.fetchall()

    schema = ""

    for table in tables:

        table_name = table[0]

        # Get columns
        cursor.execute(f"PRAGMA table_info({table_name})")

        columns = cursor.fetchall()

        schema += f"\nTable: {table_name}\n"

        for column in columns:
            column_name = column[1]
            data_type = column[2]

            schema += f"- {column_name} ({data_type})\n"

    conn.close()

    return schema


# Test retrieval
schema = get_schema()

print("Retrieved Database Schema:")
print(schema)
