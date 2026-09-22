import ollama

question = "Show me all students who scored above 80."

schema = """
Table: students

Columns:
id INTEGER
name TEXT
department TEXT
marks INTEGER
"""

prompt = f"""
You are a Text-to-SQL assistant.

Database schema:
{schema}

User question:
{question}

Generate only the SQL query.
Do not explain anything.
"""

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

sql = response["message"]["content"]

print("Generated SQL:")
print(sql)