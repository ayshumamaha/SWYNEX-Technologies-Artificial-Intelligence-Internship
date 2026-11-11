import re
import math
from collections import Counter

# ------------------------------------------
# AI-BASED COLLEGE FAQ QUESTION ANSWERING
# ------------------------------------------

faq_data = [
    {
        "category": "Admission",
        "question": "How can I apply for admission?",
        "answer": "Students can apply through the official college admission process."
    },
    {
        "category": "Fees",
        "question": "How can I pay my college fees?",
        "answer": "Fee payments should be completed through the payment method officially provided by the college."
    },
    {
        "category": "Library",
        "question": "What are the library timings?",
        "answer": "The library timings should be checked through the latest official college notice."
    },
    {
        "category": "Attendance",
        "question": "Where can I check attendance requirements?",
        "answer": "Attendance requirements are available in the institution's academic regulations."
    },
    {
        "category": "Examination",
        "question": "Where can I find the exam timetable?",
        "answer": "The examination timetable is published through the official examination notice or portal."
    },
    {
        "category": "Certificates",
        "question": "How can I request a bonafide certificate?",
        "answer": "Students should contact the college office or follow its certificate application procedure."
    },
    {
        "category": "Results",
        "question": "Where can I check my examination results?",
        "answer": "Results should be accessed through the official examination portal, when available."
    },
    {
        "category": "Contact",
        "question": "How can I contact the college office?",
        "answer": "Students can use the contact details published on the official college website."
    },
    {
        "category": "Scholarships",
        "question": "Where can I find scholarship information?",
        "answer": "Scholarship information is available through official college announcements."
    },
    {
        "category": "ID Card",
        "question": "How can I obtain a student ID card?",
        "answer": "Students should contact the appropriate college office for the ID card procedure."
    }
]


# Words that do not add much meaning
stop_words = {
    "a", "an", "the", "is", "are", "was", "were",
    "do", "does", "did", "can", "could", "i",
    "me", "my", "to", "for", "of", "in", "on",
    "and", "or", "what", "where", "how", "when",
    "please", "tell", "about", "would", "should"
}


# ------------------------------------------
# TEXT PREPROCESSING
# ------------------------------------------

def preprocess(text):
    text = text.lower()
    words = re.findall(r"[a-z0-9]+", text)

    processed_words = [
        word for word in words
        if word not in stop_words
    ]

    return processed_words


# ------------------------------------------
# TF-IDF CALCULATION
# ------------------------------------------

def calculate_idf(documents):
    total_documents = len(documents)
    document_frequency = Counter()

    for document in documents:
        unique_words = set(document)
        document_frequency.update(unique_words)

    idf = {}

    for word, frequency in document_frequency.items():
        idf[word] = math.log(
            (total_documents + 1) / (frequency + 1)
        ) + 1

    return idf


def create_tfidf_vector(words, idf):
    word_counts = Counter(words)
    total_words = len(words)

    vector = {}

    if total_words == 0:
        return vector

    for word, count in word_counts.items():
        tf = count / total_words
        vector[word] = tf * idf.get(word, 0)

    return vector


# Prepare FAQ question documents
faq_questions = [
    preprocess(item["question"])
    for item in faq_data
]

# Calculate IDF values
idf_values = calculate_idf(faq_questions)

# Convert FAQ questions into TF-IDF vectors
faq_vectors = [
    create_tfidf_vector(question, idf_values)
    for question in faq_questions
]


# ------------------------------------------
# COSINE SIMILARITY
# ------------------------------------------

def cosine_similarity(vector1, vector2):

    common_words = set(vector1) & set(vector2)

    dot_product = sum(
        vector1[word] * vector2[word]
        for word in common_words
    )

    magnitude1 = math.sqrt(
        sum(value ** 2 for value in vector1.values())
    )

    magnitude2 = math.sqrt(
        sum(value ** 2 for value in vector2.values())
    )

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0

    return dot_product / (magnitude1 * magnitude2)


# ------------------------------------------
# QUESTION ANSWERING
# ------------------------------------------

def get_answer(user_question):

    processed_question = preprocess(user_question)

    if not processed_question:
        return None, 0.0

    user_vector = create_tfidf_vector(
        processed_question,
        idf_values
    )

    best_score = 0.0
    best_index = -1

    for index, faq_vector in enumerate(faq_vectors):

        score = cosine_similarity(
            user_vector,
            faq_vector
        )

        if score > best_score:
            best_score = score
            best_index = index

    # Similarity threshold
    threshold = 0.35

    if best_index != -1 and best_score >= threshold:

        answer = faq_data[best_index]["answer"]

        return answer, best_score

    return None, best_score


# ------------------------------------------
# MAIN APPLICATION
# ------------------------------------------

def main():

    print("=" * 55)
    print("   AI-BASED COLLEGE FAQ QUESTION ANSWERING SYSTEM")
    print("=" * 55)

    while True:

        print("\n1. Ask a Question")
        print("2. View Available FAQ Categories")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            question = input("\nEnter your question: ").strip()

            if not question:
                print("\nPlease enter a valid question.")
                continue

            answer, score = get_answer(question)

            print("\n" + "-" * 55)

            if answer is not None:

                print("Answer:", answer)
                print("Similarity Score:", round(score, 3))

            else:

                print(
                    "Sorry, the requested information "
                    "is not available in the FAQ dataset."
                )

                print("Similarity Score:", round(score, 3))

            print("-" * 55)

        elif choice == "2":

            print("\nAVAILABLE FAQ CATEGORIES")

            categories = sorted({
                item["category"]
                for item in faq_data
            })

            for category in categories:
                print("-", category)

        elif choice == "3":

            print("\nThank you for using the FAQ system!")
            print("Exiting application...")
            break

        else:

            print("\nInvalid choice. Please enter 1, 2, or 3.")


# ------------------------------------------
# PROGRAM EXECUTION
# ------------------------------------------

if __name__ == "__main__":
    main()

