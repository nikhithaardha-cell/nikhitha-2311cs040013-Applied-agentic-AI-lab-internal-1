import sqlite3
import ollama

from schema_retriever import get_schema


# ==========================================
# STEP 1: Get user question
# ==========================================

question = input("Ask your question: ")


# ==========================================
# STEP 2: Retrieve database schema
# ==========================================

schema = get_schema()

print("\nRetrieved Database Schema:")
print(schema)


# ==========================================
# STEP 3: Create SQL generation prompt
# ==========================================

prompt = f"""
You are a Text-to-SQL assistant.

Convert the user's question into a valid SQLite SQL query.

Database schema:
{schema}

User question:
{question}

Rules:
1. Generate only SQL.
2. Do not explain anything.
3. Use only tables and columns from the schema.
4. Only generate SELECT queries.
5. Do not use DROP, DELETE, UPDATE, INSERT, ALTER, or CREATE.
"""


# ==========================================
# STEP 4: Generate SQL using Ollama
# ==========================================

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)


# ==========================================
# STEP 5: Clean generated SQL
# ==========================================

sql = response["message"]["content"].strip()

sql = sql.replace("```sql", "")
sql = sql.replace("```", "")
sql = sql.strip()

print("\nGenerated SQL:")
print(sql)


# ==========================================
# STEP 6: Safety check
# ==========================================

forbidden_words = [
    "DROP",
    "DELETE",
    "UPDATE",
    "INSERT",
    "ALTER",
    "CREATE"
]

sql_upper = sql.upper()

for word in forbidden_words:

    if word in sql_upper:

        print("\nUnsafe SQL detected!")
        print("Query was not executed.")

        exit()


if not sql_upper.startswith("SELECT"):

    print("\nOnly SELECT queries are allowed.")
    print("Query was not executed.")

    exit()


# ==========================================
# STEP 7: Execute SQL
# ==========================================

try:

    conn = sqlite3.connect("college.db")

    cursor = conn.cursor()

    cursor.execute(sql)

    results = cursor.fetchall()

    column_names = [
        description[0]
        for description in cursor.description
    ]

    conn.close()


except Exception as e:

    print("\nSQL Execution Error:")
    print(e)

    exit()


# ==========================================
# STEP 8: Display database results
# ==========================================

print("\nQuery Results:")
print("-" * 40)

print(" | ".join(column_names))

print("-" * 40)

for row in results:

    print(" | ".join(str(value) for value in row))

print("-" * 40)

print(f"Total rows: {len(results)}")


# ==========================================
# STEP 9: Ask LLM to explain results
# ==========================================

result_prompt = f"""
You are a helpful database assistant.

The user asked:
{question}

The SQL query was:
{sql}

The database returned:
{results}

Give a simple natural-language answer to the user.

Do not mention internal technical details unless necessary.
Keep the answer short and clear.
"""

answer_response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": result_prompt
        }
    ]
)


# ==========================================
# STEP 10: Display final answer
# ==========================================

answer = answer_response["message"]["content"]

print("\nFinal Answer:")
print(answer)