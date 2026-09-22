# Fine-Tuning / Domain Adaptation Simulation
# Specialized AI Assistant for Hospital Domain

print("========================================")
print("   HOSPITAL DOMAIN ADAPTATION SYSTEM")
print("========================================")

# Hospital domain knowledge
hospital_data = {
    "appointment": "Patients can book an appointment through the hospital reception or online appointment system.",
    "emergency": "The emergency department is available 24 hours a day for urgent medical conditions.",
    "visiting": "Hospital visiting hours are from 10 AM to 12 PM and 4 PM to 7 PM.",
    "admission": "Patients generally need an identification document, medical records, and insurance information for admission.",
    "departments": "The hospital provides Cardiology, Neurology, Orthopedics, Pediatrics, Dermatology, and General Medicine.",
    "ambulance": "The hospital provides emergency ambulance services for patients requiring urgent transportation.",
    "laboratory": "The hospital provides blood tests, urine tests, imaging, and other diagnostic laboratory services.",
    "pharmacy": "The hospital pharmacy provides medicines according to prescriptions from authorized doctors."
}

# Training / Domain Adaptation
print("\nTraining specialized hospital model...")

for key in hospital_data:
    print("Learning:", key)

print("\nDomain adaptation completed!")

# Hospital AI model
def hospital_ai(question):

    question = question.lower()

    if "appointment" in question or "book" in question:
        return hospital_data["appointment"]

    elif "emergency" in question:
        return hospital_data["emergency"]

    elif "visiting" in question or "visitor" in question:
        return hospital_data["visiting"]

    elif "admission" in question or "documents" in question:
        return hospital_data["admission"]

    elif "department" in question:
        return hospital_data["departments"]

    elif "ambulance" in question:
        return hospital_data["ambulance"]

    elif "laboratory" in question or "test" in question:
        return hospital_data["laboratory"]

    elif "pharmacy" in question or "medicine" in question:
        return hospital_data["pharmacy"]

    else:
        return "Sorry, I do not have information about this hospital service."

# Evaluation questions
test_questions = [
    "How can I book an appointment?",
    "Where is the emergency service?",
    "What are the visiting hours?",
    "What documents are required for admission?",
    "What departments are available?",
    "Does the hospital have an ambulance?",
    "Does the hospital provide laboratory tests?",
    "Where can I get medicines?"
]

# Evaluation
print("\n========================================")
print("           MODEL EVALUATION")
print("========================================")

correct = 0

for question in test_questions:

    answer = hospital_ai(question)

    if "Sorry" not in answer:
        correct += 1

    print("\nQuestion:", question)
    print("Answer:", answer)

# Accuracy
accuracy = (correct / len(test_questions)) * 100

print("\n========================================")
print("Evaluation Accuracy:", accuracy, "%")
print("========================================")

# Interactive chatbot
print("\nHospital AI Assistant")
print("Type 'exit' to stop.")

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Hospital AI: Thank you!")
        break

    print("Hospital AI:", hospital_ai(question))
