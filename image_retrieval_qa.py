import os

# ---------------------------------------
# IMAGE RETRIEVAL + VISUAL QA SYSTEM
# ---------------------------------------

# Image database
image_database = {
    "cat.jpg": {
        "objects": ["cat", "animal"],
        "color": "white",
        "location": "home"
    },

    "car.jpg": {
        "objects": ["car", "vehicle"],
        "color": "red",
        "location": "road"
    },

    "tree.jpg": {
        "objects": ["tree", "plant"],
        "color": "green",
        "location": "park"
    },

    "dog.jpg": {
        "objects": ["dog", "animal"],
        "color": "brown",
        "location": "park"
    }
}


# ---------------------------------------
# STEP 1: IMAGE RETRIEVAL
# ---------------------------------------

def retrieve_image(query):

    query = query.lower()

    for image, information in image_database.items():

        # Search objects, color and location
        searchable_data = (
            information["objects"]
            + [information["color"]]
            + [information["location"]]
        )

        if any(word in query for word in searchable_data):
            return image, information

    return None, None


# ---------------------------------------
# STEP 2: VISUAL QUESTION ANSWERING
# ---------------------------------------

def answer_question(image, information, question):

    question = question.lower()

    if "what" in question and "object" in question:
        return "The image contains " + ", ".join(information["objects"])

    elif "what color" in question:
        return "The main color is " + information["color"]

    elif "where" in question:
        return "The image shows a scene from a " + information["location"]

    elif "animal" in question:
        if "animal" in information["objects"]:
            return "Yes, an animal is present in the image."
        else:
            return "No animal is present in the image."

    else:
        return "I cannot answer that question."


# ---------------------------------------
# STEP 3: MULTIMODAL PIPELINE
# ---------------------------------------

print("======================================")
print(" IMAGE RETRIEVAL + VISUAL QA SYSTEM")
print("======================================")

query = input("\nEnter image search query: ")

image, information = retrieve_image(query)

if image is None:

    print("\nNo matching image found.")

else:

    print("\nRetrieved Image:", image)

    question = input("Ask a question about the image: ")

    answer = answer_question(
        image,
        information,
        question
    )

    print("\nAnswer:", answer)