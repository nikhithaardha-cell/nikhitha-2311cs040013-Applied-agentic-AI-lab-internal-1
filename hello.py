# Prompt Chaining for Summarization
# No external libraries required

text = """
Artificial Intelligence is a technology that enables computers to
perform tasks that normally require human intelligence. AI is used
in healthcare, education, finance and transportation. Machine
Learning is a part of AI that allows computers to learn from data
and improve their performance. AI helps organizations automate
tasks, make decisions and solve complex problems.
"""

# Step 1: Extract important sentences
sentences = text.strip().split(".")

important_points = sentences[:3]

# Step 2: Create a draft summary
draft_summary = ". ".join(important_points) + "."

# Step 3: Create final summary
final_summary = (
    "Artificial Intelligence enables computers to perform "
    "human-like tasks. It is used in many fields, while "
    "Machine Learning helps computers learn from data."
)

print("===== ORIGINAL TEXT =====")
print(text)

print("\n===== STEP 1: KEY POINTS =====")
for i, point in enumerate(important_points, 1):
    print(i, ".", point.strip())

print("\n===== STEP 2: DRAFT SUMMARY =====")
print(draft_summary)

print("\n===== STEP 3: FINAL SUMMARY =====")
print(final_summary)