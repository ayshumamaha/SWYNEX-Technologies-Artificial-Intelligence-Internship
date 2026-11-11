# TASK 4 Final Project: AI-Based FAQ Question Answering System

## 1. Project Overview

The AI-Based FAQ Question Answering System is a Python-based chatbot developed as part of the AI Internship at SWYNEX Technologies.

The project aims to simplify access to frequently requested college-related information by allowing users to ask questions in natural language. Instead of manually searching through documents or contacting administrative staff, users can interact with the chatbot to retrieve relevant predefined answers.

The final prototype uses a pretrained Sentence Transformer model, `all-MiniLM-L6-v2`, for semantic question matching. It also incorporates model evaluation, similarity threshold comparison, failure-case analysis, and an interactive Gradio interface.

## 2. Problem Statement

Students frequently need information about college admissions, fees, attendance, examinations, library facilities, scholarships, certificates, and other administrative services.

Finding this information manually can be time-consuming. Traditional keyword-based FAQ systems may also fail when users phrase questions differently from the stored questions.

This project addresses the problem by developing a semantic FAQ retrieval system that identifies questions with similar meanings and returns the corresponding stored answers.

## 3. Project Objectives

- Develop an AI-based FAQ question-answering prototype.
- Use a pretrained language model for semantic question matching.
- Retrieve relevant answers from a predefined FAQ dataset.
- Evaluate retrieval performance using test questions.
- Compare different similarity thresholds.
- Identify failure cases and unsupported questions.
- Provide an interactive chatbot interface.

## 4. Methodology

The project uses a pretrained Sentence Transformer model called `all-MiniLM-L6-v2`.

### Workflow

1. **FAQ Dataset Preparation:** Prepare a collection of college-related questions, keywords, categories, and predefined answers.
2. **Text Embedding:** Convert FAQ questions and keywords into numerical vector representations using the pretrained model.
3. **User Input:** Accept a question entered by the user.
4. **Semantic Matching:** Convert the user question into an embedding.
5. **Similarity Calculation:** Calculate cosine similarity between the user question and stored FAQ embeddings.
6. **Answer Retrieval:** Return the answer associated with the most relevant FAQ when the similarity score meets the configured threshold.
7. **Fallback Handling:** Display a fallback message when no FAQ meets the threshold.

### Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Sentence Transformers | Semantic text embeddings |
| all-MiniLM-L6-v2 | Pretrained embedding model |
| PyTorch | Model computation |
| Pandas | Data handling and evaluation |
| Gradio | Interactive chatbot interface |
| Google Colab | Development and execution |

## 5. Demo and Execution

The prototype is implemented in a Google Colab notebook and provides an interactive interface through Gradio.

### How to Run

1. Open `Task3_FAQ_Chatbot.ipynb` in Google Colab.
2. Connect to a runtime.
3. Run the complete implementation cell.
4. Allow the required libraries and pretrained model to load.
5. Review the model evaluation and threshold comparison results.
6. Open the Gradio interface link generated after execution.
7. Enter a college-related question and examine the chatbot's response.

### Example Questions

- How can I apply for admission?
- Where can I find information about college fees?
- What are the library timings?
- How can I obtain my student ID card?
- How do I apply for a scholarship?

The chatbot returns a predefined answer when a sufficiently similar FAQ is identified. Otherwise, it displays a fallback response.

**Demo requirements:** An internet connection is required to install dependencies and download the pretrained model. No Gemini API key or paid API is required. The temporary Gradio sharing link remains available only while the notebook session is active.

## 6. Model Evaluation

The prototype includes evaluation examples to examine its retrieval behaviour.

The evaluation covers:

- In-scope question retrieval.
- Out-of-scope question rejection.
- Similarity threshold comparison.
- Incorrect or ambiguous matches.
- Failure-case analysis.

The implementation compares similarity thresholds of 0.30, 0.40, 0.50, and 0.60.

Evaluation results should be taken from the actual notebook execution. Similarity scores alone do not establish that an answer is factually correct.

## 7. Limitations

- The FAQ dataset contains illustrative college-related information and is not connected to a verified institution database.
- The system can answer only questions covered by its predefined FAQ entries.
- Ambiguous or differently phrased questions may produce incorrect matches.
- A high similarity score does not guarantee that the retrieved answer is correct.
- The system retrieves existing answers rather than generating new responses.
- The prototype does not access live college websites, student portals, or administrative databases.
- The Gradio demo link is temporary and depends on the active notebook session.
- The pretrained model requires an initial internet connection for download.

## 8. Ethical Considerations

The project follows basic responsible AI principles:

### Privacy and Data Protection
The prototype does not require personal student information, passwords, or confidential academic records. Users should avoid entering sensitive personal information.

### Transparency
Users should be informed that the chatbot retrieves predefined FAQ answers and does not independently verify institutional policies.

### Accuracy and Reliability
The system should not be treated as an authoritative source for important administrative decisions. Users should verify critical information with the relevant college department.

### Bias and Fairness
The FAQ dataset should cover different categories of student queries and be reviewed to avoid systematically excluding particular groups of users.

### Responsible Use
The chatbot should not be used to make admission, scholarship, examination, or other high-impact decisions. Unsupported questions should be referred to appropriate institutional staff.

## 9. Future Enhancements

- Expand the dataset using verified college information.
- Integrate an official college website or database.
- Add multilingual question support.
- Improve retrieval through a larger and more diverse evaluation dataset.
- Introduce user feedback to improve FAQ matching.
- Deploy the chatbot as a permanent web application.
- Add secure integration with institutional services where appropriate.

## 10. Conclusion

The final project demonstrates a semantic FAQ question-answering prototype using a pretrained Sentence Transformer model. It combines natural-language question matching with predefined answer retrieval, evaluation examples, threshold comparison, failure-case analysis, and an interactive Gradio interface.

The project provides a foundation for developing more reliable and accessible institutional FAQ systems while recognising the importance of data quality, privacy, transparency, and responsible AI use.

## 11. Repository Structure

```text
Improved-AI-FAQ-Question-Answering-System/
│
├── Task1_FAQ_Use_Case.md
├── Task2_FAQ_Prototype.ipynb
├── Task3_FAQ_Chatbot.ipynb
├── README.md
└── requirements.txt
```

## Author
M. Ayshwarya
